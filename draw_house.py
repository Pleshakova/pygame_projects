import pygame
from math import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (50, 100, 255)
green = (50, 150, 50)
yellow = (255, 255, 0)
gray = (200, 200, 200)
dark_red = (150, 50, 0)
dark_green = (0, 100, 0)
brown = (150, 100, 50)
x0 = 0
y0 = 0
size = 800, 600
screen = pygame.display.set_mode(size)
screen.fill(white)


def main():
    horizon(y0 + size[1] // 2, size[0], size[1] // 2)
    draw_sky()
    draw_house(200, 250, 200, 200)
    draw_tree(650, 250, 100, 250)


def horizon(y_horizon, width, height):
    pygame.draw.rect(screen, green, (x0, y_horizon, width, height))
    pygame.draw.rect(screen, blue, (x0, y0, width, height))


def draw_sky():
    # draw sun
    x_sun = x0 + size[0] * 5 // 6
    y_sun = y0 + size[1] * 1 // 6
    r_sun = 40
    draw_sun(x_sun, y_sun, r_sun)
    # draw clouds
    x_clouds = x0 + size[0] // 16
    y_clouds = y0 + size[1] // 6
    r_clouds = 50
    draw_clouds(x_clouds, y_clouds, r_clouds)


def draw_sun(x, y, r):
    pygame.draw.circle(screen, yellow, (x, y), r)


def draw_clouds(x, y, r):
    pygame.draw.ellipse(screen, white, (x, y - 5, r * 3, r * 1.1))
    pygame.draw.circle(screen, white, (x + r, y + r // 4), r // 2)
    pygame.draw.circle(screen, white, (x + 2 * r, y + r // 4), r // 2)
    pygame.draw.circle(screen, white, (x + r, y + 30), r // 2)
    pygame.draw.circle(screen, white, (x + 2 * r, y + 30), r // 2)


def draw_house(x, y, width, height):
    """ Функция рисует дом
    :param x: координата x верхнего угла левой стены
    :param y: координата y верхнего угла левой стены
    :param width: ширина дома
    :param height: высота стены
    """
    walls_width = width
    walls_height = height
    roof_width = width
    roof_height = height // 3 * 2
    window_width = width // 3
    window_height = height // 3
    x_window = x + (width - window_width) // 2
    y_window = y + (height - window_height) // 2
    draw_walls(x, y, walls_width, walls_height)
    draw_roof(x, y, roof_width, roof_height)
    draw_window(x_window, y_window, window_width, window_height)


def draw_walls(x, y, width, height):
    pygame.draw.rect(screen, gray, (x, y, width, height))
    pygame.draw.rect(screen, black, (x, y, width, height), 2)


def draw_roof(x, y, width, height):
    pygame.draw.polygon(screen, dark_red, [(x, y), (x + width, y), (x + width // 2, y - height)])
    pygame.draw.polygon(screen, black, [(x, y), (x + width, y), (x + width // 2, y - height)], 2)


def draw_window(x, y, width, height):
    pygame.draw.rect(screen, yellow, (x, y, width, height))
    pygame.draw.rect(screen, black, (x, y, width, height), 2)
    x1 = x + width // 2
    x2 = x + width
    y1 = y + height // 2
    y2 = y + height
    draw_window_lines(x, y, x1, x2, y1, y2)


def draw_window_lines(x, y, x1, x2, y1, y2):
    pygame.draw.line(screen, black, (x, y1), (x2, y1), 2)
    pygame.draw.line(screen, black, (x1, y), (x1, y2), 2)


def draw_tree(x, y, width, height):
    """ Функция рисует дерево
    :param x: координата x верхушки дерева
    :param y: координата у верхушки дерева
    """
    height_triangle = height // 4
    y_bottom_1triangle = y + height_triangle
    y_top_2triangle = y_bottom_1triangle - height_triangle // 3
    y_bottom_2triangle = y_top_2triangle + height_triangle * 1.3
    y_top_3triangle = y_bottom_2triangle - height_triangle // 3
    y_bottom_3triangle = y_top_3triangle + height_triangle * 1.3 * 1.3
    pygame.draw.rect(screen, brown, (x-5, y_bottom_3triangle, width // 5, height // 5))
    pygame.draw.polygon(screen, dark_green, [(x, y), (x - width // 2, y_bottom_1triangle), (x + width // 2, y_bottom_1triangle)])
    pygame.draw.polygon(screen, dark_green, [(x, y_top_2triangle), (x - width // 3 * 2, y_bottom_2triangle), (x + width // 3 * 2, y_bottom_2triangle)])
    pygame.draw.polygon(screen, dark_green, [(x, y_top_3triangle), (x - width, y_bottom_3triangle), (x + width, y_bottom_3triangle)])


main()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
