import time
from periphery import GPIO

# Define the GPIO pin number that the SK6812 LED is connected to
LED_PIN = 18

# Define the number of LEDs in the strip
NUM_LEDS = 1

# Initialize the GPIO pin as an output
led = GPIO(LED_PIN, "out")

# Define a function to set the color of the LED
def set_color(red, green, blue):
    # Convert the RGB values to a single 24-bit value
    color = (red << 16) | (green << 8) | blue

    # Send the color data to the LED
    for i in range(NUM_LEDS):
        for j in range(23, -1, -1):
            bit = (color >> j) & 1
            if bit:
                led.write(True)
                time.sleep(0.0008)
                led.write(False)
                time.sleep(0.0004)
            else:
                led.write(True)
                time.sleep(0.0004)
                led.write(False)
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

# Clean up the GPIO pin
led.close()
