import csv
import numpy as np
from matplotlib import pyplot as plt

x = []
y = []
y1 = []
y2 = []
y3 = []
cnt = 0

#Interpreting Data
with open("Primary_Data.csv","r") as file:
    csv_reader = csv.reader(file,delimiter=',')
    for row in csv_reader:
            if len(row) != 0:
                y.append(int((row[0].strip(" . 0 0").replace(" ",""))))
                y1.append(int((row[1].strip(" . 0 0").replace(" ",""))))
                y2.append(int(row[2].replace(" ","")))
                y3.append(int(row[3].replace(" ","")))
                cnt +=1
    for i in range(int(cnt)):
        x.append(float(i/(960))*1000)
        

#User Interface -- Selection of Data or Graphs to see
while True:
    print("Please input either 1,2,3,4 or 5\n")
    ans = input("Action: (1)View Humidity Data / (2)View Temperature Data / (3)View CO2 Data / (4)View TVOC Data / (5)View Graphs   ")
    if ans == "1":
        print("Humidity:")
        print("Mean: "+str(np.round(np.mean(y),4))+" Median: "+str(np.round(np.median(y),4))+" Standard Deviation: "+str(np.round(np.std(y),4)))
        print("Min: "+str(np.round(np.amin(y),4))+" Max: "+str(np.round(np.amax(y),4))+" Range: "+str(np.round(np.ptp(y),4))+"\n")
        
    elif ans == "2":
        print("Mean: "+str(np.round(np.mean(y1),4))+" Median: "+str(np.round(np.median(y1),4))+" Standard Deviation: "+str(np.round(np.std(y1),4)))
        print("Min: "+str(np.round(np.amin(y1),4))+" Max: "+str(np.round(np.amax(y1),4))+" Range: "+str(np.round(np.ptp(y1),4))+"\n")

    elif ans == "3":
        print("Mean: "+str(np.round(np.mean(y2),4))+" Median: "+str(np.round(np.median(y2),4))+" Standard Deviation: "+str(np.round(np.std(y2),4)))
        print("Min: "+str(np.round(np.amin(y2),4))+" Max: "+str(np.round(np.amax(y2),4))+" Range: "+str(np.round(np.ptp(y2),4))+"\n")
    
    elif ans == "4":
        print("Mean: "+str(np.round(np.mean(y3),4))+" Median: "+str(np.round(np.median(y3),4))+" Standard Deviation: "+str(np.round(np.std(y3),4)))
        print("Min: "+str(np.round(np.amin(y3),4))+" Max: "+str(np.round(np.amax(y3),4))+" Range: "+str(np.round(np.ptp(y3),4))+"\n")
        
    elif ans == "5":
        break
#First Graph(Temp/ Humidity)
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
fig.suptitle('Humidity/Temperature')
plt.xlabel('Time')
ax1.plot(x, y,'tab:orange',linewidth = 5, label='Humidity(g/m^3)')
ax2.plot(x, y1,'tab:red',linewidth = 5, label='Temperature(°C)')

ax1.legend()
ax2.legend()
plt.show()

#Second Graph(CO2)
plt.xlabel('Time')
plt.ylabel('CO2')

plt.plot(x,y2,linewidth = 5, label='CO2(ppm)')
plt.legend()
plt.show()

#Third Graph(CO2/Temp/Humidity)
fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('CO2 / Humidity / Temperature')

axs[0].plot(x,y2,linewidth = 5, label='CO2(ppm)')
axs[1].plot(x,y,'tab:orange',linewidth = 5, label='Humidity')
axs[2].plot(x,y1,'tab:red',linewidth = 5, label='Temperature(°C)')
plt.xlabel('Time')

axs[0].legend()
axs[1].legend()
axs[2].legend()
plt.show()

#Fourth Graph(CO2/TVOC)
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
fig.suptitle('CO2 / TVOC')
plt.xlabel('Time')
ax1.plot(x, y2,linewidth = 5, label='CO2(ppm)')
ax2.plot(x, y3,'tab:green',linewidth = 5, label='TVOC(ppb)')

ax1.legend()
ax2.legend()
plt.show()

#Fifth Graph(All)
figure, axis = plt.subplots(2, 2)
axis[0, 0].plot(x, y2,linewidth = 5)
axis[0, 0].set_title("CO2(ppm)")

axis[0, 1].plot(x, y3,'tab:green',linewidth = 5)
axis[0, 1].set_title("TVOC(ppb)")

axis[1, 0].plot(x, y,'tab:orange',linewidth = 5)
axis[1, 0].set_title("Humidity")

axis[1, 1].plot(x, y1,'tab:red',linewidth = 5)
axis[1, 1].set_title("Temperature(°C)")
plt.show()
