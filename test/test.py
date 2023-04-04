import RPi.GPIO as GPIO
import time

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 10  # use GPIO pin 10 (BCM numbering)
GPIO.setup(PIN, GPIO.OUT)

# Define function to set LED color
def set_color(r, g, b):
    for i in range(8):
        if (b & 0x80):
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.0008)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(0.0004)
        else:
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.0004)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(0.0008)
        b <<= 1
        if (g & 0x80):
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.0008)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(0.0004)
        else:
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.0004)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(0.0008)
        g <<= 1
        if (r & 0x80):
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.0008)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(0.0004)
        else:
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.0004)
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(0.0008)
        r <<= 1

# Flash white light for 5 seconds
start_time = time.time()
while time.time() - start_time < 5:
    set_color(255, 255, 255)  # set white color
    time.sleep(0.5)
    set_color(0, 0, 0)  # turn off
    time.sleep(0.5)

# Cleanup GPIO pins
GPIO.cleanup()