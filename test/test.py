import time
import wiringpi as wp

# Configuration
LED_PIN = 1  # Replace this with the WiringPi pin number for your data pin
LED_COUNT = 30
LED_BRIGHTNESS = 255

# Initialize WiringPi
wp.wiringPiSetup()

# Initialize the LED strip
wp.wiringPiSPISetup(0, 8000000)
wp.pinMode(LED_PIN, wp.OUTPUT)
wp.digitalWrite(LED_PIN, wp.LOW)

def send_byte(byte):
    wp.wiringPiSPIDataRW(0, bytearray([byte]))

def send_color(red, green, blue):
    send_byte(0b11100000 | (LED_BRIGHTNESS >> 3))
    send_byte(blue)
    send_byte(green)
    send_byte(red)

def activate_whitelight():
    # Set all LEDs to white
    for i in range(LED_COUNT):
        send_color(255, 255, 255)

    # Show the LEDs for 5 seconds
    wp.digitalWrite(LED_PIN, wp.HIGH)
    time.sleep(0.001)
    wp.digitalWrite(LEDPIN, wp.LOW)
    time.sleep(5)

    # Turn off all LEDs
    for i in range(LED_COUNT):
        send_color(0, 0, 0)

    # Show the LEDs
    wp.digitalWrite(LED_PIN, wp.HIGH)
    time.sleep(0.001)
    wp.digitalWrite(LED_PIN, wp.LOW)

# Main function
def main():
    while True:
        activate_white_light()
        time.sleep(1)

if name == "main":
    main()