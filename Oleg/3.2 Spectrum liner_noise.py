import random
import os
import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
import smuthi.simulation
import smuthi.initial_field
import smuthi.layers
import smuthi.particles
import smuthi.postprocessing.far_field as ff
def spectrum(name):
    with open (name) as f:
        arr=f.readlines()

    res=[]
    for i in arr:
        temp=i.replace("\t", " ")
        temp = temp.replace("\n", "")
        ans=temp.split(" ")
        res.append([float(ans[0]), float(ans[1])])
    print(res)

    x=[]
    y=[]
    for i in res:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y)


#spectrum('7.txt')
#spectrum('8.txt')
#spectrum('9.txt')
#spectrum('10.txt')
#spectrum('11.txt')
#spectrum('12.txt')
#spectrum('13.txt')
#spectrum('15.txt')



plt.title("")
plt.xlabel("Wavelength, nm")
plt.ylabel("Normalised cross section")
#plt.legend()
plt.show()