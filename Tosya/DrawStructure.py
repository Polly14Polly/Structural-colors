import pygame

# инициализируем библиотеку Pygame
pygame.init()

# задаем название окна
pygame.display.set_caption("Отрисовка структуры")

# создаем окно
screen = pygame.display.set_mode((1000, 600))

#функция отрисовки структуры
def draw(structures_array):
    max_radius = max_rad(structures_array)
    max_coordinate = max_coord(structures_array)

    scale = 600/(max_radius + max_coordinate)

    # задаем цвет фона
    background_color = (0, 0, 0)  # синий

    # заполняем фон заданным цветом
    screen.fill(background_color)

    # обновляем экран для отображения изменений
    pygame.display.flip()

    # показываем окно, пока пользователь не нажмет кнопку "Закрыть"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for partical in structures_array:
            pygame.draw.circle(screen, (255, 255, 255), (partical[0]*scale, partical
                                                         [1]*scale), partical[2]*scale)

        pygame.display.update()

#функция поиска максимального радиуса
def max_rad(arr):
    radiuses = []
    for element in arr:
        radiuses.append(element[2])
    return max(radiuses)

def max_coord(arr):
    coords = []
    for element in arr:
        coords.append(element[0])
        coords.append(element[1])

    return max(coords)