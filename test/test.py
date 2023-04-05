import time
import RPi.GPIO as GPIO

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

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setwarnings(False)

# Initialize PWM
pwm_red = GPIO.PWM(LED_PIN, 1000)
pwm_green = GPIO.PWM(LED_PIN, 1000)
pwm_blue = GPIO.PWM(LED_PIN, 1000)

pwm_red.start(0)
pwm_green.start(0)
pwm_blue.start(0)

def set_color(red, green, blue):
    pwm_red.ChangeDutyCycle(red / 255 * 100)
    pwm_green.ChangeDutyCycle(green / 255 * 100)
    pwm_blue.ChangeDutyCycle(blue / 255 * 100)

try:
    while True:
        for color in COLORS:
            set_color(*color)
            time.sleep(DELAY)

except KeyboardInterrupt:
    pass

# Clean up
pwm_red.stop()
pwm_green.stop()
pwm_blue.stop()
GPIO.cleanup()