# -*- coding: utf-8 -*-
"""
Created on Wed Mars 23 09:32:22 2021
@author: Fekher khelifi
"""
import serial
import random
import time
from datetime import datetime
ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
while True:
  localtime = time.localtime()
  result = int (time.strftime("%S", localtime))
  time.sleep(1)

  #--------paylaod_1-----------------------------#
  if (result ==10 ):
    Profondeur = random.randint(0,100)#+random.randint(0,8)/2
    print("Profondeur:", Profondeur)
    payload = str(1)  
    payload += format(Profondeur, '02x')
    print ("payload:", payload)
    if (len(payload) ==2):
      length =str(0)
    elif (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,2,"+length+","+payload+",>")+'\r\n'
   # print (command)
    ser.write (command.encode())
    #--------paylaod_2-----------------------------#
  elif (result ==30 ) or  (result == 50) or (result == 40):
    #attitude = random.randint(0,360)+random.randint(0.8)/2
    attitude = random.randint(0,360)+random.randint(0,8)/2
    print("attitude:", attitude)
    payload = str(2)
    #payload += format(int(10*attitude), '02x')
    payload += format(int(10*attitude), '02x')
    print ("payload:", payload)
    if (len(payload) ==2):
      length =str(0)
    elif (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,2,"+length+","+payload+",>")+'\r\n'
    #print (command)
    ser.write (command.encode())

  #--------paylaod_3-----------------------------#
  elif (result == 20):  
    Force = random.randint(0,15000)
    print("Force:",Force)
    payload = str(3)
    payload += format(Force, '02x')
    print ("payload:", payload)
    if (len(payload) ==2):
      length =str(0)
    elif (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,2,"+length+","+payload+",>")+'\r\n'
    #print (command)
    ser.write (command.encode())
  #--------paylaod_4-----------------------------#
  elif (result == 00):
    Température = random.randint(0,100)#+random.randint(0,8)/2
    print("Température:", Température)  
    Tension = random.randint(0,12) #+random.randint(0,8)/2
    print("Tension:", Tension)
    payload = str(4)
    payload += format(Tension, '02x')
    payload += format(Température, '02x')
    print ("payload:", payload)
    if (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,2,"+length+","+payload+",>")+'\r\n'
    #print (command)
    ser.write (command.encode())
#  print (ser.readline())
 
  A = ser.readline()
  now = datetime.now()
  if len(A)>3:
       #print (result)
       print (A)
       g = open("GTM2.txt", "a+")
       f = open ("command1.txt","a+")
       f.writelines(str(now))
       f.writelines(str(command))
       f.write("\r\n")
       g.writelines(str(now))
       g.writelines(str(A))
       g.write("\r\n")