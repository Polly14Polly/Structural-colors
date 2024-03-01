import numpy
    def get_ref_index(wave, material):
        dependencies = {
            "SiO2": "SiO2_Gao.txt",
            "Si": "Si_Vuye_20C.txt"
        }
        file = open(dependencies[material], "r")
        lines = file.readlines()
        n_array = []
        for line in lines:
            while line[0] == " ":
                line = line[1:]
            n_array.append(line.split(" "))

        wave_ind = 0
        while float(n_array[wave_ind][0])*1000 < wave:
            wave_ind += 1
        wave_btw = [wave_ind - 1, wave_ind]
        delta_wave_1 = wave - float(n_array[wave_btw[0]][0])*1000
        delta_wave_2 = float(n_array[wave_btw[1]][0])*1000 - wave
        if delta_wave_2 == 0:
            return float(n_array[wave_btw[1]][1]) + float(n_array[wave_btw[1]][2])*1j
        if delta_wave_1 == 0:
            return float(n_array[wave_btw[0]][1]) + float(n_array[wave_btw[0]][2])*1j
        else:
            scale = delta_wave_1/(delta_wave_2+delta_wave_1)
            delta_1 = abs(float(n_array[wave_btw[1]][1]) - float(n_array[wave_btw[0]][1]))
            delta_2 = abs(float(n_array[wave_btw[1]][2]) - float(n_array[wave_btw[0]][2]))
            return ((abs(float(n_array[wave_btw[0]][1])) + abs(delta_1*scale)) +
                    (abs(float(n_array[wave_btw[0]][2])) + abs(delta_2*scale))*1j)

    def smuthi_calculation_with_some_angles(spheres):
        spectrum_with_some_angles = []

        for angle in [np.pi, np.pi*5/6, np.pi*2/3]:
            waves = []
            scss = []

            for wave in range(380, 800, 20):
                spheres_for_smuthi = []

                sphere_ref_ind = get_ref_index(wave, "Si")
                layer_ref_ind = get_ref_index(wave, "SiO2")
                for sphere in spheres:
                    print([sphere[0] * 100, sphere[1] * 100, sphere[2] * 100])
                    spheres_for_smuthi.append(
                        smuthi.particles.Sphere(
                            position=[sphere[0] * 100, sphere[1] * 100, sphere[2] * 100],
                            refractive_index=sphere_ref_ind,
                            radius=sphere[2] * 100,
                            l_max=3
                        )
                    )

                layers = smuthi.layers.LayerSystem(thicknesses=[0, 0], refractive_indices=[layer_ref_ind, 1])

                plane_wave = smuthi.initial_field.PlaneWave(
                    vacuum_wavelength=wave,
                    polar_angle=angle,
                    azimuthal_angle=0,
                    polarization=0
                )

                simulation = smuthi.simulation.Simulation(
                    layer_system=layers,
                    particle_list=spheres_for_smuthi,
                    solver_type='gmres',
                    solver_tolerance=1e-7,
                    initial_field=plane_wave
                )

                simulation.run()

                scs = ff.total_scattering_cross_section(
                    initial_field=plane_wave,
                    particle_list=spheres_for_smuthi,
                    layer_system=layers
                )

                norm = r_screen_width*r_screen_height*10000

                scs = scs / norm

                waves.append(wave)
                scss.append(scs)

            matplotlib.pyplot.plot(waves, scss, label=f"{name} angle={int(180*angle/np.pi)}")
