import numpy
import pandas
import colour
import os


#Результаты SMUTHI
S = []

j = []

delta = 0
name = input('Введите названиие файла >>> ')

file = open(f"res/{name}", "r")
str_points = file.readlines()
for str_point in str_points:
    arr_str_point = str_point.split()
    j.append(float(arr_str_point[0]))

delta = j[1] - j[0]

#Получение результатов SMUTHI
def get_plot_from_file():
    global S
    global delta
    global name

    file = open(f"res/{name}", "r")
    str_points = file.readlines()
    points = []
    for str_point in str_points:
        arr_str_point = str_point.split()
        S.append(float(arr_str_point[1]))

def sum_with_scale(array, delta):
    sum = 0
    for i in range(len(array) - 1):
        sum += (array[i] + array[i+1])/2
        i += delta / 5 - 1

    return sum

def mult_integral(delta, *args):
    mult_fun = []
    for i in range(len(args[0])-1):
        el = 1;
        for fun in args:
            if args.index(fun) == 1:
                el *= (fun[int(i*5/delta)]+fun[int(i*5/delta)+1])/2
            else:
                el *= (fun[i]+fun[i+1])/2

        mult_fun.append(el)
        i+= delta/5 - 1
        print(i)

    return sum_with_scale(mult_fun, delta)

get_plot_from_file()

#Считываем функции всоприятия цветов реепторами глаза
x_ = pandas.read_excel("x2_10deg_05.xlsx")
y_ = pandas.read_excel("y2_10deg_05.xlsx")
z_ = pandas.read_excel("z2deg_05.xlsx")

#Выбираем из тапблицы нужную колонку (1) и строки (1:82)
x_ = x_.iloc[1:82, 1]
y_ = y_.iloc[1:82, 1]
z_ = z_.iloc[1:82, 1]

#Вычисление координат цвета
precoords = (mult_integral(delta, x_.tolist(), S), mult_integral(delta, y_.tolist(), S), mult_integral(delta, z_.tolist(), S))

s = sum(precoords)

X = precoords[0]/s
Y = precoords[1]/s
Z = precoords[2]/s

print(f"{X} {Y} {Z}")
xy_r = (X, Y)
print(xy_r)

