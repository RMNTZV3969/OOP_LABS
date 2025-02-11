# ------------------------------------------------------------------------------
# Задача №1
# ------------------------------------------------------------------------------
print(len(input('Введите строку: ')))

# ------------------------------------------------------------------------------
# Задача №2
# ------------------------------------------------------------------------------
name = input('Введите ФИО: ').title().split()
print(f'{name[0]} {name[1][0]}. {name[2][0]}.')

# ------------------------------------------------------------------------------
# Задача №3
# ------------------------------------------------------------------------------
codes = ['summer', 'winter', 'spring', 'autumn']
code = input('введите кодовое слово: ')
if code in codes:
    print('кодовое слово есть в списке')
else:
    print('кодовое слово не в списке')

# ------------------------------------------------------------------------------
# Задача №4
# ------------------------------------------------------------------------------
num = int(input('Введите число: '))
if num > 0:
    for value in range(1, num + 1):
        print(f'{value}^2 = {value ** 2}')
else:
    print('Число ме положительное')

# ------------------------------------------------------------------------------
# Задача №5
# ------------------------------------------------------------------------------
nums = [int(value) for value in input().split()]
if len(nums) > 10:
    raise BaseException('больше 10 чисел')
print(sorted(nums))

# ------------------------------------------------------------------------------
# Задача №6
# ------------------------------------------------------------------------------
word = input()
for symbol in range(0, len(word), 2):  # т.к. отсчет с 0 по заданию
    print(word[symbol])


# ------------------------------------------------------------------------------
# Задача №7
# ------------------------------------------------------------------------------
def multiply(num1, num2):
    if num1 >= 0 and num2 >= 0:
        return num1 * num2
    else:
        return 'Введенные числа не положительные'


print(multiply(2, 0))

# ------------------------------------------------------------------------------
# Задача №8
# ------------------------------------------------------------------------------
import random


def multiply(num1, num2):
    if num1 >= 0 and num2 >= 0:
        return num1 * num2
    else:
        return 'Введенные числа не положительные'


user_num = int(input('Введите число больше 5: '))
num = random.randint(0, 6)
if user_num > 5:
    print(multiply(user_num, num))

# ------------------------------------------------------------------------------
# Задача №9
# ------------------------------------------------------------------------------
import random
from datetime import datetime, timedelta


def random_date():
    year = random.randint(1900, 2100)
    month = random.randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month = 29  # Високосный год
        else:
            days_in_month = 28  # Не високосный год
    day = random.randint(1, days_in_month)
    random_date = datetime(year, month, day).strftime('%d-%m-%Y')

    return random_date


print(random_date())

# ------------------------------------------------------------------------------
# Задача №10
# ------------------------------------------------------------------------------
from random import randint
import datetime


def func(date1, date2=datetime.datetime.now()):
    date1 = datetime.datetime.strptime(date1, '%d.%m.%Y')
    return (date2 - date1).seconds


print(func('.'.join([str(randint(1, 30)), str(randint(1, 12)), str(randint(1, 2022)).zfill(4)])))

# ------------------------------------------------------------------------------
# Задача №11
# ------------------------------------------------------------------------------
print('Сколько цветов на флаге РФ?')
answers = [1, 2, 3, 4]
print('Варианты ответа:')
print(*answers)
user_answer = int(input('Введите ответ: '))
if user_answer == answers[2]:
    print('Правильный ответ')
else:
    print('Неправильный ответ')

# ------------------------------------------------------------------------------
# Задача №12
# ------------------------------------------------------------------------------
my_dict = {'-': 'минус', '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять'}
user_num = input('Введите число от -5 до 5: ')
if user_num.startswith('-0'):
    user_num = user_num[1:]
if 5 >= int(user_num) >= -5:
    answer = ''
    for symbol in user_num:
        answer += my_dict[symbol] + ' '
    print(answer)
else:
    print('Введеное число не входит в заданный интервал')

# ------------------------------------------------------------------------------
# Задача №13
# ------------------------------------------------------------------------------
import random

random_num = random.randint(0, 11)
live = 3
user_num = int(input('Введите чило: '))
while live > 1:
    if user_num == random_num:
        print('Ты победил!')
        break
    else:
        live -= 1
        print('Неправильно, кол-во жизней =', live)
    user_num = int(input('Введите чило: '))
else:
    print('Ты проиграл')

# ------------------------------------------------------------------------------
# Задача №14
# ------------------------------------------------------------------------------
import random


def random_string_upper(str_list):
    result = random.choice(str_list).upper()
    return result


print(random_string_upper(input().split()))


# ------------------------------------------------------------------------------
# Задача №15
# ------------------------------------------------------------------------------
def returned_dict(user_str):
    info_dict = dict()
    info_dict['length'] = len(user_str)
    info_dict['count'] = len(user_str.split())
    info_dict['digit_count'] = 0
    for symbol in user_str:
        if symbol.isdigit():
            info_dict['digit_count'] += 1
    return info_dict


print(returned_dict(input()))
