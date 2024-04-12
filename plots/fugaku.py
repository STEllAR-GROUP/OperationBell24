import pandas as pd
import argparse
import matplotlib.pyplot as plt
import os
import numpy as np


df = pd.read_csv("fugaku_10.csv", header=None, delimiter=r",")
thread10 = df[0]
time10=df[1]

df = pd.read_csv("fugaku_11.csv", header=None, delimiter=r",")
thread11 = df[0]
time11=df[1]

df = pd.read_csv("fugaku_12.csv", header=None, delimiter=r",")
thread12 = df[0]
time12=df[1]

nodecount = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,6144]
labelsx= []
labelsx.append("1 node\n48 cores")
for i in range (1,len(nodecount)): 
  labelsx.append(str(nodecount[i])+" nodes \n"+str(48*nodecount[i])+" cores")

ydata=[]
ylabel=[]


for i in [0,len(time10)-1]:
  ydata.append(1.68309E+12*21/time10[i]/10**12)

for i in [0,int(len(time11)/2)]:
  ydata.append(1.74806E+13*21/time11[i]/10**12)

for i in [0,len(time12)-1]:
  ydata.append(1.07915E+14*26/time12[i]/10**12)

print(ydata)

for d in ydata:
  ylabel.append('{0:.2f}'.format(d))

nodecount.pop(len(nodecount)-1)
labelsx.pop(len(nodecount)-1)

plt.rcParams.update({'font.size': 8})

plt.plot(thread10,1.68309E+12*21/time10/10**12,label="Level 10",color="black",marker="s")
plt.plot(thread11,1.74806E+13*21/time11/10**12,label="Level 11",color="black",marker="*")
plt.plot(thread12,1.07915E+14*26/time12/10**12,label="Level 12",color="black",marker="^")
plt.yscale("log")
plt.xscale("log")
plt.xticks(nodecount,labelsx,rotation=45)
plt.yticks(ydata,ylabel)
plt.title("TFLOPs using DWD scenario on supercomputer Fugaku")
#plt.grid()
plt.legend()
plt.xlabel("Utilized hardware")
plt.ylabel("TFLOPs")
plt.tight_layout()
plt.savefig("fugaku.png")
plt.savefig("fugaku.pdf")
