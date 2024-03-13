import statistics

import matplotlib.pyplot as G

read = open('aaa.1.txt', 'r')
cmd = read.readline()
Xs = []
Ys = []
while cmd != "" and cmd != " ":
    cmd = cmd.replace("\n", "")
    cmd = cmd.replace('\t', ' ')
    cmds = cmd.split(" ")
    Xs.append(float(cmds[0]))
    Ys.append(float(cmds[1]))
    cmd = read.readline()

As = []
Bs = []
last = 1000
meds = []

for i in range(380, 781, 5):
    for j in range(last, len(Xs)):
        if Xs[j] >= i - 2.5:
            if Xs[j] <= i + 2.5:
                meds.append(Ys[j])
            else:
                last = j
                break
    As.append(i)
    Bs.append(statistics.median(meds))
    meds.clear()

spres = open('aaa.2.txt', 'w')
for i in range(0, len(As)):
    spres.write(str(As[i]) + " " + str(Bs[i]) + "\n")
G.plot(Xs, Ys)
G.plot(As, Bs)
G.show()
