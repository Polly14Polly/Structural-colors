import numpy as np
import math
import matplotlib.pyplot as G

read = open('12.1.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs = []
Ys = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")

    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs.append(float(cmds[0]))
    Ys.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

G.plot(Xs, Ys)
G.show()