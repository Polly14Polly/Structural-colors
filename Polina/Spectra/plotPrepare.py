import matplotlib.pyplot as G

read = open('9.txt', 'r')
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

read = open('10.txt', 'r')
cmd = read.readline()  # прочитал строку
Ys1 = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Ys1.append(float(cmds[1]))
    cmd = read.readline();  # прочитал строку

read = open('12.txt', 'r')
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
i = 0
while i < len(Xs):
    print(i)
    try:
        As.append((Ys1[i] - Ys2[i]) / (Ys3[i] - Ys4[i]))
    except ArithmeticError:
        Xs.pop(i)
        Ys.pop(i)
        Ys1.pop(i)
        Ys2.pop(i)
        Ys3.pop(i)
        Ys4.pop(i)
        i -= 1
    i += 1

#G.plot(Xs, Ys)
G.plot(Xs, As)
G.show()
spres = open('aaa.txt', 'w')
for i in range(0, len(As)):
    spres.write(str(Xs[i]) + " " + str(As[i]) + "\n")
