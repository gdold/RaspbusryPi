import FreeFL.freefl as ffl
import time

class BusStop():
    def __init__(self,id):
        self.id = str(id)
        self.businfo = []
        self.status = "No info retrieved"
        self.busstr = "No info retrieved"
        self.updated = 0.0
        
        self.BusInfo =  ffl.BusInfo(self.id,"")
    
    def info_to_str(self,info):
        next_buses = []
        
        for bus in info:
            time = bus["resDue"].replace(' min','') # Strip ' min' from bus times
            next_buses.append(time)

        if len(next_buses) == 0: 
            string = "No bus in 30 min"
        else:
            string = ', '.join(next_buses)
            if not next_buses[-1] == 'due': # Add min to end
                string += ' min'            # only if final bus not 'due'
     
        return string
    
    def last_updated(self):
        #return time.ctime(self.updated) # Returns full formatted date
        return time.strftime("%H:%M:%S",time.localtime(self.updated)) # Returns time only
    
    def update_info(self):
        self.businfo = self.BusInfo.get_live_data()
        
        self.busstr = self.info_to_str(self.businfo)
        
        self.updated = time.time() # Seconds since epoch
        self.status = "updated " + self.last_updated()
        
        return self.busstr
