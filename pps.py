# -*- coding: utf-8 -*-
"""
Created on Wed Mars 1 04:32:22 2021
@author: Fekher khelifi
http://www.electronicwings.com
"""

import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use
                          # Broadcom SOC channel names.

GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(12, 56)   # Initialize PWM on pwmPin 100Hz frequency

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=0                               # set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cycle

try:
  while True:                      # Loop until Ctl C is pressed to stop.
    for dc in range(0, 56, 56):    # Loop 0 to 56 stepping dc by 56 each loop
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.99)             # wait .99 seconds at current LED brightness
      print(dc)
    for dc in range(56, 0, -56):    # Loop 56 to 0 stepping dc down by 56 each l$
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.001)             # wait .001 seconds at current LED brightness
      print(dc)
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()    