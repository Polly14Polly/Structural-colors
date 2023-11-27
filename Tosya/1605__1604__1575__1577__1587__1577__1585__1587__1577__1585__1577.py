#*****************************************************************************#
# This is a simple example script for Smuthi v1.0.0                           #
# It evaluates the electric near field for three spheres in a waveguide       #
# excited by a plane wave under oblique incidence                             #
#*****************************************************************************#

import numpy as np
import smuthi.simulation
import smuthi.initial_field
import smuthi.layers
import smuthi.particles
import smuthi.postprocessing.graphical_output as go
import smuthi.utility.cuda

# try to enable GPU calculations
smuthi.utility.cuda.enable_gpu()

# In this file, all lengths are given in nanometers

# Initialize the layer system object containing
# - a substrate (glass)
# - a titania layer
# - the ambient (air)
# The coordinate system is such that the interface
# between the first two layers defines the plane z=0.
# Note that semi infinite layers have thickness 0!
three_layers = smuthi.layers.LayerSystem(thicknesses=[0, 500, 0],
                                         refractive_indices=[1.52, 1.75, 1])

# Scattering particles, immersed in the titania layer
class Sphere:
    def __init__(self, position, refractive_index, radius, l_max):
        self.pos = position
        self.refInd = refractive_index
        self.rad = radius
        self.l_max = l_max


    def create_sphere(self):
        return smuthi.particles.Sphere(self.pos, self.refInd, self.rad - 0.1, self.l_max)

class SphereStructure:
    def __init__(self, geom, refractive_index, radius, l_max):
        self.sphere_list = []
        length_x = geom[0]*radius*2
        length_y = geom[1]*radius*2

        left_top_point = (length_x/2, length_y/2)
        for x_sph in range(geom[0]):
            for y_sph in range(geom[1]):
                self.sphere_list.append(Sphere([left_top_point[0] - radius - x_sph*radius, left_top_point[1] - radius - y_sph*radius, 50], refractive_index, radius-0.1, l_max).create_sphere())


"""
sphere1 = smuthi.particles.Sphere(position=[-200, 0, 250],
                                  refractive_index=1.52,    # glass sphere
                                  radius=100,
                                  l_max=3)

sphere2 = smuthi.particles.Sphere(position=[0, 0, 250],
                                  refractive_index=1,       # air bubble
                                  radius=50,
                                  l_max=3)

sphere3 = smuthi.particles.Sphere(position=[200, 0, 250],
                                  refractive_index=1+6j,    # metal sphere
                                  radius=80,
                                  l_max=4)"""


# List of all scattering particles
three_spheres = SphereStructure([100, 100], refractive_index=1, radius=50, l_max=3).sphere_list

# Initial field
plane_wave = smuthi.initial_field.PlaneWave(vacuum_wavelength=550,
                                            polar_angle= 4*np.pi/5, # from top
                                            azimuthal_angle=0,
                                            polarization=0)         # 0=TE 1=TM

# Initialize and run simulation
simulation = smuthi.simulation.Simulation(layer_system=three_layers,
                                          particle_list=three_spheres,
                                          initial_field=plane_wave,
                                          length_unit='nm')
simulation.run()

# Create plots that visualize the electric near field.

go.show_near_field(quantities_to_plot=['norm(E)', 'E_y'],
                   show_plots=True,
                   show_opts=[{'label':'raw_data'},
                              {'interpolation':'quadric'},
                              {'interpolation':'quadric'}],
                   save_plots=True,
                   save_opts=[{'format':'png'},
                              {'format':'pdf','dpi':200},
                              {'format':'gif'}], # animated gif of E_y
                   outputdir='./output',
                   xmin=-600,
                   xmax=600,
                   zmin=-100,
                   zmax=900,
                   resolution_step=20,
                   simulation=simulation,
                   show_internal_field=True)


# If you want to plot data with a logarithmic colorbar, use the 'norm' key of the
# show_opts dictionary to pass e.g., a LogNorm() or a SymLogNorm(). For example:

# from matplotlib import colors
#
# colorlog = colors.SymLogNorm(base=10, linthresh=3, linscale=2, vmin=-1000, vmax=1000)
# go.show_near_field(simulation=simulation,
#                    quantities_to_plot=["E_z"],
#                    show_opts=[{'label': 'raw_log', 'norm': colorlog},
#                               {'label': 'raw', 'vmax': 1e2}]
#                    ... )
