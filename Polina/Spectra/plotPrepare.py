import matplotlib.pyplot as G

read = open('9.2.txt', 'r')
cmd = read.readline()
Xs = []
Ys = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs.append(float(cmds[0]))
    Ys.append(float(cmds[1]))
    cmd = read.readline();


read = open('12.2.txt', 'r')
cmd = read.readline()  # прочитал строку
Ys1 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Ys1.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('12.1.txt', 'r')
cmd = read.readline()  # прочитал строку
Ys2 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Ys2.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('13.txt', 'r')
cmd = read.readline()  # прочитал строку
Ys3 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Ys3.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('15.txt', 'r')
cmd = read.readline()  # прочитал строку

Ys4 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Ys4.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку
As = []
for i in range (0, len(Xs)-1):
    As.append((Ys1[i] - Ys2[i])/(Ys3[i] - Ys4[i]))
G.plot(Xs, Ys)
G.plot(Xs, As)
G.show()