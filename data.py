# -*- coding: utf-8 -*-
"""
Created on Wed Mars 23 09:32:22 2021
@author: Fekher khelifi
"""
import random
import time
import json
from datetime import datetime
while True:
  now = datetime.now()
  localtime = time.localtime()
  result = int (time.strftime("%S", localtime))
  time.sleep(1)

  #--------paylaod_1-----------------------------#
  if (result == 10) or  (result == 30) or (result == 50):
    Profondeur = random.randint(0,100)#+random.randint(0,8)/2
    altitude = random.randint(0,360)
    print("altitude:", altitude)
    print("Profondeur:", Profondeur)
    my_details = {'Profondeur': Profondeur,'altitude': altitude,'time':datetime.now()}  
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
    #print (command)
   

  #--------paylaod_2-----------------------------#
  elif (result == 20)  or  (result == 40):  
    Force = random.randint(0,15000)
    print("Force:",Force)
    my_details = {'Force': Force,'time':datetime.now()}
    payload = format(Force, '02x')
 #   print ("payload:", payload)
    if (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,0,"+length+","+payload+",>")+'\r\n'
    #print (command)

  #--------paylaod_3-----------------------------#
  elif (result == 00):
    Temperature = random.randint(0,100)+random.randint(0,8)/2
    print("Temperature:", Temperature)  
    Tension = random.randint(0,12)+random.randint(0,8)/2
    print("Tension:", Tension)
    my_details = {'Tension': Tension,'Temperature': Temperature,'time':datetime.now()}
    payload = format(int(10*Temperature), '02x')
    payload += format(int(10*Tension), '02x')
  #  print ("payload:", payload)
    if (len(payload) ==3):
      length =str(1)
    elif (len(payload) == 4):
      length =str(2)
    elif (len(payload) == 5):
      length =str(3)
    command = ("*TRA,1,0,"+length+","+payload+",>")+'\r\n'
   # print (command)

  #now = datetime.now()
  #f = open("GTM1.txt", "a+")
  #f.writelines(str(now))
  #f.write("\r\n")
  if (result ==00 or result == 10 or result == 20 or result ==30 or result ==40 or result == 50):
    json_object = json.dumps(my_details, indent = 4, default=str)
    with open('data.json', 'a+') as json_file:
      json_file.write(json_object)
      json_file.write(',')

