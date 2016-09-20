#import dothat.backlight as backlight
#import dothat.lcd as lcd
#import dothat.touch as touch

import curses # for writing to screen in a manner similar to hat

#import time

class backlight_class():
    def __init__(self):
        pass
    def off(self):
        pass
    def graph_off(self):
        pass
    def rgb(self,red,green,blue):
        pass
    def graph_set_led_duty(self,a,b):
        pass
    def graph_set_led_state(self,a,b):
        pass
    
class touch_class():
    CANCEL = 0
    def __init__(self):
        pass
    def on(self,event):
        def thing(handler):
            pass
        return thing
#    def CANCEL():
#        pass
    
    
class lcd_class():
    def __init__(self):
        self.stdscr = curses.initscr()

        self.position = 0
        self.line = 0
        height = 3; width = 16
        self.win = curses.newwin(height, width, self.line, self.position)
        
    def clear(self,):
        self.win.clear()
    def set_cursor_position(self,position,line):
        self.position = position
        self.line = line
    def set_contrast(self,lcd_contrast):
        pass
    def write(self,text):
        self.win.insstr(self.line,self.position,text)
        self.win.refresh()
    

backlight = backlight_class()
touch = touch_class()
lcd = lcd_class()



class Displayotron():
    def __init__(self):
        pass
   
    def tidyup(self):
        backlight.off()
        backlight.graph_off()
        lcd.clear()
    
    def write_line(self,line,text):
        line = int(line)
        text = str(text)[:16] # Truncate to 16 characters
        
        lcd.set_cursor_position(0,line)
        lcd.write(text)

    def set_rgb(self,red,green,blue):
        red = int(red)
        green = int(green)
        blue = int(blue)
        backlight.rgb(red,green,blue)
    
    def blink_led(self,led,time_on=0.005):
        backlight.graph_set_led_duty(0,1)
        backlight.graph_set_led_state(led,1)
#        time.sleep(time_on) # LED visible even without delay
        backlight.graph_set_led_state(led,0)
