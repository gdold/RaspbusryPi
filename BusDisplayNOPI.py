#import dothat.backlight as backlight
#import dothat.lcd as lcd
#import dothat.touch as touch

#import time

class backlight():
    def __init__(self):
        pass
    def off():
        pass
    def graph_off():
        pass
    def rgb(red,green,blue):
        pass
    def graph_set_led_duty(a,b):
        pass
    def graph_set_led_state(a,b):
        pass
    
class touch():
    CANCEL = 0
    def __init__(self):
        pass
    def on(event):
        def thing(handler):
            pass
        return thing
#    def CANCEL():
#        pass
    
    
class lcd():
    def __init__(self):
        pass
    def clear():
        pass
    def set_cursor_position(position,line):
        pass
    def set_contrast(lcd_contrast):
        pass
    def write(text):
        pass
    

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
