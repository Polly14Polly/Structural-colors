from tkinter import *

from numpy import random

mathcolors = []
mathcolors.append([random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)])
mathcolors.append([random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)])
mathcolors.append([random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)])
mathcolors.append([random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)])

dX = 0
dY = 0
zoom = 5.0
window = Tk()
w = 1920
h = 1080
c = Canvas(window, width=w, height=h)
c.pack()
sps = open('SpheresList3' + '.txt', 'r')
line = sps.readline()
while line != "":
    x = int(line.split(";")[0])
    y = int(line.split(";")[1])
    r = int(line.split(";")[2])
    m = int(line.split(";")[3])
    print(x,y,r,m)
    c.create_oval(int((x-r+dX)/zoom)+w/2, int((y-r+dY)/zoom)+h/2, int((x+r+dX)/zoom)+w/2, int((y+r+dY)/zoom)+h/2, fill='#{:02x}{:02x}{:02x}'.format( int(mathcolors[m][0]), int(mathcolors[m][1]), int(mathcolors[m][2]) ))
    line = sps.readline()
sps.close()
window.mainloop()