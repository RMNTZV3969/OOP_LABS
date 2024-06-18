# ------------------------------------------------------------------------------
# Задача №1
# ------------------------------------------------------------------------------
import os


class MyClass:
    def __init__(self, path):
        while not os.path.exists(path):
            path = input('Укажите путь до файла: ')
        if os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                self.path = path
                self.file = f.read()
                self.words = self.file.split()

    def delete_word(self, word):
        try:
            while word in self.words:
                self.words.remove(word)
        except:
            pass

    def delete_char(self, value):
        for i in range(len(self.words)):
            if value in self.words[i]:
                self.words[i] = self.words[i].replace(value, '')

    def update_source(self):
        self.words = ' '.join(self.words)
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(self.words)


# ------------------------------------------------------------------------------
# Задача №2
# ------------------------------------------------------------------------------
import csv
import json


class City:
    def __init__(self, kw):
        self.kw = kw
        self.ind = str(kw['Индекс'])
        self.tip = str(kw['Тип региона'])
        self.reg = str(kw['Регион'])
        self.city = str(kw['Город'])
        self.humans = str(kw['Население'])
        self.info = ', '.join([self.ind, self.tip, self.reg, self.city, self.humans])

    def __hash__(self):
        return hash(self.ind)

    def __eq__(self, other):
        if isinstance(other, City):
            return self.ind == other.ind

    def __str__(self):
        return self.info


with open('/Users/user/Desktop/Города.json', encoding='utf-8') as file_json:
    reader_json = json.load(file_json)
    city_list = [City(j) for j in reader_json['data']]
print('Кол-во городов в файле.JSON -', len(city_list))
uniq_city_set = set(city_list)

with open('/Users/user/Desktop/Города.csv', encoding='utf-8') as file_csv:
    reader_csv = csv.DictReader(file_csv)
    print('Кол-во городов в файле.CSV -', len(list(reader_csv)))

    uniq_city_set.update(set(City(c) for c in reader_csv))
    uniq_city_list = sorted(list(uniq_city_set), key=lambda x: int(x.humans))
    print('Уникальное кол-во городов:', len(uniq_city_list))

    with open('/Users/user/Desktop/Уникальные_города.csv', 'w', encoding='utf-8') as f:
        names = ['Индекс', 'Тип региона', 'Регион', 'Город', 'Население']
        writer = csv.DictWriter(f, fieldnames=names)
        writer.writeheader()
        writer.writerows(map(lambda x: x.kw, uniq_city_list))
