import threading

class Updater():
    def __init__(self,delay,function):
        self.delay = delay
        self.function = function
        self.t = None
    
    def _update(self):
        self.function()
        self.t = threading.Timer(self.delay,self._update)
        self.t.daemon = True
        self.t.start()
    
    def start_updating(self):
        self.t = threading.Timer(self.delay,self._update)
        self.t.daemon = True
        self.t.start()
    
    def stop_updating(self):
        self.t.cancel()
