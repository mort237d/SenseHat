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
x = 3
y = 3

sense.clear(blue)

for i in range(8):
    sense.set_pixel(i, 0, red)
    sense.set_pixel(i, 7, red)
    sense.set_pixel(0, i, red)
    sense.set_pixel(7, i, red)

sense.set_pixel(x, y, yellow)


# Define the functions
def up():
    print("up")
    y += 1
    sense.set_pixel(0, y, yellow)


def down():
    sense.clear(0, 0, 255)


def left():
    sense.clear(0, 255, 0)


def right():
    sense.clear(255, 255, 0)


while True:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":

            # Check which direction
            if event.direction == "up":
                up()  # Up arrow
            elif event.direction == "down":
                sense.show_letter("D")  # Down arrow
            elif event.direction == "left":
                sense.show_letter("L")  # Left arrow
            elif event.direction == "right":
                sense.show_letter("R")  # Right arrow
            elif event.direction == "middle":
                sense.show_letter("M")  # Enter key

            # Wait a while and then clear the screen
            time.sleep(0.5)
            sense.clear()