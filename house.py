import math


class House:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_house_first(self) -> bool:

        return self._x == 0 and self._y == 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __hash__(self):
        return hash(self.x + self.y)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        if x < 0:
            raise ValueError('Negative coordinate!')
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        if y < 0:
            raise ValueError('Negative coordinate!')
        self._y = y

    def __repr__(self):
        return f'House(x={self.x}, y={self.y})'

    @staticmethod
    def distance(house_one, house_two):
        return math.fabs(house_one.x - house_two.x) + math.fabs(house_one.y - house_two.y)
