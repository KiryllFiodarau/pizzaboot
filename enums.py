from enum import Enum


class Action(Enum):
    MOVE_NORTH = 'N'
    MOVE_SOUTH = 'S'
    MOVE_EAST = 'E'
    MOVE_WEST = 'W'
    DROP_PIZZA = 'D'
