import time
from periphery import GPIO

# Replace with the appropriate GPIO pin number
gpio_pin_number = 13

# Initialize GPIO as output
gpio_out = GPIO(gpio_pin_number, "out")

# Set the time delay (in seconds) for toggling the GPIO pin
time_delay = 0.001

try:
    while True:
        # Toggle the GPIO pin to create a square wave
        gpio_out.write(True)
        time.sleep(time_delay)
        gpio_out.write(False)
        time.sleep(time_delay)

except KeyboardInterrupt:
    # Turn off the buzzer when the script is interrupted
    gpio_out.write(False)

finally:
    # Close the GPIO pin
    gpio_out.close()