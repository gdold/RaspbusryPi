import requests
import json
import time
from calendar import timegm # convert UTC time to seconds since epoch

url_prefix = 'https://api.tfl.gov.uk/StopPoint/'
#stop_id = '490008357S'
url_suffix = '/Arrivals'
#api_key = '?app_id=f1fff9f7&app_key=80c7973c8a779d54159f53c71bdfa5e6'


class FetchBusData():
    def __init__(self,stop_id,api_key=''):
        self.stop_id = str(stop_id)
        self.api_key = str(api_key)
        self.url = url_prefix + stop_id + url_suffix + api_key
        
        self.fetched_data = []
        
        self.businfo = [] # list of time objects
        self.bus_mins = [] # list of mins to bus in str
        
        self.busstr = 'No info retrieved'
        self.status = 'No info retrieved'
        self.updated = 0.0
        
    def fetch_bus_data(self):
        try:
            fetched_data_raw = requests.get(self.url)
            fetched_string = fetched_data_raw.text
            self.fetched_data = json.loads(fetched_string)
            status_str = 'updated '
            self.updated = time.localtime()
        except requests.ConnectionError: 
            status_str = 'ConnErr '
            print('Connection Error')
            
        time_updated = time.strftime("%H:%M:%S",self.updated)
        self.status = status_str + time_updated
        
    def refresh_bus_times(self):
        self.businfo = []
        for bus in self.fetched_data:
            self.businfo.append( time.strptime(bus['expectedArrival'],"%Y-%m-%dT%H:%M:%SZ") ) # Parse ISO 8601 string to time object
        
        bus_sec_int = [ int(timegm(bus_time) - timegm(time.gmtime())) for bus_time in self.businfo ]
        bus_sec_int.sort()
        bus_min_int = [ bus_time/60 for bus_time in bus_sec_int ] # 59 sec = 0 min
        
        self.bus_mins = []
        for bus_time in bus_min_int:
            if bus_time < -9: # Buses aren't normally 10 mins late
                pass
            elif bus_time < 1:
                self.bus_mins.append('due')
            else:
                self.bus_mins.append(str(bus_time))
                
        self.busstr = 'ERROR generating string'
        if len(self.bus_mins) == 0:
            self.busstr = 'No bus in 30 min'
        else:
            self.busstr = ', '.join(self.bus_mins)
            if not self.bus_mins[-1] == 'due': # Add min to end
                self.busstr += ' min'          # only if final bus not 'due'
        
a = FetchBusData('490008357S')
a.fetch_bus_data()
a.refresh_bus_times()
print a.busstr
print a.status