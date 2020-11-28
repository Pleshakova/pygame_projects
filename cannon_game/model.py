import pygame
from random import randint
import math

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
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
        self.coord = []
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
        return self.coord

    def move(self, speed):
        self.x += speed
        self.gun_coord()

    def show(self):
        pygame.draw.line(screen, color, (self.x, self.y), self.gun_coord(), self.width)  # TODO why not self.coord?

    def fire(self):
        """
        Создает снаряд с присвоедием определенной скорости
        :return: экземпляр снаряда
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

    def move(self, time=1):
        ax, ay = 0, 9.8
        self.coord[0] += int(self.Vx * time + int(ax * (time ** 2) / 2))
        self.coord[1] += int(self.Vy * time + int(ay * (time ** 2) / 2))
        self.Vx += ax * time
        self.Vy += ay * time

    def show(self):
        pygame.draw.circle(screen, color, self.coord, self.standart_radius)

    def is_reached_border(self):
        return self.coord[0] <= 0 or self.coord[0] >= width or self.coord[1] <= 0 or self.coord[1] >= height


class Target:
    target_field_width = width
    target_field_height = height // 3

    def __init__(self):
        self.coord = []
        self.width = 100
        self.height = 50
        self.coord = self.set_coords()
        self.target_center = [self.coord[0] + self.width // 2, self.coord[1] + self.height // 2]
        self.fire_angle = math.pi * 3 / 2
        self.pow = 30

    def set_coords(self):
        self.coord.append(randint(0, self.target_field_width - self.width))
        self.coord.append(randint(0, self.target_field_height - self.height))
        return self.coord

    def fire(self):
        """
        Создает бомбу с передачей собственных координат и с заданным направлением удара
        :return: экземпляр бомбы
        """
        bomb = Bomb(coord=self.target_center, pow=self.pow, angle=self.fire_angle)
        return bomb

    def show(self):
        pygame.draw.ellipse(screen, color, (self.coord[0], self.coord[1], self.width, self.height))


class TargetMove(Target):
    def __init__(self):
        super().__init__()
        self.Vx = randint(-5, 5)

    def move(self):
        if self.is_reached_border():
            self.Vx = -1 * self.Vx
        self.coord[0] += self.Vx

    def is_reached_border(self):
        return self.coord[0] + self.width // 2 >= width or self.coord[0] - self.width // 2 <= 0


class Bomb:
    def __init__(self, coord, pow, angle):
        self.coord = coord
        self.radius = 30
        self.pow = pow
        self.angle = angle

    def move(self):
        self.coord[0] += int(math.cos(self.angle) * self.pow)
        self.coord[1] += 10

    def show(self):
        pygame.draw.circle(screen, [100, 100, 100], self.coord, self.radius)  # TODO change color


class GameManager:
    def __init__(self):
        self.cannon = Cannon()
        self.gun = CannonGun()
        self.shells = []
        self.non_moving_targets = []
        self.bombs = []
        self.finished = False

    def non_moving_target_creation(self, n):
        for i in range(n):
            self.non_moving_targets.append(Target())
        return self.non_moving_targets

    def target_fire(self):
        for target in self.non_moving_targets:
            self.bombs.append(target.fire())

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
            if not shell.is_reached_border():
                shell.move()
            else:
                self.shells.remove(shell)
        for bomb in self.bombs:
            bomb.move()

    def game_show(self):
        self.cannon.show()
        self.gun.show()
        for shell in self.shells:
            shell.show()
        for target in self.non_moving_targets:
            target.show()
        for bomb in self.bombs:
            bomb.show()

def main():
    pygame.init()
    time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    mng = GameManager()
    mng.non_moving_target_creation(5)
    while not mng.finished:
        clock.tick(30)
        if pygame.time.get_ticks() >= time + 1000:
            time = pygame.time.get_ticks()
            print('hello')
            mng.target_fire()
        mng.event_handler()
        mng.move()
        mng.game_show()
        pygame.display.flip()
        screen.fill(BLACK)


if __name__ == "__main__":
    main()
