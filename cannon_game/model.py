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

    def is_not_alive(self):
        """
        Определяет уничтожена или нет пушка
        :return: статус пушки - не уничтожена
        """
        return self.health < 0

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
        shell = Shell(self.coord, self.angle)
        shell.Vx = self.pow * math.cos(shell.angle)
        shell.Vy = -self.pow * math.sin(shell.angle)
        return shell


class Shell:
    standart_radius = 15

    def __init__(self, coord, angle):
        """Координаты снаряда наследуются от дула пушки"""
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
        self.width = 100
        self.height = 50
        self.coord = self.set_coords()
        self.target_center = [self.coord[0] + self.width // 2, self.coord[1] + self.height // 2]
        self.fire_angle = 0
        self.pow = 30

    def set_coords(self):
        self.coord = []
        self.coord.append(randint(0, self.target_field_width - self.width))
        self.coord.append(randint(0, self.target_field_height - self.height))
        return self.coord

    def fire(self):
        """
        Создает бомбу с передачей собственных координат и с заданным направлением удара
        :return: экземпляр бомбы
        """
        fire_angle = [math.pi * 1 / 4, math.pi * 1 / 2, math.pi * 3 / 4]
        self.fire_angle = fire_angle[randint(0, 2)]
        bomb = Bomb(list(self.target_center), self.fire_angle)
        return bomb

    def show(self):
        pygame.draw.ellipse(screen, color, (self.coord[0], self.coord[1], self.width, self.height))

    def get_collision(self, list, radius):
        length = ((self.target_center[0] - list[0]) ** 2 + (self.target_center[1] - list[1]) ** 2) ** 0.5
        return length <= radius + self.height // 2


class TargetMove(Target):
    def __init__(self):
        super().__init__()
        self.Vx = randint(-5, 5)

    def move(self):
        if self.is_border_reached():
            self.Vx = -1 * self.Vx
        self.coord[0] += self.Vx

    def is_border_reached(self):
        return self.coord[0] + self.width // 2 >= width or self.coord[0] - self.width // 2 <= 0


class Bomb:
    def __init__(self, coord, angle):
        self.coord = coord
        self.angle = angle
        self.radius = 30
        self.Vy = 0

    def move(self):
        self.coord[0] += int(math.cos(self.angle) * 5)
        self.coord[1] += int(math.sin(self.angle) * 5)

    def show(self):
        pygame.draw.circle(screen, [100, 100, 100], self.coord, self.radius)  # TODO change color

    def is_border_reached(self):
        return self.coord[0] < 0 or self.coord[0] > width or self.coord[1] > height


class GameManager:
    target_number = 5

    def __init__(self):
        self.cannon = Cannon()
        self.gun = CannonGun()
        self.shells = []
        self.targets = []
        self.bombs = []
        self.finished = False

    def target_creation(self, n=target_number):
        target = Target()
        self.targets.append(target)
        while len(self.targets) <= n - 1:
            indicator = True
            other = Target()
            for target in self.targets:
                length = ((target.coord[0] - other.coord[0]) ** 2 + (target.coord[1] - other.coord[1]) ** 2) ** 0.5
                if length <= 100:
                    indicator = False
            if indicator:
                self.targets.append(other)
        return self.targets

    def bomb_creation(self):
        for target in self.targets: # TODO What does it for?
            target = self.targets[randint(0, len(self.targets)-1)]
            self.bombs.append(target.fire())
            return self.bombs

    def bomb_control_border(self):
        for bomb in self.bombs:
            if bomb.is_border_reached():
                self.bombs.remove(bomb)

    def is_cannon_bombed(self):
        for bomb in self.bombs:
            length = ((self.cannon.x - bomb.coord[0])**2 + (self.cannon.y - bomb.coord[1])**2)**0.5
            if length <= self.cannon.standart_radius + bomb.radius:
                self.cannon.get_damage()
                if self.cannon.is_not_alive():
                    print('GAME IS OVER')
                    self.finished = True
                self.bombs.remove(bomb)

    def event_handler(self, dt):
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

    def collision(self):
        for target in self.targets:
            for shell in self.shells:
                if target.get_collision(shell.coord, shell.standart_radius):
                    self.targets.remove(target)
                    self.shells.remove(shell)
        if not self.targets:
            print('YOU WIN!')
            self.finished = True

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
        for target in self.targets:
            target.show()
        for bomb in self.bombs:
            bomb.show()


def main():
    pygame.init()
    time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    dt = clock.tick(30) / 1000
    mng = GameManager()
    mng.target_creation()
    mng.bomb_creation()
    while not mng.finished:
        clock.tick(30)
        if pygame.time.get_ticks() >= time + 1000:
            time = pygame.time.get_ticks()
            mng.bomb_creation()
        mng.bomb_control_border()
        mng.is_cannon_bombed()
        mng.event_handler(dt)
        mng.collision()
        mng.move()
        mng.game_show()
        pygame.display.flip()
        screen.fill(BLACK)


if __name__ == "__main__":
    main()
    pygame.quit()
