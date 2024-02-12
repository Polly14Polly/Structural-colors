import pygame
from settings import *
import numpy
import pandas
import colour
import os

def cie_from_spec(file_name):
    S = []

    j = []

    delta = 0

    file = open(f"{file_name}.txt", "r")
    str_points = file.readlines()
    for str_point in str_points:
        arr_str_point = str_point.split()
        j.append(float(arr_str_point[0]))

    delta = j[1] - j[0]

    # Получение результатов SMUTHI
    def get_plot_from_file():
        file = open(f"{file_name}.txt", "r")
        str_points = file.readlines()
        points = []
        for str_point in str_points:
            arr_str_point = str_point.split()
            S.append(float(arr_str_point[1]))

    def sum_with_scale(array, delta):
        sum = 0
        for i in range(len(array) - 1):
            sum += (array[i] + array[i + 1]) / 2
            i += delta / 5 - 1

        return sum

    def mult_integral(delta, *args):
        mult_fun = []
        for i in range(len(args[0]) - 1):
            el = 1;
            for fun in args:
                if args.index(fun) == 1:
                    el *= (fun[int(i * 5 / delta)] + fun[int(i * 5 / delta) + 1]) / 2
                else:
                    el *= (fun[i] + fun[i + 1]) / 2

            mult_fun.append(el)
            i += delta / 5 - 1
            print(i)

        return sum_with_scale(mult_fun, delta)

    get_plot_from_file()

    # Считываем функции всоприятия цветов реепторами глаза
    x_ = pandas.read_excel("x2_10deg_05.xlsx")
    y_ = pandas.read_excel("y2_10deg_05.xlsx")
    z_ = pandas.read_excel("z2deg_05.xlsx")

    # Выбираем из тапблицы нужную колонку (1) и строки (1:82)
    x_ = x_.iloc[1:82, 1]
    y_ = y_.iloc[1:82, 1]
    z_ = z_.iloc[1:82, 1]

    # Вычисление координат цвета
    precoords = (
    mult_integral(delta, x_.tolist(), S), mult_integral(delta, y_.tolist(), S), mult_integral(delta, z_.tolist(), S))

    s = sum(precoords)

    X = precoords[0] / s
    Y = precoords[1] / s
    Z = precoords[2] / s

    return colour.XYZ_to_xy([X, Y, Z])

name = input("Название >>>")

screen = pygame.display.set_mode((800, 816))

bg = pygame.image.load("cie_img.png")

files = []

instruction = input("Введите название файла со спектром или start (для расчёта) >>> ")

while instruction != "start":
    files.append(instruction)
    instruction = input("Введите название файла со спектром или start (для расчёта) >>> ")

coords = []

n = 1
for spec in files:
    cie_coords = cie_from_spec(spec)
    coords.append([cie_coords[0], cie_coords[1], n, spec])
    n += 1

title = []
for coord in coords:
    title.append(f"{coord[2]} - {coord[3]}")

pygame.init()

screen.blit(bg, (0, 0))

for coord in coords:
    x = coord[0]
    y = coord[1]
    pygame.draw.circle(
        screen,
        (0, 0, 0),
        (OFFSET_X + x*GLOBAL_DELTA_X/LOCAL_DELTA_X, 816 - (OFFSET_Y + y*GLOBAL_DELTA_Y/LOCAL_DELTA_Y)),
        1
    )

    #font = pygame.font.SysFont(None, 24)
    #img = font.render(f'{coord[2]}', True, (0, 0, 0))
    #screen.blit(img, (OFFSET_X + x*GLOBAL_DELTA_X/LOCAL_DELTA_X + 8, 816 - (OFFSET_Y + y*GLOBAL_DELTA_Y/LOCAL_DELTA_Y + 8)))

#dk = 0
#for t in title:
#    font = pygame.font.SysFont(None, 24)
#    img = font.render(f'{t}', True, (0, 0, 0))
#    screen.blit(img, (500 ,60 + dk))
#    dk += 30

pygame.image.save(screen, f"{name}.png")
pygame.quit()