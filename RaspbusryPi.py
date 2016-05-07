import FreeFL.freefl as ffl

StopMD = ffl.BusInfo("54119","Hornsey Central Health Centre (MD)")

buses = StopMD.get_live_data()

next_buses = []

for bus in buses:
    time = bus["resDue"].replace(' min','') # Strip ' min' from bus times
    next_buses.append(time)

def times_to_str(bus_times):
    if len(bus_times) == 0: 
        string = "No buses within 30 min"
    else:
        string = ', '.join(bus_times)
        if not next_buses[-1] == 'due': # Add min to end
            string += ' min'            # only if final bus not 'due'
     
    return string

print(times_to_str(next_buses))