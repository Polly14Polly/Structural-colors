from DrawStructure import draw

class Sphere:
    def __init__(self, position, refractive_index, radius, l_max):
        self.pos = position
        self.refInd = refractive_index
        self.rad = radius
        self.l_max = l_max


    def create_sphere(self):
        return [self.pos[0], self.pos[1], self.rad]

class SphereStructure:
    def __init__(self, geom, refractive_index, radius, l_max):
        self.sphere_list = []
        length_x = geom[0]*radius*2
        length_y = geom[1]*radius*2

        left_top_point = (length_x/2, length_y/2)
        for x_sph in range(geom[0]):
            for y_sph in range(geom[1]):
                self.sphere_list.append(Sphere([left_top_point[0] - radius - x_sph*radius, left_top_point[1] - radius - y_sph*radius, 50], refractive_index, radius-0.1, l_max).create_sphere())

draw(SphereStructure([100, 100], refractive_index=1, radius=50, l_max=3).sphere_list)