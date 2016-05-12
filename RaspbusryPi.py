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
import signal
import requests


def strip_spaces(string):
    return string.replace(', ',',')

update = True
    
stop_id = '490008357S'
bus = "W7"
fetch_delay = 30
refresh_delay = 5

backlight_r = 33
backlight_g = 33
backlight_b = 33
lcd_contrast = 43
    
Stop = fbd.FetchBusData(stop_id)
Disp = dsp.Displayotron()

def fetch_bus_data():
    Stop.fetch_bus_data()

def display_bus_times():
    lcd.clear()
    Disp.write_line(0,bus + " from " + stop_id)
    if len(Stop.busstr) > 16:
        Disp.write_line(1,strip_spaces(Stop.busstr))
    else:
        Disp.write_line(1,Stop.busstr)
    Disp.write_line(2,Stop.status)
    
def refresh_display():
    Stop.refresh_bus_times()
    display_bus_times()


Disp.tidyup()

Disp.set_rgb(backlight_r,backlight_g,backlight_b)
lcd.set_contrast(lcd_contrast)

fetch_bus_data()
refresh_display()


FetchUpdater = upd.Updater(fetch_delay,fetch_bus_data)
RefreshUpdater = upd.Updater(refresh_delay,refresh_display)
FetchUpdater.start_updating()
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


#Updater.stop_updating()

# if __name__ == '__main__':
    # try:
        # try: input = raw_input # Compatibility with Python 2 & 3
        # except NameError: pass
        # input("") # Main thread ends on user pressing enter
        # Updater.stop_updating()
        # Disp.tidyup()
    # except KeyboardInterrupt:
        # print('Keyboard interrupt')
        # Updater.stop_updating()
        # Disp.tidyup()
        # sys.exit(0)

#signal.pause() # Alternate option
