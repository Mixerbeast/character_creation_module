from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Функция, которая генерирует и возвращает строку с сообщением об атаке.
    :param char_name: str, имя персонажа.
    :param char_class: str, класс персонажа (warrior, mage или healer).
    :return: str, строка с сообщением об атаке и сгенерированным уроном.
    """
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')
    return (f'{char_name} не Атаковал')


def defence(char_name: str, char_class: str) -> str:
    """Функция, которая генерирует и возвращает строку с сообщением о блокировании.
    :param char_name: str, имя персонажа.
    :param char_class: str, класс персонажа (warrior, mage или healer).
    :return: str, строка с сообщением о блокировании урона и сгенерированными
    очками защиты.
    """
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} ед. урона')
    return (f'{char_name} не блокировал Атаку')


def special(char_name: str, char_class: str) -> str:
    """Функция которая возвращает строку с сообщением о применении.
    специального умения и сгенерированными очками для этого умения.
    :param char_name: имя персонажа
    :param char_class: класс персонажа
    :return: возвращение сгенерированных очков для этого умения
    """
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Функция которая о запускает режим тренировки персонажа.
    В зависимости от класса персонажа выводится соответствующее приветствие.
    :param char_name: имя персонажа
    :param char_class: класс персонажа
    :param while: обрабатывает алгоритм пропуска тренировки или вывод одной
    применения команды
    :return: производит выход из функции тренировка
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Функция которая запоминает выбор класса персонажа пользователем.
    и возращает выбранный класс персонажа.
    :param char_name: Ввод имени пользователя
    :param char_class: Выбор класса персонажа
    :param: approve_choice: подтверждение выбора персонажа
    :return: возвращение текущего значения выброного персонажа
    """
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.'
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа: ').lower()
    return char_class



main()


# ...запишите:
if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
