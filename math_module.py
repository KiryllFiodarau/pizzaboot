import math
from point import Point


def distance(point_one: Point, point_two: Point):
    return math.fabs(point_one.x - point_two.x) + math.fabs(point_one.y - point_two.y)
