# -*- coding: utf-8 -*-
"""
Created on Wed Mars 25 09:32:22 2020
@author: Fekher khelifi
"""
import serial
import random
import threading
import time
import datetime
now = datetime.datetime.now()
def result():
  ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
  while True:
    localtime = time.localtime()
    result = int (time.strftime("%S", localtime))
    time.sleep(0.5)
    A = ser.readline()
    #print (A)
    if len(A)>3:
#       print (result)
       print (A)
def pay ():
  ser = serial.Serial('/dev/ttyUSB0', 38400, timeout = 0)
  n = 0
  while n <255:
    n += 1
    payload = format (n, '02x')
    command = ("*TRA,2,2,2,FF"+payload+",>")+'\r\n'
    ser.write(command.encode())
    time.sleep(12)

t_1 = threading.Thread(name='result', target=result)
t_2 = threading.Thread(name='pay', target=pay)
t_1.start()
t_2.start()

t_1.join()
t_2.join()


