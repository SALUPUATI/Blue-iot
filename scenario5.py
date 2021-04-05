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
#   print (len (data))
   if (len(data) == 49):
           output  = ((data[38:42]).decode())
          # print (output)
           if (len(output) ==2):
              length =str(0)
           elif (len(output) == 3):
              length =str(1)
           elif (len(output) == 4):
              length =str(2)
           command = ("*TRA,0,1,"+length+","+output+",>")+'\r\n'
           ser.write (command.encode())
           print (data)
           print (command)
           time.sleep(12)
   elif (len(data)== 26):
           output = ((data [17:19]).decode())
           if (len(output) ==2):
              length =str(0)
           elif (len(output) == 3):
              length =str(1)
           elif (len(output) == 4):
              length =str(2)
           command = ("*TRA,2,3,"+length+","+output+",>")+'\r\n'
           ser.write (command.encode())
           print (data)
           print (command)
           time.sleep(12)
   else:
           n += 1
           payload = format(n, '02x')
           command = ("*TRA,0,1,0,"+payload+",>")+'\r\n'
           ser.write (command.encode())
           print (data)
           print (command)
           time.sleep(12)
