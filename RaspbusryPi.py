import FreeFL.freefl as ffl
import BusStop as bs

def strip_spaces(string):
    return string.replace(' ','')

id = "54119"
    
Stop = bs.BusStop(id)
Stop.update_info()

print(Stop.busstr)
#print(strip_spaces(Stop.busstr))
print(Stop.status)