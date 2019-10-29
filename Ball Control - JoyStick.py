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

x = 3
y = 3

draw_screen()
sense.set_pixel(x, y, yellow)

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                if y > 0:
                    y = y - 1
                else:
                    y = 7

                draw_screen()
                sense.set_pixel(x, y, yellow)
            elif event.direction == "down":
                if y < 7:
                    y = y + 1
                else:
                    y = 0

                draw_screen()
                sense.set_pixel(x, y, yellow)
            elif event.direction == "left":
                if x > 0:
                    x = x - 1
                else:
                    x = 7

                draw_screen()
                sense.set_pixel(x, y, yellow)
            elif event.direction == "right":
                if x < 7:
                    x = x + 1
                else:
                    x = 0

                draw_screen()
                sense.set_pixel(x, y, yellow)
            elif event.direction == "middle":
                sense.set_pixel(x, y, green)