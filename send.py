#///////////////////////////////////////////////////////////
#//Blue IoT Eolia -  Project
#//
#//Serial / raspberry pi intended for the Mats-LT
#//
#//(C) 2021, Fekher KHELIFI(Fekher.Khelifi@univ-nantes.fr)
#//////////////////////////////////////////////////////////
# Import de la librairie serial
import os
import serial
import time
# Ouverture du port serie avec :
# '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
# 9600 : vitesse de communication
ser = serial.Serial('/dev/ttyUSB1', 38400, timeout=10)
n = 0
while n < 255:
  n += 1
  payload=format(n,'02x')
  time.sleep(0.1)
  command = ("*TRA,1,0,2,00"+ payload+",>")+'\r\n'
  print (command)
# Ecriture de chaque message recu
  ser.write(command.encode())
  data = ser.readline()
  f = open("zoo.txt", "+a")
  f.writelines(command)
  #print (ser.readline())

