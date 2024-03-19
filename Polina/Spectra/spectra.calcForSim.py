# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:52:31 2024

@author: polly
"""

import matplotlib.pyplot as plt

data_sig = []

data_lamp = []
# Sig
with open('1plot.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data_sig.append((x, y))
# Lamp
with open('lampBis.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        data_lamp.append((x, y))

result = []

for (x, sig), (_, lamp) in zip(data_sig, data_lamp):
    y = (sig) / (lamp)/2
    result.append((x, y))


result_trimmed = [(x, y) for x, y in result if x >= 430 and x <= 780]

plt.plot([x for x, _ in result_trimmed], [y for _, y in result_trimmed])
plt.xlabel('Wavelenght')
plt.ylabel('Sct. Int. (a.u.)')
plt.show()

spres = open('1plot.1.txt', 'w')
for i in range(0, len(result)):
    spres.write(str(result[i][0]) + " " + str(result[i][1]) + "\n")