from abc import ABC, abstractmethod
import networkx as nx
import math_module
from point import Point
from converters import PointConvertor


class WayOptimizationService(ABC):

    @abstractmethod
    def get_optimal_way(self, input_data: str) -> list:
        pass


class WayOptimizationBySort(WayOptimizationService):

    def __init__(self, convertor: PointConvertor) -> None:
        self._convertor = convertor

    def get_optimal_way(self, input_data: str) -> list:

        points = self._convertor.get_way(input_data)

        return sorted(points, key=lambda point: point.x)


class WayOptimizationByTraverSal(WayOptimizationService):

    def __init__(self, convertor: PointConvertor) -> None:
        self._graph = nx.Graph()
        self._convertor = convertor

    def get_optimal_way(self, input_data: str) -> list:

        try:
            points = self._convertor.get_way(input_data)
            self.init_edge(points)
            mst = nx.minimum_spanning_tree(self._graph)
            nodes = list(nx.edge_dfs(mst, source=0))
            optimization_path = [Point(0, 0)]
            for node in nodes:
                optimization_path.append(points[node[1]])
        except nx.exception.NetworkXException as networkx_ex:
            raise networkx_ex
        except Exception as ex:
            raise ex

        return optimization_path

    def init_edge(self, points: list) -> None:
        for i in range(len(points)):
            for j in range(i, len(points)):
                if i != j:
                    self._graph.add_edge(i, j, weight=math_module.distance(points[i], points[j]))
