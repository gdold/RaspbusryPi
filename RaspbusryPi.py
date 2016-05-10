import FreeFL.freefl as ffl
import BusStop as bs

import dothat.backlight as backlight
import dothat.lcd as lcd
import BusDisplay as dsp

import time
import threading
import sys

import BusUpdater as upd

def strip_spaces(string):
    return string.replace(' ','')

update = True
    
id = "54119"
bus = "W7"
delay = 30
    
Stop = bs.BusStop(id)
Disp = dsp.Displayotron()

def update_bus_info():
    Stop.update_info()

def display_bus_times():
    lcd.clear()
    Disp.write_line(0,bus + " from " + id)
    Disp.write_line(1,strip_spaces(Stop.busstr))
    Disp.write_line(2,Stop.status)
    
def update_display():
    update_bus_info()
    display_bus_times()


Disp.tidyup()
update_bus_info()
display_bus_times()


Updater = upd.Updater(delay,update_display)
Updater.start_updating()



#Updater.stop_updating()

if __name__ == '__main__':
    try:
        try: input = raw_input # Compatibility with Python 2 & 3
        except NameError: pass
        input("") # Main thread ends on user pressing enter
        
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        Updater.stop_updating()
        Disp.tidyup()
        sys.exit(0)