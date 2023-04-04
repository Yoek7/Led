import wiringpi as wp
import time

# Setup WiringPi library
wp.wiringPiSetup()

# Configure SPI interface
SPI_CHANNEL = 0
SPI_SPEED = 800000  # Hz
wp.wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED)

# Define function to set LED color
def set_color(r, g, b):
    data = [0x00, b, g, r]
    wp.wiringPiSPIDataRW(SPI_CHANNEL, bytes(data))

# Flash white light for 5 seconds
start_time = time.time()
while time.time() - start_time < 5:
    set_color(255, 255, 255)  # set white color
    time.sleep(0.5)
    set_color(0, 0, 0)  # turn off
    time.sleep(0.5)