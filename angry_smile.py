import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((400, 400))

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
x = 200
y = 200
r = 100
clock = pygame.time.Clock()
pygame.display.update()
done = False

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(GRAY)
    # draw a head
    pygame.draw.circle(screen, YELLOW, (x, y), r)
    pygame.draw.circle(screen, BLACK, (x, y), r, 1)
    # draw eyes
    circle(screen, RED, (x - r // 2, y - r // 3), r // 4)
    circle(screen, BLACK, (x - r // 2, y - r // 3), r // 4, 1)
    circle(screen, BLACK, (x - r // 2, y - r // 3), r // 10)
    circle(screen, RED, (x + r // 2, y - r // 3), r // 5)
    circle(screen, BLACK, (x + r // 2, y - r // 3), r // 5, 1)
    circle(screen, BLACK, (x + r // 2, y - r // 3), r // 10)
    # draw eyebrows
    line(screen, BLACK, (x - r // 6 * 5, y - r // 6 * 5), (x - r // 6, y - r // 2), 10)
    line(screen, BLACK, (x + r, y - r // 5 * 3), (x + r // 6, y - r // 2), 10)
    # draw a mouth
    rect(screen,BLACK,(x-50,y+40,100,20))

    pygame.display.flip()
pygame.quit()