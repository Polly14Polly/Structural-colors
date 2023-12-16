import numpy
import pandas

#Результаты SMUTHI
S = []

#Получение результатов SMUTHI
def get_plot_from_file():
    global S
    file = open(f"{input('Введите названиие файла >>> ')}", "r")
    str_points = file.readlines()
    points = []
    for str_point in str_points:
        arr_str_point = str_point.split()
        S.append(float(arr_str_point[1]))

def mult_integral(delta, *args):
    mult_fun = []
    for i in range(len(args[0])):
        el = 1;
        for fun in args:
            el *= fun[i]
        mult_fun.append(el)

    return sum(mult_fun)*delta

def XYZ2xy(xyz):
    x = xyz[0]
    y = xyz[1]
    s = sum(xyz)
    return (x/s, y/s)


get_plot_from_file()

#Считываем функции всоприятия цветов реепторами глаза
x_ = pandas.read_excel("x2_10deg_05.xlsx")
y_ = pandas.read_excel("y2_10deg_05.xlsx")
z_ = pandas.read_excel("z2deg_05.xlsx")

#Выбираем из тапблицы нужную колонку (1) и строки (1:82)
x_ = x_.iloc[1:82, 1]
y_ = y_.iloc[1:82, 1]
z_ = z_.iloc[1:82, 1]

#Вычисление коэффициента
N = mult_integral(5, y_.tolist(), S)

print(N)

#Вычисление координат цвета
X = (1/N)*mult_integral(5, x_.tolist(), S)
Y = (1/N)*mult_integral(5, y_.tolist(), S)
Z = (1/N)*mult_integral(5, z_.tolist(), S)


print(f"{X} {Y} {Z}")
xy_r = XYZ2xy((X, Y, Z))
print(xy_r)

