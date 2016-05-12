#!/usr/bin/env python

import FetchBusData as fbd
import UpdaterThread as upd
import time
import threading
import sys



def strip_spaces(string):
    return string.replace(' ','')

update = True
    
stop_id = '490008357S'
bus = "W7"
fetch_delay = 11
refresh_delay = 2
    
Stop = fbd.FetchBusData(stop_id)

def fetch_bus_data():
    Stop.fetch_bus_data()
    
def refresh_bus_times():
    Stop.refresh_bus_times()

def display_bus_times():
    print(Stop.busstr)
    print(Stop.status)
    
def full_update_display():
    fetch_bus_data()
    refresh_bus_times()
    display_bus_times()

def disp():
    refresh_bus_times()
    display_bus_times()

print(bus + " from " + stop_id)
full_update_display()
print(Stop.busstr)
print(Stop.status)

FetchUpdater = upd.Updater(fetch_delay,fetch_bus_data)
RefreshUpdater = upd.Updater(refresh_delay,disp)
FetchUpdater.start_updating()
RefreshUpdater.start_updating()



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