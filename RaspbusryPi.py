#!/usr/bin/env python

import FreeFL.freefl as ffl
import BusStop as bs

import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as touch
import BusDisplay as dsp

import time
import threading
import sys
import signal

import BusUpdater as upd

def strip_spaces(string):
    return string.replace(', ',',')

update = True
    
id = "54119"
bus = "W7"
delay = 30

backlight_r = 33
backlight_g = 33
backlight_b = 33
lcd_contrast = 43
    
Stop = bs.BusStop(id)
Disp = dsp.Displayotron()

def update_bus_info():
    try: Stop.update_info()
    except ConnectionError: 
        Stop.status = "ConErr  " + Stop.last_updated()
        print("Connection error " + time.localtime())

def display_bus_times():
    lcd.clear()
    Disp.write_line(0,bus + " from " + id)
    if len(Stop.busstr) > 16:
        Disp.write_line(1,strip_spaces(Stop.busstr))
    else:
        Disp.write_line(1,Stop.busstr)
    Disp.write_line(2,Stop.status)
    
def update_display():
    update_bus_info()
    display_bus_times()


Disp.tidyup()

Disp.set_rgb(backlight_r,backlight_g,backlight_b)
lcd.set_contrast(lcd_contrast)

update_bus_info()
display_bus_times()


Updater = upd.Updater(delay,update_display)
Updater.start_updating()


@touch.on(touch.CANCEL)
def handle_cancel(ch, evt):
    print("Cancel button")
    Updater.stop_updating()
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

signal.pause() # Alternate option
