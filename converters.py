from abc import ABC, abstractmethod
import re
from house import House


class HouseOrderOptimization(ABC):

    @abstractmethod
    def get_houses(self, input_data: str) -> list:
        pass


class HouseLocationConverter(HouseOrderOptimization):

    def __init__(self, common_pattern: str, house_location_pattern: str, field_size_pattern: str) -> None:
        self._common_pattern = common_pattern
        self._house_location_pattern = house_location_pattern
        self._field_size_pattern = field_size_pattern

    def get_houses(self, input_data: str) -> list:

        results = []
        match = re.match(self._common_pattern, input_data)

        if match is None:
            raise AttributeError('Not a valid data')

        field_size = re.findall(self._field_size_pattern, input_data)
        size = int(field_size[0][0]), int(field_size[0][0])
        houses_coordinates = re.findall(self._house_location_pattern, input_data)

        for house_coordinates in houses_coordinates:
            if int(house_coordinates[0]) < size[0] and int(house_coordinates[1]) < size[1]:
                results.append(House(int(house_coordinates[0]), int(house_coordinates[1])))
            else:
                raise AttributeError('The house goes beyond the boundaries of the field')

        return results

