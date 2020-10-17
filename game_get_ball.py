import pygame
from random import *
pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [yellow, cyan, magenta, red, green, blue]

pygame.display.update()
clock = pygame.time.Clock()
done = False
all_balls = 0
have_balls = 0


def new_parameters():
    global x, y, r, COLOR
    x = randint(50, 600)
    y = randint(50, 500)
    r = randint(30, 60)
    COLOR = colors[randint(0, 5)]


def parameter_x():
    return x


def new_ball():
    for i in range(3):
        pygame.draw.circle(screen, COLOR, (x, y), r)


def click():
    length = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
    if length <= r:
        screen.fill(white)
        pygame.display.update()
        return 1
    return 0


new_parameters()
all_balls += 1
while not done:
    while not done and x + r < 800:
        new_ball()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Поймал шариков:", have_balls)
                print("Всего шариков:", all_balls)
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event.x, event.y = event.pos
                have_balls += click()
                if click() > 0:
                    new_parameters()
                    all_balls += 1
        screen.fill(black)
        clock.tick(25)
        x+=10
    while not done and x - r > 0:
        new_ball()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Поймал шариков:", have_balls)
                print("Всего шариков:", all_balls)
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event.x, event.y = event.pos
                have_balls += click()
                if click() > 0:
                    new_parameters()
                    all_balls += 1
        screen.fill(black)
        clock.tick(25)
        x -= 10

pygame.quit()
