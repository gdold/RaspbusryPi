#!/usr/bin/env python

import FreeFL.freefl as ffl
import BusStop as bs

import time
import threading
import sys

import BusUpdater as upd

def strip_spaces(string):
    return string.replace(' ','')

update = True
    
id = "54119"
bus = "W7"
delay = 3
    
Stop = bs.BusStop(id)

def update_bus_info():
    Stop.update_info()

def display_bus_times():
    print(Stop.busstr)
    print(Stop.status)
    
def update_display():
    update_bus_info()
    display_bus_times()


print(bus + " from " + id)
Stop.update_info()
print(Stop.busstr)
print(Stop.status)

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
        sys.exit(0)