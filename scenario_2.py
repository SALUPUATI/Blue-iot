# -*- coding: utf-8 -*-
"""
Created on Wed Mars 23 09:32:22 2021
@author: Fekher khelifi
"""
import serial
import random
import time
from datetime import datetime
ser = serial.Serial('/dev/ttyUSB2', 38400, timeout=0)
while True:
  localtime = time.localtime()
  result = int (time.strftime("%S", localtime))
  time.sleep(1)

  #--------paylaod_1-----------------------------#
  if (result == 10) or  (result == 30) or (result == 50):
    Profondeur = random.randint(0,100)#+random.randint(0,8)/2
    altitude = random.randint(0,360)
    print("altitude:", altitude)
    print("Profondeur:", Profondeur)  
    payload = format(Profondeur, '02x')
    payload += format(altitude, '02x')
#    print ("payload:", payload)
    if (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,0,"+length+","+payload+",>")+'\r\n'
    print (command)
    ser.write (command.encode())

  #--------paylaod_2-----------------------------#
  elif (result == 20)  or  (result == 40):  
    Force = random.randint(0,15000)
    print("Force:",Force)
    payload = format(Force, '02x')
 #   print ("payload:", payload)
    if (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,0,"+length+","+payload+",>")+'\r\n'
    print (command)
    ser.write (command.encode())

  #--------paylaod_3-----------------------------#
  elif (result == 00):
    Température = random.randint(0,100)+random.randint(0,8)/2
    print("Température:", Température)  
    Tension = random.randint(0,12)+random.randint(0,8)/2
    print("Tension:", Tension)
    payload = format(int(10*Température), '02x')
    payload += format(int(10*Tension), '02x')
  #  print ("payload:", payload)
    if (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,0,"+length+","+payload+",>")+'\r\n'
    print (command)
    ser.write (command.encode())
  #print (ser.readline())
  A = ser.readline()
  now = datetime.now()
  if len(A)>3:
       #print (result)
       print (A)
       f = open("GTM1.txt", "a+")
       f.writelines(str(now))
       f.writelines(str(A))
       f.write("\r\n")


