from tkinter import *


window = Tk()
c = Canvas(window, width=1920, height=1080)
c.pack()
sps = open('SpheresList3' + '.txt', 'r')
line = sps.readline()
while line != "":
    m = int(line.split(";")[3])
    c.create_oval(int(line.split(";")[0])/20-int(line.split(";")[2])/20, int(line.split(";")[1])/20-int(line.split(";")[2])/20, int(line.split(";")[0])/20+int(line.split(";")[2])/20, int(line.split(";")[1])/20+int(line.split(";")[2])/20, fill='#{:02x}{:02x}{:02x}'.format( int(mathcolors[m][0]), int(mathcolors[m][1]), int(mathcolors[m][2]) ))
    line = sps.readline()
sps.close()
window.mainloop()