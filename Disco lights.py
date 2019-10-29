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

x = 1
  
while True:
  R = random.randint(0,255)
  G = random.randint(0,255)
  B = random.randint(0,255)

  sense.clear(R, G, B)
  time.sleep(x)
  x -= .05