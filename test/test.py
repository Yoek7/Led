import mraa
import time

LED_PIN = 10  # Change this to the pin number connected to the LED

led = mraa.Gpio(LED_PIN)
led.dir(mraa.DIR_OUT)

while True:
    # Flash the LED with red color
    led.write(1)
    time.sleep(0.5)
    led.write(0)
    time.sleep(0.5)

    # Flash the LED with green color
    led.write(1)
    time.sleep(0.5)
    led.write(0)
    time.sleep(0.5)

    # Flash the LED with blue color
    led.write(1)
    time.sleep(0.5)
    led.write(0)
    time.sleep(0.5)