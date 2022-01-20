from abc import ABC, abstractmethod
import networkx as nx
from house import House


class HouseOrderOptimization(ABC):

    @abstractmethod
    def get_optimal_houses_order(self, houses: list) -> list:
        pass


class HouseOrderOptimizationBySort(HouseOrderOptimization):

    def get_optimal_houses_order(self, houses: list) -> list:

        try:
            houses.insert(0, House(0, 0))
            sorted_houses = sorted(houses, key=lambda house: house.x)
        except AttributeError as attr_ex:
            raise attr_ex
        except Exception as ex:
            raise ex

        return sorted_houses


class HouseOrderOptimizationByTraverSal(HouseOrderOptimization):

    def __init__(self) -> None:
        self._graph = nx.Graph()

    def get_optimal_houses_order(self, houses: list) -> list:

        try:
            houses.insert(0, House(0, 0))
            self.init_edge(houses)
            mst = nx.minimum_spanning_tree(self._graph)
            nodes = list(nx.edge_dfs(mst, source=0))
            optimal_houses_order = [House(0, 0)]
            for node in nodes:
                optimal_houses_order.append(houses[node[1]])
        except nx.exception.NetworkXException as networkx_ex:
            raise networkx_ex
        except Exception as ex:
            raise ex

        return optimal_houses_order

    def init_edge(self, houses: list) -> None:
        for i in range(len(houses)):
            for j in range(i, len(houses)):
                if i != j:
                    self._graph.add_edge(i, j, weight=House.distance(houses[i], houses[j]))
