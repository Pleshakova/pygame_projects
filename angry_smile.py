import pygame

pygame.init()
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
size = (400, 400)
screen = pygame.display.set_mode(size)
screen.fill(GRAY)
x = 200
y = 200
r = 100


def main():
    draw_angry_smile(x, y, r)


def draw_angry_smile(x, y, r):
    """ Рисую злобного смайла
    :param x: координата x центра окружности
    :param y: координала y центра окружности
    :param r: радиус окружности
    :return: None
    """
    pygame.draw.circle(screen, YELLOW, (x, y), r)
    pygame.draw.circle(screen, BLACK, (x, y), r, 1)
    left_eye_center = (x - r // 2, y - r // 2)
    left_eye_radius = r // 4
    right_eye_center = (x + r // 2, y - r // 2)
    right_eye_radius = r//4
    left_eyebrow_1 = (x - r, y - r)
    left_eyebrow_2 = (x - r // 4, y - r // 2)
    right_eyebrow_1 = (x + r, y - r)
    right_eyebrow_2 = (x + r // 4, y - r // 2)
    mouth_point = x - r // 2, y + r // 2
    mouth_dimension = (100, 20)
    draw_eyes(left_eye_center,left_eye_radius, right_eye_center,right_eye_radius)
    draw_eyebrows(left_eyebrow_1, left_eyebrow_2, right_eyebrow_1,right_eyebrow_2)
    draw_mouth(mouth_point,mouth_dimension)


def draw_eyes(left_eye_center,left_eye_radius, right_eye_center,right_eye_radius):
    """ Рисуем глаза в виде окружностей
    :param left_eye_center: координаты центра левого глаза
    :param left_eye_radius: радиус окружности левого глаза
    :param right_eye_center: координаты центра правого глаза
    :param right_eye_radius: радиус окружности левого глаза
    :return:
    """
    pygame.draw.circle(screen,BLACK,left_eye_center,left_eye_radius)
    pygame.draw.circle(screen,BLACK,right_eye_center,right_eye_radius)


def draw_eyebrows(left_eyebrow_1, left_eyebrow_2, right_eyebrow_1, right_eyebrow_2):
    """ Рисуем брови в виде прямых широких линий
    :param left_eyebrow_1: первая точка линии левого глаза
    :param left_eyebrow_2: вторая точка линии левого глаза
    :param right_eyebrow_1: первая точка линии правого глаза
    :param right_eyebrow_2: вторая точка линии правого глаза
    :return: None
    """
    pygame.draw.line(screen,BLACK,left_eyebrow_1,left_eyebrow_2, 5)
    pygame.draw.line(screen, BLACK, right_eyebrow_1, right_eyebrow_2, 5)


def draw_mouth(mouth_point, mouth_dimension):
    """ Рисуем рот в виде прямоугольника
    :param mouth_point: координаты точки прямоугольника
    :param mouth_dimension: длина и ширина прямоугольника
    :return: None
    """
    pygame.draw.rect(screen,BLACK,(mouth_point,mouth_dimension))


main()

clock = pygame.time.Clock()
pygame.display.update()
done = False

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

pygame.quit()
