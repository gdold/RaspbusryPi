import FreeFL.freefl as ffl
import BusStop as bs

import time
import threading
import sys

def strip_spaces(string):
    return string.replace(' ','')

id = "54119"
delay = 5
    
Stop = bs.BusStop(id)
Stop.update_info()

#print(Stop.busstr)
#print(strip_spaces(Stop.busstr))
#print(Stop.status)

def start_updating(delay):
    Stop.update_info()
    print(Stop.busstr)
    print(Stop.status)
    t = threading.Timer(delay,start_updating,[delay]).start()


start_updating(delay)

time.sleep(2)
print 'iamhere'
sys.exit(0)
print 'ishouldhaveexited'