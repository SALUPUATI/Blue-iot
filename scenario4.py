# -*- coding: utf-8 -*-
"""
Created on Wed Mars 25 09:32:22 2020
@author: Fekher khelifi
"""
import serial
import random
import time
ser = serial.Serial('/dev/ttyUSB0', 38400, timeout = 0)
n = 0
while n < 255:
   data = ser.readline()
   #print (len (data))
   if (len(data) == 29):
           output  = ((data[20:22]).decode())
           if (len(output) ==2):
              length =str(0)
           elif (len(output) == 3):
              length =str(1)
           elif (len(output) == 4):
              length =str(2)
           command = ("*TRA,1,0,"+length+","+output+",>")+'\r\n'
           ser.write (command.encode())
           print (command)
           time.sleep(10)
   elif (len(data)== 23):
           output = ((data [13:15]).decode())
           if (len(output) ==2):
              length =str(0)
           elif (len(output) == 3):
              length =str(1)
           elif (len(output) == 4):
              length =str(2)
           command = ("*TRA,1,0,"+length+","+output+",>")+'\r\n'
           ser.write (command.encode())
           print (command)
           time.sleep(10)
   else:
           n += 1
           payload = format(n, '02x')
           command = ("*TRA,1,0,0,"+payload+",>")+'\r\n'
           ser.write (command.encode())
           print (command)
           time.sleep(10)
   print (data) 
   print (len(data))
   print (data[20:22])

