import pandas as pd
import argparse
import matplotlib.pyplot as plt
import os
import numpy as np


df = pd.read_csv("frontier_10.csv", header=None, delimiter=r",")
thread10 = df[0]
time10=df[1]

df = pd.read_csv("frontier_11.csv", header=None, delimiter=r",")
thread11 = df[0]
time11=df[1]

df = pd.read_csv("frontier_12.csv", header=None, delimiter=r",")
thread12 = df[0]
time12=df[1]

nodecount = [1,4,16,64,256,1024]


labelsx= []
labelsx.append("1 node\n 64 cores\n 4 MI250X")
for i in range (1,len(nodecount)): 
  labelsx.append(str(nodecount[i])+" nodes \n"+str(56*nodecount[i])+" cores\n"+str(4*nodecount[i])+" MI250X")


ydata=[]
ydata2=[]
ylabel=[]
ylabel2=[]

for i in [0,int(len(time10)/2)]:
  ydata.append(1.68309E+12*26/time10[i]/10**12)
  ydata2.append(3.8*10**6*26/time10[i])

for i in [0,int(len(time11)/2)]:
  ydata.append(1.74806E+13*26/time11[i]/10**12)
  ydata2.append(40.2*10**6*26/time11[i])

for i in [0,len(time12)-1]:
  ydata.append(1.07915E+14*26/time12[i]/10**12)
  ydata2.append(257.3*10**6*26/time12[i])

for d in ydata:
  ylabel.append('{0:.2f}'.format(d))
  
for d in ydata2:
  ylabel2.append('{:5.2e}'.format(d))

plt.rcParams.update({'font.size': 8})

ax1 = plt.gca()
ax1.plot(thread10,1.68309E+12*26/time10/10**12,label="Level 10",color="gray",marker="s")
ax1.plot(thread11,1.74806E+13*26/time11/10**12,label="Level 11",color="gray",marker="*")
ax1.plot(thread12,1.07915E+14*26/time12/10**12,label="Level 12",color="gray",marker="^")
ax1.set_yscale("log")
ax1.set_ylabel("TFLOP/s")
plt.xscale("log")
plt.xticks(nodecount,labelsx,rotation=0)
ax1.set_yticks(ydata,ylabel)

ax2 = ax1.twinx()

ax2.plot(thread10,3.8*10**6*26/time10,label="Level 10",color="black",marker="s")
ax2.plot(thread11,40.2*10**6*26/time11,label="Level 11",color="black",marker="*")
ax2.plot(thread12,257.3*10**6*26/time12,label="Level 11",color="black",marker="^")
ax2.set_yscale("log")
ax2.set_ylabel("Processed cells per second")
ax2.set_yticks(ydata2,ylabel2)
plt.title("DWD scenario on Frontier")
#plt.grid()
plt.legend()
plt.xlabel("Utilized hardware")
#plt.ylabel("TFLOPs")
plt.tight_layout()
plt.savefig("frontier_both.png")
plt.savefig("frontier_both.pdf")
