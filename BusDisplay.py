import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as touch

#import time

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
