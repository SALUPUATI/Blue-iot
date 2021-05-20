# -*- coding: utf-8 -*-
"""
Created on Wed May 17 09:32:22 2020
@author: Fekher khelifi
Sensor Node
1.	Réception du ping "00"
2.	Émission du "00"
3.	Réception du Ttx
4.	Time.sleep(Ttx)
5.	Réception du Req "01"
6.	time.sleep bloque l'émission du data pendant un temps Ttx
7.	Emission du data

"""
import serial
import time
from time import sleep
import threading
def ping():

 ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
 while True:
  A = ser.readline()
  output= ((A[11:13]).decode())
  #print (output)
  if len(A)!=0:
    if (output== '00'):
      command = ("*TRA,0,1,0,00,>")+'\r\n'
      print (ser.readline())
      ser.write(command.encode())
      time.sleep(0.1)
      print (command)
    elif (output!= '00' and output!= '01' and len(output) != 0):
        slep = (int(A[12:15], 16))
        #print (slep)
        print (ser.readline())
        sleep = slep/1000
        print (sleep)
    elif (output == '01'):
      time.sleep(sleep)
      print (ser.readline())
      command = ("*TRA,0,1,2,FF00,>")+'\r\n'
      ser.write(command.encode())
      print (command)
      time.sleep(0.1)
  else:
    time.sleep(0.1)
    #print (ser.readline())
def read():
   ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
#   print (ser.readline())
#   time.sleep(2)



t_1 = threading.Thread(name='ping', target=ping)
t_2 = threading.Thread(name='read', target=read)
t_1.start()
t_2.start()

t_1.join()
t_2.join()

