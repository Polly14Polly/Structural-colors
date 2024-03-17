# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:52:31 2024

@author: polly
"""

import matplotlib.pyplot as plt

data_sig = []
data_dark1 = []
data_dark2 = []
data_lamp = []
# Sig
with open('7.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data_sig.append((x, y))
# Dark1
with open('12.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data_dark1.append((x, y))
# Dark2
with open('15.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data_dark2.append((x, y))
# Lamp
with open('13.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data_lamp.append((x, y))

result = []

for (x, sig), (_, dark1), (_, dark2), (_, lamp) in zip(data_sig, data_dark1, data_dark2, data_lamp):
    if lamp - dark2 != 0:
        y = 10 * (sig - dark1) / (lamp - dark2)
        result.append((x, y))
    else:
        result.append((x, 0))

result_trimmed = [(x, y) for x, y in result if x >= 430 and x <= 780]

plt.plot([x for x, _ in result_trimmed], [y for _, y in result_trimmed])
plt.xlabel('Wavelenght')
plt.ylabel('Sct. Int. (a.u.)')
plt.show()

spres = open('prak.txt', 'w')
for i in range(0, len(result)):
    spres.write(str(result[i][0]) + " " + str(result[i][1]) + "\n")