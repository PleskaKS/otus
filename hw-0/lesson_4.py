import re
from math import sqrt


def convert_quantity(digit: int) -> str:
    """Вводится целое число (любого размера). Написать функцию, которая разобьет это число на разряды символом "пробел",
     Функция возвращает тип данных str 1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976` """

    digit_reformat = '{0:,}'.format(digit).replace(',', ' ')
    return digit_reformat


def change_case(txt: str) -> str:
    """Написать функцию, которая заменяет принимает строку текста и изменяет снейк_кейс на КамелКейс и наоборот
    my_first_func -> MyFirstFunc, AnotherFunction -> another_function"""
    if re.match(r'^([A-Z][a-z\d]+)+', txt):
        return "".join(['_' + x.lower() if x.isupper() else x for x in txt]).lstrip("_")
    elif re.match(r'^([a-z][a-z\d]+_)+([a-z][a-z\d]+)', txt):
        return "".join(x.capitalize() for x in txt.lower().split("_"))
    else:
        raise ValueError("Invalid format")


def solve_equation(func: str):
    """Написать функцию, которая принимает на вход квадратное уравнение (одной строкой) и возвращает его корни, либо сообщает, что их нет
    "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7"""
    func = func.replace(' ', '')
    p = re.compile(r'(?P<a>-?\d*)?\*?(x\*\*2)(\+?(?P<b>-?\d*)?\*?(?P<x>x)?)?(\+)?(?P<c>-?\d*)?')
    m = p.search(func)

    a = int(m.group('a').replace(' ', '')) if m.group('a') != '' else 1
    b = get_param_b(m)
    c = get_param_c(m)

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = int((-b + sqrt(discriminant)) / (2 * a))
        x2 = int((-b - sqrt(discriminant)) / (2 * a))
        return x1, x2
    elif discriminant == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        return "Уравнение не имеет действительных корней"


def get_param_b(match: re.Match):
    if match.group('x') != '' and match.group('x') is not None:
        return int(match.group('b').replace(' ', '')) if match.group('b') != '' else 1
    else:
        return 0


def get_param_c(match: re.Match):
    group_name = 'c' if get_param_b(match) != 0 else 'b'
    return int(match.group(group_name).replace(' ', '')) if match.group(group_name) != '' else 0


def encrypt_caesar(word: str, shift: int) -> str:
    """Шифр Цезаря. Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int). Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря)
    'dog', 3 -> 'grj', 'python', 5 -> 'udymts"""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_word = []

    for i in word:
        ilow = i.lower()
        enc = i.replace(i, alphabet[alphabet.index(ilow) + shift
        if alphabet.index(ilow) + shift < len(alphabet)
        else len(alphabet) - alphabet.index(ilow) + shift - 1])
        encrypted_word.append(enc if i.islower() else enc.upper())

    return ''.join(encrypted_word)


def decrypt_caesar(word: str, shift: int) -> str:
    """Написать вторую функцию, которая будет проводить обратный процесс (или написать одну, выполняющую оба действия"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_word = []

    for i in word:
        ilow = i.lower()
        enc = i.replace(i, alphabet[alphabet.index(ilow) - shift])
        encrypted_word.append(enc if i.islower() else enc.upper())

    return ''.join(encrypted_word)


