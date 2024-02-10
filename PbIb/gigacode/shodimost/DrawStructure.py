from tkinter import *
import keyboard

window = Tk()
c = Canvas(window, width=1920, height=1080)
c.pack()
sps = open('SpheresList8' + '.txt', 'r')
line = sps.readline()

x = 500
y = 25
zoom = 1
while line != "":
    c.create_oval(((int(line.split(";")[0])/2-int(line.split(";")[2])/2)+x)*zoom , ((int(line.split(";")[1])/2-int(line.split(";")[2])/2)+y)*zoom, ((int(line.split(";")[0])/2+int(line.split(";")[2])/2)+x)*zoom, ((int(line.split(";")[1])/2+int(line.split(";")[2])/2)+y)*zoom, fill='green')
    line = sps.readline()
sps.close()
window.mainloop()
