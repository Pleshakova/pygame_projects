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
x0 = 0
y0 = 0
size = 800, 600
screen = pygame.display.set_mode(size)
screen.fill(white)


def main():
    horizon(size, y0)
    draw_sky(size, 40)
    draw_house(200, 250, 200, 200)
    draw_tree(650, 250, 100, 250)


def horizon(size, y0):
    width1 = size[0]
    heigth1 = size[1] // 2
    y1 = y0 + heigth1
    pygame.draw.rect(screen, green, (x0, y1, width1, heigth1))
    pygame.draw.rect(screen, blue, (x0, y0, width1, heigth1))


def draw_sky(size, r):
    x = x0 + size[0] * 5 // 6
    y = y0 + size[1] * 1 // 6
    # draw the sun
    draw_sun(x, y, r)
    # draw clouds
    x = x0 + size[0] // 16
    y = y0 + size[1] // 6
    draw_clouds(x, y, r + 10)


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
    draw_walls(200, 250, 200, 200)
    draw_roof(200, 250, 200, 200)
    draw_window(200, 250, 200, 200)


def draw_walls(x, y, width, height):
    pygame.draw.rect(screen, gray, (x, y, width, height))
    pygame.draw.rect(screen, black, (x, y, width, height), 2)


def draw_roof(x, y, width, height):
    x1 = x + width
    x2 = x + width // 2
    y2 = y - height // 3 * 2
    pygame.draw.polygon(screen, dark_red, [(x, y), (x1, y), (x2, y2)])
    pygame.draw.polygon(screen, black, [(x, y), (x1, y), (x2, y2)], 2)


def draw_window(x, y, width, height):
    width1 = width // 3
    height1 = height // 3
    x1 = x + (width - width1) // 2
    y1 = y + (height - height1) // 2
    x2 = x1 + width1 // 2
    x3 = x1 + width1
    y2 = y1 + height1
    y3 = y1 + height1 // 2
    pygame.draw.rect(screen, yellow, (x1, y1, width1, height1))
    pygame.draw.rect(screen, black, (x1, y1, width1, height1), 2)
    pygame.draw.line(screen, black, (x2, y1), (x2, y2), 2)
    pygame.draw.line(screen, black, (x1, y3), (x3, y3), 2)


def draw_tree(x, y, width, height):
    pygame.draw.rect(screen, red, (x, y, width // 10, height))


main()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
