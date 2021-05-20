# -*- coding: utf-8 -*-
"""
Created on Wed May 17 09:32:22 2020
@author: Fekher khelifi
Gateway Node
1.      Broadcast ping
2.      Réception ping du nœuds,
3.      Calcule du Ttx
4.      Broadcast Ttx vers le nœud
5.      Broadcast Req
6.      Réception Data

"""
import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=0)
n = 0
while n <4:
      start = time.time()
      command = ("*TRA,0,1,0,00,>")+'\r\n'
      ser.write(command.encode())
      print ('command_1')
      time.sleep(5)
      A = ser.readline()
      output= ((A[17:19]).decode())
      if len(A)!=0 and output =='00':
        end = time.time()
        times = int(1000*((end-start)/2))
        Payload =format(times, '02x')
        commande= ("*TRA,0,1,1,"+Payload+",>")+'\r\n'
        ser.write (commande.encode())
        print ('commande_2')
        #print (Payload)
        time.sleep(5)
        n = 4
      elif len(A)!=0 :
       start = time.time()
       time.sleep(5)
       output= ((A[17:19]).decode())
       if output =='00':
        end = time.time()
        times = int(1000*((end-start)/2)) 
        Payload =format(times, '02x')
        commande= ("*TRA,0,1,1,"+Payload+",>")+'\r\n'
        ser.write (commande.encode())
        print ('commande_3')
        time.sleep(5)
        n = 4
      else:
        n +=1
      print (ser.readline())
while True:
    time.sleep(5)
    command = ("*TRA,0,1,0,01,>")+'\r\n'
    ser.write(command.encode())
    print ('command_4')
    print (ser.readline())
