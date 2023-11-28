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
    max_x = max_coord(structures_array, 0)
    max_y = max_coord(structures_array, 1)

    sc_settings = (800, 800/(max_x*max_radius + max_radius)*(max_y*max_radius + max_radius))

    screen = pygame.display.set_mode(sc_settings)

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
            pygame.draw.circle(screen, (255, 255, 255), (partical[0] + sc_settings[0]/2, partical
                                                         [1] + sc_settings[1]/2), partical[2])

        pygame.display.update()

#функция поиска максимального радиуса
def max_rad(arr):
    radiuses = []
    for element in arr:
        radiuses.append(element[2])
    return max(radiuses)

def max_coord(arr, ind):
    coords = []
    for element in arr:
        coords.append(abs(element[ind]))

    return max(coords)