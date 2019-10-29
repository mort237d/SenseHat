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

for i in range(8):
  for j in range(8):
    sense.set_pixel(i,j, nothing)

R = random.randint(0,255)

for k in range(2):
  sense.set_pixel(k,0, (R, R, 0))
  
x = 0
  
while x<8:
  sense.set_pixel(x, 0, red)
  time.sleep(.25)
  x += 1