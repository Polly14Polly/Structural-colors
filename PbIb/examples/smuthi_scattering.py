import numpy as np
import smuthi.simulation
import smuthi.initial_field
import smuthi.layers
import smuthi.particles
import smuthi.postprocessing.far_field as ff
import matplotlib.pyplot as plt
import smuthi.utility.automatic_parameter_selection

def make_sphere(radius, refractive_index, offset):
    sphere = [smuthi.particles.Sphere(position=[0, 0, radius+offset],
                                    refractive_index=refractive_index,
                                    radius=radius,
                                    l_max=3,
                                    m_max=3)]
    return sphere

def get_incident_beam(wavelength, angle, polarization):
    plane_wave = smuthi.initial_field.PlaneWave(vacuum_wavelength=wavelength,
                                            polar_angle=angle,  # oblique incidence from top
                                            azimuthal_angle=angle,
                                            polarization=polarization) 
    return plane_wave

radius = 100
wavelength = 500
n1 = 1
n2 = 1
n_sphere = 1.52
n_angles = 720

two_layers = smuthi.layers.LayerSystem(thicknesses=[0, 0],
                                       refractive_indices=[n2, n1])
polar_angles = np.linspace(0, 2*np.pi, n_angles)
azimuthal_angles = np.linspace(0, np.pi, n_angles)

theta_i = np.array([0, 0.1*np.pi, 0.2*np.pi, 0.3*np.pi, 0.4*np.pi, 0.499*np.pi])
single_np = make_sphere(radius, n_sphere, offset=0)

ff_list = []

for angle in theta_i:
    # TE part
    plane_wave = get_incident_beam(wavelength, angle, 0)

    # Initialize and run simulation
    simulation = smuthi.simulation.Simulation(layer_system=two_layers,
                                            particle_list=single_np,
                                            initial_field=plane_wave)
    simulation.run()

    far_fields = ff.scattered_far_field(wavelength, single_np, two_layers, polar_angles=polar_angles, azimuthal_angles=azimuthal_angles)
    integral = far_fields.azimuthal_integral()
    
    ff_TE = integral[0] + integral[1]
    
    ###############
    # TM part
    plane_wave = get_incident_beam(wavelength, angle, 1)

    # Initialize and run simulation
    simulation = smuthi.simulation.Simulation(layer_system=two_layers,
                                            particle_list=single_np,
                                            initial_field=plane_wave)
    simulation.run()

    far_fields = ff.scattered_far_field(wavelength, single_np, two_layers, polar_angles=polar_angles, azimuthal_angles=azimuthal_angles)
    integral = far_fields.azimuthal_integral()
    
    ff_TM = integral[0] + integral[1]

    ff_tot = ff_TE + ff_TM
    norm_scat = ff_tot / np.max(ff_tot)
    ff_list.append(norm_scat)

# Plot it
colors = ['blue', 'orange', 'red', 'green', 'purple', 'brown']
for i in range(len(ff_list)):
    plt.plot(polar_angles/np.pi*180, ff_list[i], 
             label=f'{int(theta_i[i]/np.pi*180)}$\degree$',
             color=colors[i])
    plt.axvline(x=theta_i[i]/np.pi*180, color=colors[i], linestyle='dashed')
plt.legend()
plt.xlabel('Exit Angle (Degrees)')
plt.ylabel('Normalized Farfield Intensity (a.u.)')
plt.show()