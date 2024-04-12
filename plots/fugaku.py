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

plt.rcParams.update({'font.size': 8})

plt.plot(thread10,1.68309E+12*21/time10/10**9,label="Level 10",color="black",marker="s")
plt.plot(thread11,1.74806E+13*21/time11/10**9,label="Level 11",color="black",marker="*")
plt.plot(thread12,1.07915E+14*26/time12/10**9,label="Level 12",color="black",marker="^")
plt.yscale("log")
plt.xscale("log")
plt.xticks([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,6144],["1 core","2 cores ","4 cores","8 cores","16 cores","32 cores","64 cores","128 cores","256 cores","512 cores","1028 cores","2048 cores","4096 cores","6144 cores"],rotation=45)
#plt.yticks(time[0:7],time[0:7])
plt.title("TFLOPs using DWD scenario on supercomputer Fugaku")
plt.grid()
plt.legend()
plt.xlabel("Utilized hardware")
plt.ylabel("TFLOPs")
plt.savefig("fugaku.png")
plt.savefig("fugaku.pdf")
