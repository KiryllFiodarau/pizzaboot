from point import Point
from path_optimization_services import PathOptimizationBySort
from route_services import RouteServiceByAction

points = [Point(0, 0), Point(1, 4), Point(4, 1), Point(2, 4)]

path_opt = PathOptimizationBySort()

new_points = path_opt.get_optimal_way(points)
route_services = RouteServiceByAction()
print(new_points)
print(route_services.get_route(new_points))
