#!/usr/bin/env python

import FetchBusData as fbd
import UpdaterThread as upd

try:
    import BusDisplay as dsp
    is_pi = True
except:
    print("Error importing display library (dot3k library not installed?). Using terminal.")
    import BusDisplayTerm as dsp
    is_pi = False
    
    


import sys
import time

stops = [{'stop_id':'490008357S', 'description':"W7 to F'buryPark", 'line_id':"w7"},{'stop_id':'490008357N', 'description':"W7 to Musw'lHill", 'line_id':"w7"},{'stop_id':'490005826CB', 'description':"91 to Trf'garSqu", 'line_id':"91"}]
stop = 0
    
stop_id = stops[0]['stop_id']
api_key = '?app_id=f1fff9f7&app_key=80c7973c8a779d54159f53c71bdfa5e6'
description = stops[0]['description']
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
    dsp.lcd.clear()
    Disp.write_line(0,stops[stop]['description'])
    if len(Stop.busstr) > 16:
        Disp.write_line(1,strip_spaces(Stop.busstr))
    else:
        Disp.write_line(1,Stop.busstr)
    Disp.write_line(2,Stop.status)
    
def refresh_display():
    Stop.refresh_bus_times()
    display_bus_times()
    Disp.blink_led(0,led_on_time)
    
def cycle_stop(increment=1):
    global stop, Stop
    stop = (stop+increment)%len(stops)
    Stop.reassign_stop(stops[stop]['stop_id'],stops[stop]['line_id'])
    Stop.busstr = ' '*16
    Stop.status = 'Please Wait...  '
    display_bus_times()
    fetch_bus_data()
    refresh_display()
    


    
def create_stop(stop_id,api_key,line_id):
    return fbd.FetchBusData(stop_id,api_key,line_id)
    
def ready_display():
    Disp = dsp.Displayotron()
    Disp.tidyup()
    Disp.set_rgb(backlight_r,backlight_g,backlight_b)
    dsp.lcd.set_contrast(lcd_contrast)
    
    return Disp
    
def start_fetch_updater():
    fetch_bus_data()
    FetchUpdater = upd.Updater(fetch_delay,fetch_bus_data)
    FetchUpdater.start_updating()
    
    return FetchUpdater

def start_refresh_updater():
    refresh_display()
    RefreshUpdater = upd.Updater(refresh_delay,refresh_display)
    RefreshUpdater.start_updating()
    
    return RefreshUpdater
    
def stop_updating():
    FetchUpdater.update = False
    RefreshUpdater.update = False
    
    FetchUpdater.stop_updating()
    RefreshUpdater.stop_updating()

    
Stop = create_stop(stops[stop]['stop_id'],api_key,stops[stop]['line_id'])
Disp = ready_display()
FetchUpdater = start_fetch_updater()
RefreshUpdater = start_refresh_updater()


@dsp.touch.on(dsp.touch.CANCEL)
def handle_cancel(ch, evt):
    print("Cancel button")
    
    stop_updating()
    
    Disp.tidyup()
    sys.exit(0)
    
@dsp.touch.on(dsp.touch.BUTTON)
def handle_button(ch, evt):
    pass
    
@dsp.touch.on(dsp.touch.LEFT)
def handle_left(ch, evt):
    cycle_stop(-1)
    
@dsp.touch.on(dsp.touch.RIGHT)
def handle_right(ch, evt):
    cycle_stop(1)
    
@dsp.touch.on(dsp.touch.UP)
def handle_up(ch, evt):
    pass
    
@dsp.touch.on(dsp.touch.DOWN)
def handle_down(ch, evt):
    pass

if not is_pi: dsp.touch.check_for_inputs()

