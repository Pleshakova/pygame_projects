import pygame
from random import randint
import math

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
color = (randint(0, 255), randint(0, 255), randint(0, 255))  # FIXME цвет не должен сливаться с экраном
BLACK = (0, 0, 0)


class Cannon:
    standart_radius = 40
    health = 3

    def __init__(self):
        self.x = 200
        self.y = 600
        self.is_alive = True

    def is_alive(self):
        """
        Определяет уничтожена или нет пушка
        :return: статус пушки - не уничтожена
        """
        if self.health >= 0:
            return self.is_alive

    def get_damage(self):
        self.health -= 1  # FIXME добавить условие соударения пушки с бомбой

    def move(self, speed):
        self.x += speed

    def show(self):
        pygame.draw.circle(screen, color, (self.x, self.y), self.standart_radius)


class CannonGun(Cannon):
    width = 10
    length = 100

    def __init__(self):
        super().__init__()
        self.angle = math.pi / 2
        self.coord = self.gun_coord()
        self.pow = 0

    def gun_angle(self, other_x, other_y):
        """
        Определяет угол наклона дула в зависимости от расположения цели
        :param other_x: координата цели х
        :param other_y: координата цели у
        :return: угол наклона дула в месте выстрела
        """
        if other_x > self.x:
            self.angle = math.atan((self.y - other_y) / (other_x - self.x))
        elif other_x < self.x:
            self.angle = math.pi + math.atan((self.y - other_y) / (other_x - self.x))
        return self.angle

    def gun_coord(self):
        self.coord = []
        self.coord.append(self.x + int(self.length * math.cos(self.angle)))
        self.coord.append(self.y - int(self.length * math.sin(self.angle)))
        print(self.coord)
        return self.coord

    def move(self, speed):
        self.x += speed
        self.coord = self.gun_coord()

    def show(self):
        print(self.coord)
        pygame.draw.line(screen, color, (self.x, self.y), self.coord, self.width)

    def fire(self):
        """
        Создает снаряд с присвоедием определенной скорости
        :return: снаряд
        """
        self.pow = 100
        shell = Shell(coord=self.coord, angle=self.angle)
        shell.Vx = self.pow * math.cos(shell.angle)
        shell.Vy = -self.pow * math.sin(shell.angle)
        return shell


class Shell(CannonGun):
    standart_radius = 15

    def __init__(self, coord, angle):
        """Координаты снаряда наследуются от дула пушки"""
        super().__init__()
        self.coord = coord
        self.angle = angle
        self.Vx = 0
        self.Vy = 0

    def move(self, time = 1):
        ax, ay = 0, 9.8
        self.coord[0] += int(self.Vx * time + int(ax * (time**2) / 2))
        self.coord[1] += int(self.Vy * time + int(ay * (time**2) / 2))
        self.Vx += ax * time
        self.Vy += ay * time

    def show(self):
        pygame.draw.circle(screen, color, self.coord, self.standart_radius)


class Target:
    pass


class TargetMove(Target):
    pass


class Meteor_rain:
    pass


class GameManager:
    def __init__(self):
        self.cannon = Cannon()
        self.gun = CannonGun()
        self.shells = []
        self.finished = False

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True
            elif event.type == pygame.MOUSEMOTION:
                other_x, other_y = event.pos
                self.gun.gun_angle(other_x, other_y)
                self.gun.gun_coord()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.shells.append(self.gun.fire())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.cannon.move(10)
                    self.gun.move(10)
                if event.key == pygame.K_LEFT:
                    self.cannon.move(-10)
                    self.gun.move(-10)

    def move(self):
        for shell in self.shells:
            shell.move()
            shell.show()

    def game_process(self):
        self.cannon.show()
        self.gun.show()


def main():
    mng = GameManager()
    while not mng.finished:
        clock.tick(20)
        mng.event_handler()
        mng.move()
        mng.game_process()
        pygame.display.flip()
        screen.fill(BLACK)


if __name__ == "__main__":
    main()