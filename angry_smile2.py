def main():
    screen = (400, 400)
    x = 200
    y = 200
    r = 100
    draw_angry_smile(x, y, r)


def draw_angry_smile(x, y, r):
    """ Рисую злобного смайла
    x- координата x центра окружности
    y- координала y центра окружности
    r- радиус окружности
    """
    print("Типа рисую angry_smile", x, y, r)
    left_eye = (x - r // 2, y - r // 2, r // 4)
    right_eye = (x + r // 2, y - r // 2, r // 4)
    left_eyebrow = (x - r, y - r, x - r // 4, y - r // 2)
    right_eyebrow = (x + r, y - r, x + r // 4, y - r // 2)
    mouth = x - r // 2, y + r // 2
    draw_eyes(left_eye, right_eye)
    draw_eyebrows(left_eyebrow, right_eyebrow)
    draw_mouth(mouth)


def draw_eyes(left_eye, right_eye):
    """Рисуем левый и правый глаз
    """
    pass
    print("Типа рисую глаза", left_eye, right_eye)


def draw_eyebrows(left_eyebrow, right_eyebrow):
    """Рисуем левую и плавую бровь
    """
    pass
    print("Типа рисую брови", left_eyebrow, right_eyebrow)


def draw_mouth(mouth):
    """Рисуем рот
    """
    pass
    print("Типа рисую рот", mouth)


main()
