import pygame
from settings import *

name = input("Название >>>")

pygame.init()

screen = pygame.display.set_mode((800, 816))

bg = pygame.image.load("cie_img.jpg")

coords = [
    [0.32, 0.5],
    [0.12, 0.21],
    [0.3, 0.4]
]

loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            pygame.image.save(screen, f"results/{name}.png")
            pygame.quit()

    screen.blit(bg, (0, 0))

    for coord in coords:
        x = coord[0]
        y = coord[1]
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (OFFSET_X + x*GLOBAL_DELTA_X/LOCAL_DELTA_X, 816 - (OFFSET_Y + y*GLOBAL_DELTA_Y/LOCAL_DELTA_Y)),
            3
        )

    pygame.display.update()