from sense_hat import SenseHat
import time

sense = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)

def draw_screen():
    sense.clear(blue)

    for i in range(8):
        sense.set_pixel(i, 0, red)
        sense.set_pixel(i, 7, red)
        sense.set_pixel(0, i, red)
        sense.set_pixel(7, i, red)

def next(n):
	return (n+1) % 8

def prev(n):
	if n==0:
		return 7
	else:
		return n-1

x = 3
y = 3

draw_screen()
sense.set_pixel(x, y, yellow)

while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    moved = False

    if 10 < pitch < 180:
        x = prev(x); moved = True
    elif 180 < pitch < 350:
        x = next(x); moved = True

    if 10 < roll < 180:
        y = next(y);
        moved = True
    elif 180 < roll < 350:
        y = prev(y);
        moved = True

    if moved:
        draw_screen()
        sense.set_pixel(x, y, yellow)