from abc import ABC, abstractmethod
from enums import Action


class ActionService(ABC):

    @abstractmethod
    def get_actions(self, houses: list) -> str:
        pass


class PizzaBotActionService(ActionService):

    def get_actions(self, houses: list) -> str:

        actions = []
        for i in range(len(houses) - 1):
            x_difference = houses[i + 1].x - houses[i].x
            y_difference = houses[i + 1].y - houses[i].y
            if x_difference == 0.0 and y_difference == 0.0:
                actions.append(Action.DROP_PIZZA.value)
            else:
                if x_difference > 0.0:
                    for _ in range(x_difference):
                        actions.append(Action.MOVE_EAST.value)
                elif x_difference < 0.0:
                    for _ in range((x_difference * -1)):
                        actions.append(Action.MOVE_WEST.value)

                if y_difference > 0.0:
                    for _ in range(y_difference):
                        actions.append(Action.MOVE_NORTH.value)
                elif y_difference < 0.0:
                    for _ in range((y_difference * -1)):
                        actions.append(Action.MOVE_SOUTH.value)

                actions.append(Action.DROP_PIZZA.value)

        return ''.join(actions)
