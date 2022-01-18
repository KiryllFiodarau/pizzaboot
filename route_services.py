from abc import ABC, abstractmethod
from enums import Action
import math


class RouteService(ABC):

    @abstractmethod
    def get_route(self, optimal_way: list) -> str:
        pass


class RouteServiceByAction(RouteService):

    def get_route(self, optimal_way: list) -> str:
        actions = []
        for i in range(len(optimal_way) - 1):
            x_difference = optimal_way[i + 1].x - optimal_way[i].x
            y_difference = optimal_way[i + 1].y - optimal_way[i].y
            if x_difference == 0.0 and y_difference == 0.0:
                actions.append(Action.DROP.value)
            else:
                if x_difference > 0.0:
                    for _ in range(x_difference):
                        actions.append(Action.EAST.value)
                elif x_difference < 0.0:
                    for _ in range((x_difference * -1)):
                        actions.append(Action.WEST.value)

                if y_difference > 0.0:
                    for _ in range(y_difference):
                        actions.append(Action.NORTH.value)
                elif y_difference < 0.0:
                    for _ in range((y_difference * -1)):
                        actions.append(Action.SOUTH.value)

                actions.append(Action.DROP.value)

        return ''.join(actions)
