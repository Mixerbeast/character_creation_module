from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Указывается квадратный корень."""
    if your_number <= 0:
        print('Невозможно вычислить квадратный корень')
        return
    result = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {result}')


calc(25.5)
