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
  
while True:
  x = random.randint(0,7)
  y = random.randint(0,7)
  
  R = random.randint(0,255)
  G = random.randint(0,255)
  B = random.randint(0,255)

  sense.set_pixel(x, y, (R, G, B))
  time.sleep(.1)