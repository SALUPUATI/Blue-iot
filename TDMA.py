 # -*- coding: utf-8 -*-
"""
Created on Wed APril 15 09:32:22 2020
@author: Fekher khelifi
"""
import serial
import threading
import time
import datetime
now = datetime.datetime.now()
def seriall():
  ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
  while True:
    localtime = time.localtime()
    result = int (time.strftime("%S", localtime))
    time.sleep(0.5)
    A = ser.readline()
    #print (A)
    if len(A)>6:
#       print (result)
       print (A)
def TDMA ():
  ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
  while True:
    data = ser.readline()
    command = ("*TX,0,1,0A5,!A083")+'\r\n'
    ser.write (command.encode())
    time.sleep(10)
    print (command)
    #print (data)

t_1 = threading.Thread(name='seriall', target=seriall)
t_2 = threading.Thread(name='TDMA', target=TDMA)
t_1.start()
t_2.start()

t_1.join()
t_2.join()