import smuthi.simulation
import smuthi.initial_field
import smuthi.layers
import smuthi.particles
import smuthi.postprocessing.far_field as ff
import matplotlib.pyplot as G
import numpy as np
import smuthi.simulation
import smuthi.initial_field
import smuthi.layers
import smuthi.particles
import smuthi.postprocessing.far_field
import smuthi.postprocessing.graphical_output
import smuthi.utility.automatic_parameter_selection
from tkinter import *




class material:
    def __init__(self, name):
        self.name = name

        f = open('material.txt', 'r')  # зачитал файл
        reading = f.read()
        reading = reading.split(name)[1]
        reading_wl = reading.split("\n")[0]
        reading_n = reading.split("\n")[1]  # попилил строки(костыль), получил в строке два нужных массива

        data_n_wl = []  #создал два массива
        data_n = []

        for symbol1 in reading_wl.split(","):  # два массива data_n_wl с длинами волн и data_n с значениями коэффициента преломления
            data_n_wl.append(float(symbol1))  # в этом куске кода я заполняю эти массивы, читая reading
        for symbol2 in reading_n.split(","):
            data_n.append(float(symbol2))

        self.n = data_n
        self.wl = data_n_wl
        self.length = len(data_n)










def search_wl(left, right, A, B, key):  # бинарный поиск с усреднением относительно соседних
    if right > left + 1:
        middle = int((left + right) / 2)
        if (A[middle] == key):
            return B[middle]
        if A[middle] > key:
            return search_wl(left, middle, A, B, key)
        else:
            return search_wl(middle, right, A, B, key)
    else:
        return (key - A[left]) / (A[right] - A[left]) * (B[right] - B[left]) + B[left]








def Spectrum(materials, leftGran, rightGran, shag):
    sps = open('SpheresList1.txt', 'r')


    bI = []  # массив с рассеянием
    for i in range(leftGran, rightGran, shag):  # фором пробегаюсь по всем длинам волн (i - длина волны в нм)
        ns = []
        for mat in materials:
            ns.append(search_wl(0, mat.length, mat.wl, mat.n, i / 1000))

        two_layers = smuthi.layers.LayerSystem(thicknesses=[0, 0],  # просто стандартные два полупространства
                                               refractive_indices=[1.52, 1])




        spheres = []  # наделал сферок(чтоб каждая расчитывалась в зависимости от длины волны)
        line = sps.readline()
        while(line != ""):
            spheres.append(
                smuthi.particles.Sphere(position=[int(line.split(";")[0]), int(line.split(";")[1]), int(line.split(";")[2])],
                                        refractive_index=ns[int(line.split(";")[3])],
                                        radius=int(line.split(";")[2]),
                                        l_max=3)
            )
            line = sps.readline()




        plane_wave = smuthi.initial_field.PlaneWave(vacuum_wavelength=i,  # насветил, i - это длина волны
                                                    polar_angle=np.pi,
                                                    azimuthal_angle=0,
                                                    polarization=0)

        simulation = smuthi.simulation.Simulation(layer_system=two_layers,
                                                  particle_list=spheres,
                                                  initial_field=plane_wave)

        simulation.run()


        scs = ff.total_scattering_cross_section(initial_field=plane_wave,  # evaluate the scattering cross section
                                                particle_list=spheres,
                                                layer_system=two_layers)
        scs = scs / 1e6


        print(i)  # просто вывод, чтоб следить за процессом
        print(scs)
        bI.append(scs)
    return bI






















f = open('command.txt', 'r')  # зачитал файл
work = 1
materials = []
while (work == 1):
    cmd = f.readline();  # прочитал строку
    cmds = cmd.split(";")
    i = 1
    while (i == 1):

        if (cmds[0] == ""):  # конец программы
            work = 0
            break


        if (cmds[0] == "SimulateSpectrum"):                                         #симуляция. Вызывается так: от длины волны до длины волны с шагом
            y = Spectrum(materials, int(cmds[1]), int(cmds[2]), int(cmds[3]))

            x = []
            for i in range(int(cmds[1]), int(cmds[2]), int(cmds[3])):  # массив иксов, чтоб график построить
                x.append(i)

            G.plot(x, y)  # строю графек
            G.show()
            break

        if (cmds[0] == "OneSphere"):                                                #добавление сферы
            sprs = open('SpheresList1.txt', 'a')  # записал сферки
            sprs.write(cmds[1] + ";" + cmds[2] + ";" + cmds[3] + ";" + cmds[4])     #сфера добавляется так: x;y;r;номер материала
            sprs.close()
            break

        if (cmds[0] == "AddMaterial"):                                              #придётся запоминать номера...
            materials.append(material(cmds[1]))
            break

        if (cmds[0] == "Draw"):
            window = Tk()
            c = Canvas(window, width=1000, height=1000)  # Холст 1000
            c.pack()
            c.create_oval(100, 100, 500, 500)
            window.mainloop()
            break

        print("Something is creating script ERRORs")
        i = 0  # почему нет switch case пришлось костылить...