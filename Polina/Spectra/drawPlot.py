import numpy as np
import math
import matplotlib.pyplot as G

read = open('1plot.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs1 = []
Ys1 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs1.append(float(cmds[0]))
    Ys1.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('3plot.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs2 = []
Ys2 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs2.append(float(cmds[0]))
    Ys2.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('1plot.1.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs3 = []
Ys3 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs3.append(float(cmds[0]))
    Ys3.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('3plot.1.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs4 = []
Ys4 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs4.append(float(cmds[0]))
    Ys4.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('11.3.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs5 = []
Ys5 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs5.append(float(cmds[0]))
    Ys5.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('prak.2.txt', 'r')
cmd = read.readline()  # прочитал строку
Xs6 = []
Ys6 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs6.append(float(cmds[0]))
    Ys6.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

G.plot(Xs1, Ys1)
G.plot(Xs2, Ys2)
G.plot(Xs3, Ys3)
G.plot(Xs4, Ys4)
G.plot(Xs5, Ys5)
G.plot(Xs6, Ys6)
G.show()