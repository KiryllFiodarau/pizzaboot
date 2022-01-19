from point import Point
from path_optimization_services import PathOptimizationBySort, PathOptimizationByTraverSalMethod
from route_services import RouteServiceByAction

points = [Point(0, 0), Point(1, 3), Point(4, 4), Point(4, 2), Point(4, 2), Point(0, 1), Point(3, 2), Point(2, 3),
          Point(4, 1)]

# points = [Point(0, 0), Point(1, 4), Point(2, 4), Point(4, 1)]

route_services = RouteServiceByAction()
trever_sal = PathOptimizationByTraverSalMethod()
trever_sal.init_edge(points)

optimal_path = trever_sal.get_optimal_path(points)
print(optimal_path)
print(route_services.get_route(optimal_path))

path_opt = PathOptimizationBySort()
new_points = path_opt.get_optimal_path(points)

print(new_points)
print(route_services.get_route(new_points))
