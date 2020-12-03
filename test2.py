import pygame
from random import randint

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
color = (randint(0, 255), randint(0, 255), randint(0, 255))  # FIXME цвет не должен сливаться с экраном
BLACK = (0, 0, 0)


class Target:
    target_field_width = width
    target_field_height = height // 3

    def __init__(self):
        self.width = 100
        self.height = 50
        self.coord = [400, 200]
        self.r = 50

    def set_coord(self):
        self.coord = []
        self.coord.append(randint(0, self.target_field_width - self.width))
        self.coord.append(randint(0, self.target_field_height - self.height))
        return self.coord

    def show(self):
        pygame.draw.circle(screen, color, self.coord, self.r)

    def fire(self):
        bomb = Bomb()
        bomb.Vy = 10
        return bomb


class Bomb(Target):
    def __init__(self):
        super().__init__()
        self.radius = 20
        self.Vy = 0

    def show(self):
        pygame.draw.circle(screen, [100, 100, 100], self.coord, self.radius)

    def move(self):
        self.coord[1] += self.Vy


def main():
    finished = False
    pygame.init()
    time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    target = Target()
    bomb = target.fire()
    while not finished:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        if pygame.time.get_ticks() >= time + 1000:
            time = pygame.time.get_ticks()
            bomb = target.fire()
        target.show()
        bomb.show()
        bomb.move()
        pygame.display.flip()
        screen.fill(BLACK)


if __name__ == "__main__":
    main()

