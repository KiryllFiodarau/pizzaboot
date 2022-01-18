from abc import ABC, abstractmethod


class PathOptimizationService(ABC):

    @abstractmethod
    def get_optimal_way(self, points: list) -> list:
        pass


class PathOptimizationBySort(PathOptimizationService):

    def get_optimal_way(self, points: list) -> list:

        return sorted(points, key=lambda point: point.x)
