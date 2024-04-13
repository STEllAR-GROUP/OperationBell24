import pandas as pd
import argparse
import matplotlib.pyplot as plt
import os
import numpy as np


df = pd.read_csv("perlmutter_10.csv", header=None, delimiter=r",")
thread10 = df[0]
time10=df[1]

df = pd.read_csv("perlmutter_11.csv", header=None, delimiter=r",")
thread11 = df[0]
time11=df[1]

df = pd.read_csv("perlmutter_12.csv", header=None, delimiter=r",")
thread12 = df[0]
time12=df[1]

nodecount = [1,4,16,64,256,1720]


labelsx= []
labelsx.append("1 node\n 64 cores\n 4 A100")
for i in range (1,len(nodecount)): 
  labelsx.append(str(nodecount[i])+" nodes \n"+str(64*nodecount[i])+" cores\n"+str(4*nodecount[i])+" A100")


ydata=[]
ylabel=[]

thread12[5] = 1475

for i in [0,int(len(time10)/2)]:
  ydata.append(1.68309E+12*26/time10[i]/10**12)

for i in [0,int(len(time11)/2)]:
  ydata.append(1.74806E+13*26/time11[i]/10**12)

for i in [0,len(time12)-1]:
  ydata.append(1.07915E+14*26/time12[i]/10**12)


for d in ydata:
  ylabel.append('{0:.2f}'.format(d))

plt.rcParams.update({'font.size': 8})

plt.plot(thread10,1.68309E+12*26/time10/10**12,label="Level 10",color="black",marker="s")
plt.plot(thread11,1.74806E+13*26/time11/10**12,label="Level 11",color="black",marker="*")
plt.plot(thread12,1.07915E+14*26/time12/10**12,label="Level 12",color="black",marker="^")
plt.yscale("log")
plt.xscale("log")
plt.xticks(nodecount,labelsx,rotation=0)
plt.yticks(ydata,ylabel)
plt.title("TFLOPs using DWD scenario on Perlmutter")
#plt.grid()
plt.legend()
plt.xlabel("Utilized hardware")
plt.ylabel("TFLOPs")
plt.tight_layout()
plt.savefig("perlmutter.png")
plt.savefig("perlmutter.pdf")
