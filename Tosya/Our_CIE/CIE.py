import pygame
from settings import *

def cie_from_spec(file):
    pass

name = input("Название >>>")

screen = pygame.display.set_mode((800, 816))

bg = pygame.image.load("cie_img.png")

files = []

instruction = input("Введите название файла со спектром или start (для расчёта) >>> ")

while instruction != "exit":
    files.append(instruction)
    instruction = input("Введите название файла со спектром или start (для расчёта) >>> ")

coords = []

n = 1
for spec in files:
    cie_coords = cie_from_spec(spec)
    coords.append([cie_coords[0], cie_coords[1], n, spec])

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
        3
    )

    font = pygame.font.SysFont(None, 24)
    img = font.render(f'{coord[2]}', True, (0, 0, 0))
    screen.blit(img, (OFFSET_X + x*GLOBAL_DELTA_X/LOCAL_DELTA_X + 8, 816 - (OFFSET_Y + y*GLOBAL_DELTA_Y/LOCAL_DELTA_Y + 8)))

dk = 0
for t in title:
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'{t}', True, (255, 255, 255))
    screen.blit(img, (500 ,60 + dk))
    dk += 30

pygame.image.save(screen, f"results/{name}.png")
pygame.quit()