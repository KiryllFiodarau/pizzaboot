from abc import ABC, abstractmethod
import networkx as nx
import math_module
from point import Point

class PathOptimizationService(ABC):

    @abstractmethod
    def get_optimal_path(self, points: list) -> list:
        pass


class PathOptimizationBySort(PathOptimizationService):

    def get_optimal_path(self, points: list) -> list:
        return sorted(points, key=lambda point: point.x)


class PathOptimizationByTraverSalMethod(PathOptimizationService):

    def __init__(self) -> None:
        self._graph = nx.Graph()

    def get_optimal_path(self, points: list) -> list:

        mst = nx.minimum_spanning_tree(self._graph)
        nodes = list(nx.edge_dfs(mst, source=0))
        optimization_path = [Point(0, 0)]
        for node in nodes:
            optimization_path.append(points[node[1]])

        return optimization_path

    def init_edge(self, points: list) -> None:
        for i in range(len(points)):
            for j in range(i, len(points)):
                if i != j:
                    self._graph.add_edge(i, j, weight=math_module.distance(points[i], points[j]))
