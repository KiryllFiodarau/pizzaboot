import unittest
from unittest.mock import patch
from unittest import mock
from point import Point
from converters import PointConvertor, PointConvertorByRegex
from way_optimization_services import WayOptimizationByTraverSal
import networkx as nx

common_pattern = r'^([1-9][0-9]*)x([1-9][0-9]*)( \([0-9]+\, [0-9]+\))+$'
point_pattern = r'\(([0-9]+)\, ([0-9]+)\)'
field_size_pattern = r'([1-9][0-9]*)x([1-9][0-9]*)'
input_data = '5x5 (0, 0) (1, 1)'
input_without_start = '5x5 (1, 1)'
input_incorrect_pattern = '5x'
input_incorrect_point = '5x5 (0,10)'
input_data_optimal_way = '5x5 (4, 4) (1, 3)'
input_data_optimal_fail = '5x5 (0, 0)'


class PointConvertorByRegexTest(unittest.TestCase):

    @patch.multiple(PointConvertor, __abstractmethods__=set())
    def setUp(self) -> None:
        self.point_convertor = PointConvertorByRegex(
            common_pattern,
            point_pattern,
            field_size_pattern)

    def test_get_way_pass(self) -> None:
        assert self.point_convertor.get_way(input_data) == [Point(0, 0), Point(1, 1)]
        assert self.point_convertor.get_way(input_without_start) == [Point(0, 0), Point(1, 1)]

    def test_get_way_fail(self) -> None:
        with self.assertRaises(AttributeError):
            self.point_convertor.get_way(input_incorrect_pattern)
            self.point_convertor.get_way(input_incorrect_point)


class WayOptimizationByTraverSalTest(unittest.TestCase):

    @patch.multiple(PointConvertor, __abstractmethods__=set())
    def setUp(self) -> None:
        self._optimization_traver_sal = WayOptimizationByTraverSal(PointConvertor())

    @mock.patch.object(PointConvertor, 'get_way')
    def test_get_optimal_way_pass(self, get_way) -> None:
        get_way.return_value = [Point(0, 0), Point(4, 4), Point(1, 3)]

        assert self._optimization_traver_sal.get_optimal_way(input_data_optimal_way) == [Point(0, 0), Point(1, 3),
                                                                                         Point(4, 4)]

    @mock.patch.object(PointConvertor, 'get_way')
    def test_get_optimal_way_fail(self, get_way) -> None:
        get_way.return_value = [Point(0, 0)]

        with self.assertRaises(nx.exception.NetworkXException):
            self._optimization_traver_sal.get_optimal_way(input_data_optimal_fail)


if __name__ == '__main__':
    unittest.main()
