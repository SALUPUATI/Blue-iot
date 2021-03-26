# -*- coding: utf-8 -*-
"""
Created on Wed Mars 23 09:32:22 2021
@author: Fekher khelifi
http://www.electronicwings.com
"""

import RPi.GPIO as GPIO
from time import sleep

ledpin = 12				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 
while True:
    for duty in range(0,57,57):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(5)
    sleep(0.5)
    
    for duty in range(57,-1,-57):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(5)
    sleep(0.5)
