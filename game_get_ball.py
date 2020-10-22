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
n = 3

pygame.display.update()
clock = pygame.time.Clock()
done = False
all_balls = 0
have_balls = 0


def new_parameters(n):
    global X, Y, R, COLOR
    X = [randint(50, 600) for i in range(n)]
    Y = [randint(50, 600) for i in range(n)]
    R = [randint(30, 60) for i in range(n)]
    COLOR = [colors[randint(0, 5)] for i in range(n)]


def initial_sorted_X():
    N = len(X)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if X[j] > X[i]:
                X[j], X[i] = X[i], X[j]


def initial_sorted_A(n):
    global A, T
    A = []
    for i in range(n):
        T = [X[i], Y[i], R[i], COLOR[i]]
        A.append(T)


def new_ball():
    for T in A:
        T[0], T[1], T[2], T[3] = T
        for i in range(len(T)):
            pygame.draw.circle(screen, T[3], (T[0], T[1]), T[2])


def new_sorted_A1():
    i = 0
    if Opt[0] == 1:
        for T in A:
            T[0], T[1], T[2], T[3] = T
            T[0] += 10
    elif Opt[1] == 1:
        for T in A:
            T[0], T[1], T[2], T[3] = T
            if i == 0:
                T[0] -= 10
            else:
                T[0] += 10
            i += 1
    elif Opt[2] == 1:
        for T in A:
            T[0], T[1], T[2], T[3] = T
            if i == 0 or i == 1:
                T[0] -= 10
            else:
                T[0] += 10
            i += 1


def new_sorted_A2():
    i = 0
    if Opt2[0] == 1:
        for T in A:
            T[0], T[1], T[2], T[3] = T
            T[0] -= 10
    elif Opt2[1] == 1:
        for T in A:
            T[0], T[1], T[2], T[3] = T
            if i == 0:
                T[0] += 10
            else:
                T[0] -= 10
            i += 1
    elif Opt2[2] == 1:
        for T in A:
            T[0], T[1], T[2], T[3] = T
            if i == 0 or i == 1:
                T[0] += 10
            else:
                T[0] -= 10
            i += 1


def adjusted_X1():
    if Opt[0] == 1:
        for i in range(len(X)):
            X[i] += 10
    elif Opt[1] == 1:
        for i in range(len(X)):
            if i == 0:
                X[i] -= 10
            else:
                X[i] += 10
    elif Opt[2] == 1:
        for i in range(len(X)):
            if i == 0 or i == 1:
                X[i] -= 10
            else:
                X[i] += 10


def adjusted_X2():
    if Opt2[0] == 1:
        for i in range(len(X)):
            X[i] -= 10
    elif Opt2[1] == 1:
        for i in range(len(X)):
            if i == 0:
                X[i] += 10
            else:
                X[i] -= 10
    elif Opt2[2] == 1:
        for i in range(len(X)):
            if i == 0 or i == 1:
                X[i] += 10
            else:
                X[i] -= 10


def options1(n):
    global Opt
    Opt = [0] * len(A)
    Opt[n] = 1


def options2(n):
    global Opt2
    Opt2 = [0] * len(A)
    Opt2[n] = 1


new_parameters(n)
initial_sorted_X()
initial_sorted_A(n)
"""        
def click(n):
    length1 = ((event.x - A[0]) ** 2 + (event.y - A[1]) ** 2) ** 0.5
    length2 = ((event.x - B[0]) ** 2 + (event.y - B[1]) ** 2) ** 0.5
    if length1 <= A[2] or length2 <=B[2]:
        screen.fill(white)
        pygame.display.update()
        return 1
    return 0
"""
while not done:
    for i in range(n):
        while not done and X[i] < 700:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Поймал шариков:", have_balls)
                    print("Всего шариков:", all_balls)
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    event.x, event.y = event.pos
        #            have_balls += click()
        #               if click() > 0:
        #                   new_parameters()
        #                   all_balls += 1
            new_ball()
            pygame.display.update()
            screen.fill(black)
            options1(i)
            new_sorted_A1()
            adjusted_X1()
    for i in range(n):
        while not done and X[i] > 50:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Поймал шариков:", have_balls)
                    print("Всего шариков:", all_balls)
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    event.x, event.y = event.pos
            #        have_balls += click()
            #               if click() > 0:
            #                   new_parameters()
            #                   all_balls += 1
            options2(i)
            new_sorted_A2()
            new_ball()
            pygame.display.update()
            screen.fill(black)
            adjusted_X2()

pygame.quit()
