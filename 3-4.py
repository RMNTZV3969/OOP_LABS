# ------------------------------------------------------------------------------
# Задача №1
# ------------------------------------------------------------------------------
class Cat:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def get_sound(self):
        return 'мяю'

    def add_friend(self, obj):
        if obj != self:
            self.friends.append(obj)
        else:
            raise BaseException(f'Нельзя добавить самого себя в друзья')

    def friends_list(self):
        if self.friends:
            friends = [friend.name for friend in self.friends]
            return f'Друзья {self.name}: {friends}'
        return 'Список друзей пуст'


class Dog:
    def __init__(self, name):
        self.name = name

    def get_sound(self):
        return 'гав-гав'


class Chicken:
    def __init__(self, name):
        self.name = name

    def get_sound(self):
        return 'чик-чик'


animals = [Dog('Шарик'), Dog('Тузик'), Dog('Рекс'), Cat('Мурка'), Cat('Ася'), Cat('Барсик'), Chicken('Петя'),
           Chicken('Кок'), Chicken('Цыпа')]
for animal in animals:
    print(animal.name, animal.get_sound())


# ------------------------------------------------------------------------------
# Задача №2
# ------------------------------------------------------------------------------
class Human:
    def __init__(self, name, surname, father_name, age=0, gender='М'):
        self.name = name.title()
        self.surname = surname.title()
        self.father_name = father_name.title()
        self.age = age
        self.gender = gender.title()

    def get_fio(self):
        return f'{self.surname} {self.name[0]}. {self.surname[0]}.'

    def get_full_info(self):
        return (f'Фамилия: {self.surname},\nИмя: {self.name},\nОтчество: {self.father_name},'
                f'\nПол: {self.gender},\nВозраст: {self.age}')


class Student(Human):
    def __init__(self, name, surname, father_name, group, age=0, gender='М'):
        super().__init__(name, surname, father_name, age=0, gender='М')
        self.group = group

    def get_full_info(self):
        return (f'Фамилия: {self.surname},\nИмя: {self.name},\nОтчество: {self.father_name},'
                f'\nПол: {self.gender},\nВозраст: {self.age},\nГруппа: {self.group}')


# ------------------------------------------------------------------------------
# Задача №3
# ------------------------------------------------------------------------------
class Triangle:

    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def check(self):
        result_check = (
                (self.__side1 + self.__side2) > self.__side3 and (self.__side1 + self.__side3) > self.__side2 and (
                self.__side2 + self.__side3) > self.__side1)
        return result_check if result_check else 'Не соответствует правилу треугольника'

    def set_side1(self, value):
        if isinstance(value, (int,)):
            old_value = self.__side1
            self.__side1 = value
            if not self.check():
                self.__side1 = old_value

    def set_side2(self, value):
        if isinstance(value, (int,)):
            old_value = self.__side2
            self.__side2 = value
            if not self.check():
                self.__side2 = old_value

    def set_side3(self, value):
        if isinstance(value, (int,)):
            old_value = self.__side3
            self.__side3 = value
            if not self.check():
                self.__side3 = old_value

    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3
