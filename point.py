class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        if x < 0:
            raise ValueError('Negative point!')
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        if y < 0:
            raise ValueError('Negative point!')
        self._y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
