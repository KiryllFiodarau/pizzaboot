from abc import ABC, abstractmethod
import re
from point import Point


class PointConvertor(ABC):

    @abstractmethod
    def get_way(self, input_data: str) -> list:
        pass


class PointConvertorByRegex(PointConvertor):

    def __init__(self, common_pattern: str, point_pattern: str, field_size_pattern: str) -> None:
        self._common_pattern = common_pattern
        self._point_pattern = point_pattern
        self._field_size_pattern = field_size_pattern

    def get_way(self, input_data: str) -> list:

        results = []
        match = re.match(self._common_pattern, input_data)
        if match is None:
            raise AttributeError('Not a valid date')
        else:
            field_size = re.findall(self._field_size_pattern, input_data)
            size = int(field_size[0][0]), int(field_size[0][0])
            points = re.findall(self._point_pattern, input_data)
            for point in points:
                if int(point[0]) < size[0] and int(point[1]) < size[1]:
                    results.append(Point(int(point[0]), int(point[1])))
                else:
                    raise AttributeError('The point goes beyond the boundaries of the field')

        return self.add_start_point(results)

    @staticmethod
    def add_start_point(points: list) -> list:

        if points[0].x == 0 and points[0].y == 0:
            return points
        else:
            index_point = 0
            for i in range(len(points)):
                if points[i].x == 0 and points[i].y == 0:
                    index_point = i
                    break
            if index_point:
                points.remove(index_point)
                points.insert(0, Point(0, 0))
            else:
                points.insert(0, Point(0, 0))

        return points
