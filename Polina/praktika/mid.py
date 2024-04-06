import os

import numpy as np
import math
import matplotlib.pyplot as G
Xs = []
Ys = []
n = 0
#name = input("Название >>>")
files = os.listdir("Folder for mid")
name = files.pop()
for counttt in range(0, len(files)):
    Xs.append([])
    Ys.append([])
    read = open("Folder for mid/" + name, 'r')
    cmd = read.readline()
    while cmd != "" and cmd != " ":
        cmd = cmd.replace("\n", "")
        cmd = cmd.replace('\t', ' ')
        cmds = cmd.split(" ")
        Xs[n].append(float(cmds[0]))
        Ys[n].append(float(cmds[1]))
        cmd = read.readline()
    n -=- 1
    name = files.pop()
#    name = input("Название >>>")

Bs = []
for i in range(0, len(Xs[0])):
    sum = 0
    for j in range(0, len(Xs)):
        sum += Ys[j][i]
    Bs.append(sum/len(Xs))

out = open('../../Tosya/Our_CIE/middle.txt', 'w')
G.plot(Xs[0], Bs)
for i in range(0, len(Xs[0])):
    out.write(str(Xs[0][i]) + " " + str(Bs[i]) + "\n")
out.close()


G.savefig("middle.png")
