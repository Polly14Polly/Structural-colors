import random
import time
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
        reading_wl = reading.split("\n")[1]
        reading_n = reading.split("\n")[2]  # попилил строки(костыль), получил в строке два нужных массива

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



def const_r_rect_net(size_x, size_y, a, b, r):
    Na = size_x // a
    Nb = size_y // b

    arr = []  # относительные координаты сфер
    for i in range(Na):
        arr.append([])
        for j in range(Nb):
            arr[i].append([])

            x = random.randint(r + 1, a - r - 1)
            y = random.randint(r + 1, b - r - 1)
            arr[i][j].append(x)
            arr[i][j].append(y)
            arr[i][j].append(r)
    # p(arr)
    # каждая ячейка массива Na*Nb содержит в себе массив - пару чисел (координаты центра ОТНОСИТЕЛЬНО ЛЕВОГО НИЖНЕГО УГЛА) и радиус

    arr1 = arr  # абсолютные координаты
    for i in range(Na):
        for j in range(Nb):
            arr1[i][j][0] = arr[i][j][0] + a * i
            arr1[i][j][1] = arr[i][j][1] + b * j
    sprs = open('SpheresList1.txt', 'a')
    for i in range(Na):
        for j in range(Nb):
            sprs.write(str(arr1[i][j][0]) + ";" + str(arr1[i][j][1]) + ";" + str(arr1[i][j][2]) + ";" + "0\n")
    sprs.close()



def Spectrum(materials, leftGran, rightGran, shag):


    bI = []  # массив с рассеянием
    for i in range(leftGran, rightGran, shag):  # фором пробегаюсь по всем длинам волн (i - длина волны в нм)
        sps = open('SpheresList1.txt', 'r')
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
                                                  solver_type='gmres',
                                                  solver_tolerance=1e-5,
                                                  initial_field=plane_wave)

        simulation.run()


        scs = ff.total_scattering_cross_section(initial_field=plane_wave,  # evaluate the scattering cross section
                                                particle_list=spheres,
                                                layer_system=two_layers)
        scs = scs / 1e6


        print(i)  # просто вывод, чтоб следить за процессом
        print(scs)
        bI.append(scs)
        sps.close()
    return bI

'''def convert_PS_to_PNG(infile, outfile):

    path_infile = dataDir + infile

    options = PsLoadOptions()
    options.SupressErrors = True
    # Open .ps document with created load options
    document = Document(path_infile, options)

    # Create Resolution object

    resolution = Resolution(300)

    device = PngDevice(resolution)

    pageCount = 1

    while pageCount <= document.Pages.Count:
        imageStream = FileStream(self.dataDir + outfile + str(pageCount) + "_out.png", FileMode.Create)

        # Convert a particular page and save the image to stream

        device.Process(document.Pages[pageCount], imageStream)

        # Close stream

        imageStream.Close()
        pageCount = pageCount + 1

    print(infile + " converted into " + outfile)'''












f = open('command.txt', 'r')  # зачитал файл

s = open('SpheresList1.txt', 'w') #почистил массив(текстовый файл) сфер
s.truncate()
s.close()
s2 = open('output.txt', 'w')  #почистил вывод
s2.truncate()
s2.close()




countSim = 1;
countDraw = 1;
work = 1
materials = []
veryNachalo = time.time()
while (work == 1):
    cmd = f.readline();  # прочитал строку
    cmd = cmd.replace("\n", "")
    cmds = cmd.split(";")
    i = 1
    while (i == 1):

        if (cmds[0] == ""):  # конец программы
            work = 0
            break


        if (cmds[0] == "SimulateSpectrum"):                                         #симуляция. Вызывается так: от длины волны до длины волны с шагом
            begin = time.time()
            y = Spectrum(materials, int(cmds[1]), int(cmds[2]), int(cmds[3]))

            x = []
            for i in range(int(cmds[1]), int(cmds[2]), int(cmds[3])):  # массив иксов, чтоб график построить
                x.append(i)

            G.plot(x, y)  # строю графек
            if (len(cmds) > 4):
                if(cmds[4] == "save"):
                    G.savefig(str(countSim) + "section.png")
                    out = open('output.txt', 'a')
                    vrem = time.time() - begin
                    out.write("\n" + str(countSim) + ") Proshlo " + str(vrem) + " secund\n")
                    out.close()
                    countSim = countSim + 1
                else:
                    G.show()
            else:
                G.show()
            G.close()
            break

        if (cmds[0] == "OneSphere"):                                                #добавление сферы
            sprs = open('SpheresList1.txt', 'a')  # записал сферки
            sprs.write(cmds[1] + ";" + cmds[2] + ";" + cmds[3] + ";" + cmds[4]+"\n")     #сфера добавляется так: x;y;r;номер материала
            sprs.close()
            break

        if (cmds[0] == "AddMaterial"):                                              #придётся запоминать номера...
            materials.append(material(cmds[1]))
            break

        if (cmds[0] == "Draw"):
            window = Tk()
            c = Canvas(window, width=1920, height=1080)  # Холст 1000
            c.pack()
            sps = open('SpheresList1.txt', 'r')
            line = sps.readline()
            while (line != ""):
                c.create_oval(int(line.split(";")[0])/20-int(line.split(";")[2])/20, int(line.split(";")[1])/20-int(line.split(";")[2])/20, int(line.split(";")[0])/20+int(line.split(";")[2])/20, int(line.split(";")[1])/20+int(line.split(";")[2])/20, fill="red")
                line = sps.readline()
            sps.close()
            if(len(cmds) > 1):
                if(cmds[1] == "save"):
                    window.update()                                                                 # pip install aspose-pdf
                    c.postscript(file=str(countDraw) + "udoli.ps", colormode='color')               #костыль - https://products.aspose.com/pdf/ru/python-net/conversion/ps-to-png/
                    countDraw = countDraw + 1
                else:
                    window.mainloop()
            else:
                window.mainloop()
            break

        if (cmds[0] == "RectNet"):                                              #придётся запоминать номера...
            const_r_rect_net(int(cmds[1]),int(cmds[2]),int(cmds[3]),int(cmds[4]),int(cmds[5]))
            break

        if (cmds[0] == "Clear"):  # придётся запоминать номера...
            ssss = open('SpheresList1.txt', 'w')
            ssss.truncate()
            ssss.close()
            break

        print("Something is creating script ERRORs")
        i = 0  # почему нет switch case пришлось костылить...

out = open('output.txt', 'a')
out.write("\n Vsego proshlo " +str(time.time() - veryNachalo))
out.close()
