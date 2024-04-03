import numpy as np
import math
import matplotlib.pyplot as G
Xs = []
Ys = []
n = 0
name = input("Название >>>")
while name != " " and name != "":
    Xs.append([])
    Ys.append([])
    read = open(name + '.txt', 'r')
    cmd = read.readline()
    while cmd != "" and cmd != " ":
        cmd = cmd.replace("\n", "")
        cmd = cmd.replace('\t', ' ')
        cmds = cmd.split(" ")
        Xs[n].append(float(cmds[0]))
        Ys[n].append(float(cmds[1]))
        cmd = read.readline()
    n -=- 1
    name = input("Название >>>")

Bs = []
for i in range(0, len(Xs[0])):
    sum = 0
    for j in range(0, len(Xs)):
        sum += Ys[j][i]
    Bs.append(sum/len(Xs))


G.plot(Xs[0], Bs)

out = open('middle.txt', 'w')
for i in range(0, len(Xs[0])):
    out.write(str(Xs[0][i]) + " " + str(Bs[i]) + "\n")

G.savefig("middle.png")
