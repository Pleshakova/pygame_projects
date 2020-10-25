import pygame
from random import *
import lib_ball_game as lib
pygame.init()

n = 10

pygame.display.update()
clock = pygame.time.Clock()
done = False


class Ball:
    def __init__(self, x, y, r, color, direction):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
        self.direction=direction

    def draw(self):
        pygame.draw.circle(lib.screen,self.color,(self.x,self.y),self.r)

    def move(self):
        if self.direction == 1:
            self.x += 10
            if self.x + self.r >= 800:
                self.direction = randint(1, 2)

        if self.direction == 2:
            self.x -= 10
            if self.x - self.r <= 0:
                self.direction = randint(1, 2)

    def coord(self, x, y):
        if y == 0:
            return self.x
        if x == 0:
            return self.y


list_ball = [0]*n
for i in range(n):
    x = randint(50, 700)
    y = randint(50, 550)
    r = randint(40,50)
    color = lib.colors[randint(0,5)]
    direction = randint(1, 2)
    list_ball[i] = Ball(x, y, r, color, direction)
while not done:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event.x, event.y = event.pos
            for i in range(len(list_ball)):
                length = ((event.x - list_ball[i].coord(x, 0))**2 + (event.y - list_ball[i].coord(0, y))**2)**0.5
                if length <= r:
                    print('You got a ball')
                    list_ball.pop(i)
                    x = randint(50, 700)
                    y = randint(50, 550)
                    r = randint(40, 50)
                    color = lib.colors[randint(0, 5)]
                    direction = randint(1, 2)
                    list_ball.insert(i,Ball(x, y, r, color, direction))
    for i in range(len(list_ball)):
        list_ball[i].draw()
    pygame.display.update()
    lib.screen.fill(lib.black)
    for i in range(len(list_ball)):
        list_ball[i].move()

pygame.quit()