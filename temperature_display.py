#!/usr/bin/env python3

# temperature_display.py - display the temperature


# bring in the libraries to control the screen

import scrollphathd as sphd
from scrollphathd.fonts import font3x5


# bring in the libraries to monitor the temperature

import bme680
import time


# refresh interval in seconds

REFRESH_INTERVAL = 0.1


# open the temperature sensor and set to 8x oversampling

sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
sensor.set_temperature_oversample(bme680.OS_8X)


# rotate the screen upside-down (power on top) and set
# the font to 3x5 pixels to fit more on the screen
# (default is 5x7)

sphd.rotate(180)
sphd.set_font(font3x5)
sphd.set_brightness(0.8)


# flag to track if the 'running' dot should be display
# this time round

dot = False


# loop forever

while True:
    # get the current temperature

    sensor.get_sensor_data()
    temp = getattr(sensor.data, "temperature")
   
   
    # get the units and decimal parts of the temperature

    units = int(temp)
    decimal = int(temp * 100) % 100
    # DEBUG ONLY -
    #print("%f = %d . %d" % (temp, units, decimal))


    # clear the screen
    
    sphd.clear()


    # print the units part of the temperature
    
    width = sphd.write_string(str(units), brightness=0.3)


    # if we're printing a dot this time round, do that
    
    if dot:
        sphd.set_pixel(width, 4, 0.2)


    # print the tenths part of the temperature, leaving a gap for the dot
    #
    # the '"%02d" % decimal' part prints in a special format: the '2'
    # means '2 characters long', '0' is 'put zeroes at the front, if
    # needed, to make it 2 characters long' and the 'd' means 'print a
    # decimal number'

    sphd.write_string("%02d" % decimal, x=width + 2, brightness=0.2)


    # update the screen

    sphd.show()


    # toggle the dot so we do the opposite thing next time round
    
    dot = not dot


    # wait for a bit

    time.sleep(REFRESH_INTERVAL)
