from house_order_optimization import HouseOrderOptimizationByTraverSal,HouseOrderOptimizationBySort
from action_services import PizzaBotActionService
import sys
from converters import HouseLocationConverter
from decouple import config

if __name__ == '__main__':

    if len(sys.argv) == 2:
        house_location_converter = HouseLocationConverter(
            config('COMMON_PATTERN'),
            config('HOUSE_LOCATION_PATTERN'),
            config('FIELD_SIZE_PATTERN'))
        houses = house_location_converter.get_houses(sys.argv[1])
        order_optimizer = None

        if config('HOUSE_ORDER_OPTIMIZATION_MODE') == 'TreverSal':
            order_optimizer = HouseOrderOptimizationByTraverSal()
        elif config('HOUSE_ORDER_OPTIMIZATION_MODE') == 'Sort':
            order_optimizer = HouseOrderOptimizationBySort()

        optimal_houses_order = order_optimizer.get_optimal_houses_order(houses)
        action_service = PizzaBotActionService()
        actions = action_service.get_actions(optimal_houses_order)
        print(actions)

    else:

        print("Invalid input arguments")
