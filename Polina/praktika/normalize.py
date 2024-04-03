import numpy as np
import math
import matplotlib.pyplot as G

Xs = []
Ys = []
Names = []
n = 0
name = input("Название >>>")
Names.append(name)
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
    n -= - 1
    name = input("Название >>>")
    Names.append(name)
Names.pop()

for i in range(0, len(Xs)):
    max = -1
    for j in range(0, len(Ys[i])):
        if Ys[i][j] > max:
            max = Ys[i][j]
    for j in range(0, len(Ys[i])):
        Ys[i][j] = Ys[i][j]/max

for i in range(0, len(Xs)):
    out = open(Names[i] + '.txt', 'w')
    for j in range(0, len(Xs[0])):
        out.write(str(Xs[0][j]) + " " + str(Ys[i][j]) + "\n")
    out.close()
