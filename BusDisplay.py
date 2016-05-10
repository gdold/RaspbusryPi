import dothat.backlight as backlight
import dothat.lcd as lcd

class Displayotron():
    def __init__():
        pass
   
    def tidyup():
        backlight.off()
        backlight.graph_off()
        lcd.clear()
    
    def write_line(line,text):
        line = int(line)
        text = str(text)[:16] # Truncate to 16 characters
        
        lcd.set_cursor_position(0,line)
        lcd.write(text)

