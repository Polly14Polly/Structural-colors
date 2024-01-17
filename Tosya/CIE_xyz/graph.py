import matplotlib.pyplot

j = []
S = []


file = open(f"{input('Введите названиие файла >>> ')}", "r")
str_points = file.readlines()
points = []
for str_point in str_points:
    arr_str_point = str_point.split()
    S.append(float(arr_str_point[1]))
points = []
for str_point in str_points:
    arr_str_point = str_point.split()
    j.append(float(arr_str_point[0]))

matplotlib.pyplot.plot(j, S)
matplotlib.pyplot.show()