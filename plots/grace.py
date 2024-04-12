import pandas as pd
import argparse
import matplotlib.pyplot as plt
import os
import numpy as np


df = pd.read_csv("grace.csv", header=None, delimiter=r"\s+")

thread = df[2]

time=df[3]

plt.rcParams.update({'font.size': 8})

plt.plot(thread[0:7],1.68309E+12*25/time[0:7]/10**9,label="Fusion 1",color="black")
plt.plot(thread[7:len(thread)],1.68309E+12*25/time[7:len(time)]/10**9,label="Fusion 8",color="black",ls="--")
plt.yscale("log")
plt.xscale("log")
plt.xticks(thread[0:7],["1 core","2 cores ","4 cores","9 cores","18 cores","36 cores","72 cores"])
plt.yticks(time[0:7],time[0:7])
plt.title("Time using DWD Level 10 scenario on NVIDIA Grace Hopper")
plt.grid()
plt.legend()
plt.xlabel("Utilized hardware")
plt.ylabel("Time [s]")
plt.savefig("grace_hopper.png")
plt.savefig("grace_hopper.pdf")
