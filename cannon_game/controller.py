import pygame
import model as mod

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event.x, event.y = event.pos
            other_x, other_y = event.x, event.y
            # call game_manager
        elif event.type == pygame.KEYDOWN:
            pass