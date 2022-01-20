from way_optimization_services import WayOptimizationByTraverSal
from route_services import RouteServiceByAction
import sys
from converters import PointConvertorByRegex
from decouple import config

if __name__ == '__main__':

    if len(sys.argv) == 2:
        point_converter_regex = PointConvertorByRegex(
            config('COMMON_PATTERN'),
            config('POINT_PATTERN'),
            config('FIELD_SIZE_PATTERN'))
        way_optimization_travel_sal = WayOptimizationByTraverSal(point_converter_regex)
        route_service = RouteServiceByAction(way_optimization_travel_sal)
        print(route_service.get_route(sys.argv[1]))

    else:

        print("Invalid input arguments")
