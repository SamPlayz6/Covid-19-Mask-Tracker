import numpy as np
from matplotlib import pyplot as plt

import serial
import time
import csv
data1 = ""
d1 = []
d2 = []
d3 = []
d4 = []


#Open/Reads serial
ser = serial.Serial()
ser.baudrate = 9600
ser.port = "COM5"
ser.open()



while True:
    #Cleaning Data
    data = str(ser.readline())# retrieve and cast data to a string
    data = data.replace("b","")
    data = data.replace("'", "")
    data = data.replace(" ", "")
    data = data.replace("\\r\\n", "")
    

    #Spliting Data
    data = data.split(",")
    data = data[:-1]
    for i in range(len(data)):
        data1 += data[i] + ","
    
    #Sending Data
    time.sleep(2)
    if len(data1) > 0:
        print(data1)
        file = open("Primary_Data.csv", "a")
        k = csv.writer(file, delimiter=' ')
        
        k.writerow(data1+",")
        data1 = ""
        file.close()
    
    
ser.close

