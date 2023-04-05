import time
import RPi.GPIO as GPIO

# Define the GPIO pin number that the SK6812 LED is connected to
LED_PIN = 18

# Define the number of LEDs in the strip
NUM_LEDS = 1

# Initialize the GPIO library
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Define a function to set the color of the LED
def set_color(red, green, blue):
    # Convert the RGB values to a single 24-bit value
    color = (red << 16) | (green << 8) | blue

    # Send the color data to the LED
    for i in range(NUM_LEDS):
        for j in range(23, -1, -1):
            bit = (color >> j) & 1
            if bit:
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.0008)
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.0004)
            else:
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.0004)
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.0008)

# Set the LED color to red
set_color(255, 0, 0)

# Wait for 1 second
time.sleep(1)

# Set the LED color to green
set_color(0, 255, 0)

# Wait for 1 second
time.sleep(1)

# Set the LED color to blue
set_color(0, 0, 255)

# Clean up the GPIO library
GPIO.cleanup()