#import dothat.backlight as backlight
#import dothat.lcd as lcd
#import dothat.touch as touch

import sys # for writing to screen in a manner similar to hat

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
            return True
        return thing
#    def CANCEL():
#        pass
    
    
class lcd_class():
    def __init__(self):
        self.pl = "\033[F"
        self.line = 0
        self.text = [' '*16,' '*16,' '*16]
        
        sys.stdout.write(' '*16+'\n'+' '*16+'\n'+' '*16+'\n')
        
    def clear(self,):
        sys.stdout.write(self.pl*3)
        sys.stdout.write(' '*16+'\n'+' '*16+'\n'+' '*16+'\n')
    def set_cursor_position(self,position,line):
        self.position = position
        self.line = line
    def set_contrast(self,lcd_contrast):
        pass
    def write(self,text):
        self.text[self.line] = text
        sys.stdout.write(self.pl*3)
        sys.stdout.write(self.text[0]+'\n')
        sys.stdout.write(self.text[1]+'\n')
        sys.stdout.write(self.text[2]+'\n')
    

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
