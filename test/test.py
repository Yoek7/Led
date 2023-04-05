import time
import mraa
import board
import neopixel

# Configuration
LED_PIN = 18  # GPIO pin connected to the SK6812 LED
LED_COUNT = 1  # Number of LEDs
DELAY = 0.5  # Delay between color changes in seconds

# Color definitions
COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
]

# Initialize the NeoPixel strip
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

def set_color(color):
    for i in range(LED_COUNT):
        pixels[i] = color
    pixels.show()

try:
    while True:
        for color in COLORS:
            set_color(color)
            time.sleep(DELAY)

except KeyboardInterrupt:
    pass

# Clean up
set_color((0, 0, 0))