from tkinter import *
# подготовка поля
import numpy as np
from tkinter import *
window = Tk()
c = Canvas(window,width=900, height=900) # Холст 1000
c.pack()
window.title('Структурка') # Заголовок

def circ(x, y, r):
    x1=x-r
    x2=x+r
    y1=y-r
    y2=y+r
    c.create_oval(x1, y1, x2, y2)

import random
def p(a):
    for i in a:
        for j in i:
            print(j, end=" ")
        print()

# задаем размеры подложки
size_x = 800
size_y = 800
# размер ячейки, в которую будем помещать сферу
a = 8
b = 8

Na=size_x//a
Nb=size_y//b

arr=[] # относительные координаты сфер
for i in range(Na):
    arr.append([])
    for j in range (Nb):
        arr[i].append([])
        r = 4
        x = r
        y = r
        arr[i][j].append(x)
        arr[i][j].append(y)
        arr[i][j].append(r)
#p(arr)
# каждая ячейка массива Na*Nb содержит в себе массив - пару чисел (координаты центра ОТНОСИТЕЛЬНО ЛЕВОГО НИЖНЕГО УГЛА) и радиус

arr1=arr # абсолютные координаты
for i in range(Na):
    for j in range(Nb):
        arr1[i][j][0]=arr[i][j][0]+a*i+(-1)^j*r
        arr1[i][j][1] = r*j*np.sqrt(3);

p(arr1)


for i in arr1:
    for j in i:
        circ(j[0], j[1], j[2])


window.mainloop()
