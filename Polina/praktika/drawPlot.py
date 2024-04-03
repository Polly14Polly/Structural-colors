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
for i in range(0, len(Xs)):
    G.plot(Xs[i], Ys[i])
G.show()