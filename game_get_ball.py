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
    global x, y, r, COLOR, A, B
    A=[randint(50, 600), randint(50, 600), randint(30, 60), colors[randint(0, 5)]]
    B=[randint(50, 600), randint(50, 600), randint(30, 60), colors[randint(0, 5)]]


def new_ball1():
    pygame.draw.circle(screen, A[3], (A[0], A[1]), A[2])


def new_ball2():
    pygame.draw.circle(screen, B[3], (B[0], B[1]), B[2])


def click():
    length1 = ((event.x - A[0]) ** 2 + (event.y - A[1]) ** 2) ** 0.5
    length2 = ((event.x - B[0]) ** 2 + (event.y - B[1]) ** 2) ** 0.5
    if length1 <= A[2] or length2 <=B[2]:
        screen.fill(white)
        pygame.display.update()
        return 1
    return 0

new_parameters()
if A[0] > B[0]:
    C = [A[0],B[0]]
else:
    C = [B[0],A[0]]
while not done:
    while not done and C[0]<700:
        new_ball1()
        new_ball2()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Поймал шариков:", have_balls)
                print("Всего шариков:", all_balls)
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event.x, event.y = event.pos
                have_balls += click()
    #               if click() > 0:
    #                   new_parameters()
    #                   all_balls += 1
        screen.fill(black)
        clock.tick(25)
        A[0] += 10
        B[0] += 10
        C[0]+=10
        C[1]+=10
    while not done and C[1] < 700:
        new_ball1()
        new_ball2()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Поймал шариков:", have_balls)
                print("Всего шариков:", all_balls)
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event.x, event.y = event.pos
                have_balls += click()
        #               if click() > 0:
        #                   new_parameters()
        #                   all_balls += 1
        screen.fill(black)
        clock.tick(25)
        if A[0]==C[0]:
            A[0] -= 10
            B[0] += 10
        else:
            A[0] += 10
            B[0] -= 10
        C[1] += 10
        C[0] -= 10
    while not done and C[0] >50:
        new_ball1()
        new_ball2()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Поймал шариков:", have_balls)
                print("Всего шариков:", all_balls)
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event.x, event.y = event.pos
                have_balls += click()
        #               if click() > 0:
        #                   new_parameters()
        #                   all_balls += 1
        screen.fill(black)
        clock.tick(25)
        if C[0]==A[0]:
            A[0] -= 10
            B[0] -= 10
        else:
            A[0] -= 10
            B[0] -= 10
        C[0]-=10
        C[1]-=10
    while not done and C[1] >50:
        new_ball1()
        new_ball2()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Поймал шариков:", have_balls)
                print("Всего шариков:", all_balls)
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event.x, event.y = event.pos
                have_balls += click()
        #               if click() > 0:
        #                   new_parameters()
        #                   all_balls += 1
        screen.fill(black)
        clock.tick(25)
        if C[0]==A[0]:
            A[0] += 10
            B[0] -= 10
        else:
            A[0] -= 10
            B[0] += 10
        C[1]-=10
        C[0]+=10
pygame.quit()
