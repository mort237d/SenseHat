from sense_hat import SenseHat
import random
import time

sense = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
    
sense.clear()

temp = sense.get_temperature()
print(temp)

while True:
  sense.show_message(str(round(temp, 2)), text_colour=yellow, back_colour=blue, scroll_speed=0.05)