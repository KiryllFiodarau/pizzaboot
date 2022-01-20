import unittest
from unittest.mock import patch
from house import House
from converters import HouseOrderOptimization, HouseLocationConverter
from house_order_optimization import HouseOrderOptimizationByTraverSal,HouseOrderOptimizationBySort
import networkx as nx

common_pattern = r'^([1-9][0-9]*)x([1-9][0-9]*)( \([0-9]+\, [0-9]+\))+$'
house_location_pattern = r'\(([0-9]+)\, ([0-9]+)\)'
field_size_pattern = r'([1-9][0-9]*)x([1-9][0-9]*)'
input_data = '5x5 (0, 0) (1, 1)'
input_without_start = '5x5 (1, 1)'
input_incorrect_pattern = '5x'
input_incorrect_house_location = '5x5 (0,10)'
houses_pass_test = [House(1, 3), House(4, 4)]
houses_fail_test = []
houses_pass_sort = [House(4, 4), House(1, 3)]
houses_fail_sort = ['test']


class HouseLocationConverterTest(unittest.TestCase):

    @patch.multiple(HouseOrderOptimization, __abstractmethods__=set())
    def setUp(self) -> None:
        self.house_location_convertor = HouseLocationConverter(
            common_pattern,
            house_location_pattern,
            field_size_pattern)

    def test_get_houses_pass(self) -> None:
        assert self.house_location_convertor.get_houses(input_data) == [House(0, 0), House(1, 1)]
        assert self.house_location_convertor.get_houses(input_without_start) == [House(1, 1)]

    def test_get_houses_fail(self) -> None:
        with self.assertRaises(AttributeError):
            self.house_location_convertor.get_houses(input_incorrect_pattern)
            self.house_location_convertor.get_houses(input_incorrect_house_location)


class HouseOrderOptimizationByTraverSalTest(unittest.TestCase):

    def setUp(self) -> None:
        self._house_order_optimizer = HouseOrderOptimizationByTraverSal()

    def test_get_optimal_houses_order_pass(self) -> None:
        assert self._house_order_optimizer.get_optimal_houses_order(houses_pass_test) == [House(0, 0),
                                                                                          House(1, 3),
                                                                                          House(4, 4)]

    def test_get_optimal_houses_order_fail(self) -> None:
        with self.assertRaises(nx.exception.NetworkXException):
            self._house_order_optimizer.get_optimal_houses_order(houses_fail_test)


class HouseOrderOptimizationBySortTest(unittest.TestCase):

    def setUp(self) -> None:
        self._house_order_optimizer = HouseOrderOptimizationBySort()

    def test_get_optimal_houses_order_pass(self) -> None:
        assert self._house_order_optimizer.get_optimal_houses_order(houses_pass_sort) == [House(0, 0),
                                                                                          House(1, 3),
                                                                                          House(4, 4)]

    def test_get_optimal_houses_order_fail(self) -> None:
        with self.assertRaises(AttributeError):
            self._house_order_optimizer.get_optimal_houses_order(houses_fail_sort)


if __name__ == '__main__':
    unittest.main()
