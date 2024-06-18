from jinja2 import Template, Environment, FileSystemLoader
from datetime import datetime
import csv


# ------------------------------------------------------------------------------
# Задача №1
# ------------------------------------------------------------------------------
class MyClass:
    def __init__(self, user_name, time, item, place):
        self.user_name = user_name
        self.time = time
        self.item = item
        self.place = place


obj = MyClass('Анастасия', 10, 'подарок', 'рядом')
tm = Template(
    'Приветствую тебя, {{ user_name }}! Очень рад тебя видеть! С '
    'нашей последней встречи прошло {{ time }} лет... '
    'Прими этот {{ item }} и садись {{ place }}')
msg = tm.render(user_name=obj.user_name, time=obj.time, item=obj.item, place=obj.place)
print(msg)

# ------------------------------------------------------------------------------
# Задача №2
# ------------------------------------------------------------------------------
data = {'names': ('Настя', 'Саша'), 'power': (10, 5), 'sport': 'Бокс', 'date': datetime.now()}

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('lab_2.html')
msg = tm.render(data=data)
print(msg)

# ------------------------------------------------------------------------------
# Задача №3
# ------------------------------------------------------------------------------
with open('/Users/user/Desktop/Уникальные_города_eng.csv', encoding='utf-8') as file_csv:
    csv_list = list(csv.DictReader(file_csv))
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(cities=csv_list, num=int(input('Планка кол-ва населения: ')))

# # Сохранение html файла
# with open('/Users/user/Desktop/cities.html', 'w', encoding='utf-8') as f:
#     f.write(msg)
