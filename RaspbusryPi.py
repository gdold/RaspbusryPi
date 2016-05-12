#!/usr/bin/env python

import FetchBusData as fbd
import BusUpdater as upd

import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as touch
import BusDisplay as dsp

import time
import threading
import sys
import requests

    
stop_id = '490008357S'
api_key = '?app_id=f1fff9f7&app_key=80c7973c8a779d54159f53c71bdfa5e6'
description = "W7 to F'buryPark"
fetch_delay = 30
refresh_delay = 5

backlight_r = 33
backlight_g = 33
backlight_b = 33
lcd_contrast = 43
led_on_time = 0.001
    
def strip_spaces(string):
    return string.replace(', ',',')

def fetch_bus_data():
    Stop.fetch_bus_data()
    Disp.blink_led(5,led_on_time)

def display_bus_times():
    lcd.clear()
    Disp.write_line(0,description)
    if len(Stop.busstr) > 16:
        Disp.write_line(1,strip_spaces(Stop.busstr))
    else:
        Disp.write_line(1,Stop.busstr)
    Disp.write_line(2,Stop.status)
    
def refresh_display():
    Stop.refresh_bus_times()
    display_bus_times()
    Disp.blink_led(0,led_on_time)

Stop = fbd.FetchBusData(stop_id,api_key)
Disp = dsp.Displayotron()

Disp.tidyup()

Disp.set_rgb(backlight_r,backlight_g,backlight_b)
lcd.set_contrast(lcd_contrast)

# Make sure there is data right from start
fetch_bus_data()
refresh_display()

# Two asynchronous threads that update and refresh display at set intervals
FetchUpdater = upd.Updater(fetch_delay,fetch_bus_data)
FetchUpdater.start_updating()
RefreshUpdater = upd.Updater(refresh_delay,refresh_display)
RefreshUpdater.start_updating()


@touch.on(touch.CANCEL)
def handle_cancel(ch, evt):
    print("Cancel button")
    
    FetchUpdater.update = False
    RefreshUpdater.update = False
    
    FetchUpdater.stop_updating()
    RefreshUpdater.stop_updating()
    
    Disp.tidyup()
    sys.exit(0)
