def median(f):
    # Creating buffer
    if not hasattr(median, "buffer"):
        median.buffer = [f] * 3

    # Move buffer to actually values ( [0, 1, 2] -> [1, 2, 3] )
    median.buffer = median.buffer[1:]
    median.buffer.append(f)

    # Calculation median
    a = median.buffer[0]
    b = median.buffer[1]
    c = median.buffer[2]
    middle = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))

    return middle

def easy_mean(f, s_k=0.2, max_k=0.9, d=1.5):
    # Creating static variable
    if not hasattr(easy_mean, "fit"):
        easy_mean.fit = f

    # Adaptive ratio
    k = s_k if (abs(f - easy_mean.fit) < d) else max_k

    # Calculation easy mean
    easy_mean.fit += (f - easy_mean.fit) * k

    return easy_mean.fit

def kalman(f, q=0.25, r=0.7):
    if not hasattr(kalman, "Accumulated_Error"):
        kalman.Accumulated_Error = 1
        kalman.kalman_adc_old = 0

    if abs(f-kalman.kalman_adc_old)/50 > 0.25:
        Old_Input = f*0.382 + kalman.kalman_adc_old*0.618
    else:
        Old_Input = kalman.kalman_adc_old

    Old_Error_All = (kalman.Accumulated_Error**2 + q**2)**0.5
    H = Old_Error_All**2/(Old_Error_All**2 + r**2)
    kalman_adc = Old_Input + H * (f - Old_Input)
    kalman.Accumulated_Error = ((1 - H)*Old_Error_All**2)**0.5
    kalman.kalman_adc_old = kalman_adc

    return kalman_adc

def arith_mean(f, buffer_size=7):
    # Creating buffer
    if not hasattr(arith_mean, "buffer"):
        arith_mean.buffer = [f] * buffer_size

    # Move buffer to actually values ( [0, 1, 2, 3] -> [1, 2, 3, 4] )
    arith_mean.buffer = arith_mean.buffer[1:]
    arith_mean.buffer.append(f)

    # Calculation arithmetic mean
    mean = 1
    for e in arith_mean.buffer: mean *= e
    mean = mean**(1/len(arith_mean.buffer))

    return mean

import numpy as np
import math
import matplotlib.pyplot as G

read = open('13.txt', 'r')
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
As = []
for i in Ys:
    As.append(median(i))
Bs = []
for i in As:
    Bs.append(kalman(i))
Cs = []
for i in Bs:
    Cs.append(kalman(i))
Ds = []
for i in Cs:
    Ds.append(kalman(i))
Es = []
for i in Ds:
    Es.append(kalman(i))
Fs = []
for i in Es:
    Fs.append(arith_mean(i))
Gs = []
for i in Fs:
    Gs.append(easy_mean(i))
Hs = []
for i in Gs:
    Hs.append(easy_mean(i))
G.plot(Xs, Ys)
#G.plot(Xs, Bs)
G.plot(Xs, Hs)


spres = open('lamp.txt', 'w')
for i in range(0, len(Xs)):
    spres.write(str(Xs[i]) + " " + str(Hs[i]/4000) + "\n")

spres.close()
G.show()