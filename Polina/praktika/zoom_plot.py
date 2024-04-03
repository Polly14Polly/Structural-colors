import numpy as np
import math
import matplotlib.pyplot as G

read = open('3plot.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs = []
Ys = []
zoom = 1.425
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs.append(float(cmds[0]))
    Ys.append(float(cmds[1])/zoom)
    cmd = read.readline()  # прочитал строку

G.plot(Xs, Ys)
G.show()


spres = open('3plot.1.txt', 'w')
for i in range(0, len(Xs)):
    spres.write(str(Xs[i]) + " " + str(Ys[i]) + "\n")

