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

        return results
