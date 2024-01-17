import random
import  pygame

pygame.init()

screen_width = 1000
screen_height = 500

max_radius = 80

spheres = [[0, 0, 0]]

def full_random(num_of_spheres):
    global spheres

    n = num_of_spheres

    while n > 0:
        i = True
        radius = random.randint(10, 40)
        x, y = random.randint(0 + radius, screen_width - radius), random.randint(0 + radius, screen_height - radius)
        for sphere in spheres:
            if (sphere[0] - x)**2 + (sphere[1] - y)**2 < (radius + sphere[2])**2:
                i = False
                break
        if i:
            spheres.append([x, y, radius])
            n -= 1

sc = pygame.display.set_mode((screen_width, screen_height))

full_random(100)
print(spheres)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    sc.fill((0, 0, 0))

    for sph in spheres:
        pygame.draw.circle(sc, (20, 50, 69), (sph[0], sph[1]), sph[2])

    pygame.display.update()