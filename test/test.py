import wiringpi as wp
import time

# Setup WiringPi library and pins
wp.wiringPiSetup()
PIN = 18  # use GPIO pin 18 (BCM numbering)
wp.softPwmCreate(PIN, 0, 100)  # initialize PWM output

# Define function to set LED color
def set_color(r, g, b):
    wp.softPwmWrite(PIN, r)  # set red value
    wp.softPwmWrite(PIN + 1, g)  # set green value
    wp.softPwmWrite(PIN + 2, b)  # set blue value

# Flash white light for 5 seconds
start_time = time.time()
while time.time() - start_time < 5:
    set_color(100, 100, 100)  # set white color
    time.sleep(0.5)
    set_color(0, 0, 0)  # turn off
    time.sleep(0.5)