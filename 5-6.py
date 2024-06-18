class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.__x = x
        self.__y = y

    def set_coordinate(self, x, y):
        self.__x = x
        self.__y = y

    def get_coordinate(self):
        return self.__x, self.__y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y

    def __add__(self, other):
        if isinstance(other, Point):
            return Segment(self, other)
        if isinstance(other, Segment):
            return BrokenLine([self, other.point1, other.point2])
        if isinstance(other, BrokenLine):
            return other.point_list.append(self)
        raise BaseException('Неверные данные')

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'


class Segment:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.point1_x, self.point1_y = self.point1.get_coordinate()
        self.point2_x, self.point2_y = self.point2.get_coordinate()

    def get_len(self):
        return (((self.point1_x - self.point2_x) ** 2) + ((self.point1_y - self.point2_y) ** 2)) ** 0.5

    def __str__(self):
        return f'{self.point1.name}{self.point2.name}({self.point1_x}, {self.point1_y}; {self.point2_x}, {self.point2_y})'

    def __add__(self, other):
        if isinstance(other, Segment):
            if self.point1 == (other.point1 or other.point2) or self.point2 == (other.point1 or other.point2):
                return BrokenLine([self.point1, self.point2, other.point1, other.point2])
        if isinstance(other, Point):
            return BrokenLine([other, self.point1, self.point2])
        if isinstance(other, BrokenLine):
            return other.point_list.extend([self.point2, self.point1])
        raise BaseException('Неверные данные')


class BrokenLine:
    def __init__(self, point_list=[]):
        if len(point_list) >= 3:
            self.point_list = point_list
        else:
            raise BaseException('Меньше 3-х точек')

    def get_len(self):
        sum_point = 0
        for value in range(len(self.point_list) - 1):
            sum_point += (Segment(self.point_list[value], self.point_list[value + 1])).get_len()
        return sum_point

    def __str__(self):
        return ''.join(set([i.name for i in self.point_list]))

    def __add__(self, other):
        if isinstance(other, Segment):
            return self.point_list.extend([other.point1, other.point2])
        if isinstance(other, Point):
            return self.point_list.append(other)
        if isinstance(other, BrokenLine):
            return self.point_list.extend(other.point_list)
        raise BaseException('Неверные данные')
