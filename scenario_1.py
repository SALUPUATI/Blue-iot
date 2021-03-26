# -*- coding: utf-8 -*-
"""
Created on Wed Mars 23 09:32:22 2021
@author: Fekher khelifi
"""

import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
n = 0
while n < 255:
   data = ser.readline()
   if (len(data) == 29):
           output  = ((data[20:22]).decode())
           command = ("*TRA,1,0,2,FF"+output+",>")+'\r\n'
           ser.write (command.encode())
           time.sleep(10)
   elif (len(data)== 23):
           output = ((data [14:16]).decode())
           command = ("*TRA,1,0,2,FF"+output+",>")+'\r\n'
           ser.write (command.encode())
           time.sleep(10)
   else:
           n += 1
           payload = format(n, '02x')
           command = ("*TRA,1,0,2,FF"+payload+",>")+'\r\n'
           ser.write (command.encode())
           a = (ser.readline())
           time.sleep(10)
   print (data)   
