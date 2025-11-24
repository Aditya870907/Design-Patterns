from strategy.flat_rate_shipping_strategy import FlatRateShipping
from strategy.weight_based_shipping_strategy import WeightBasedShipping
from strategy.distance_based_shipping_strategy import DistanceBasedShipping
from strategy.third_party_api_shipping_strategy import ThirdPartyAPIShipping

from shipping_cost_service import ShippingCostService
from order.order import Order
class ShippingDemo:
    def main():
        order1 = (
                Order.OrderBuilder()
                .set_weight(5)
                .set_distance(10)
                .set_value(100)
                .build()
        )
        
        # Create different shipping instances
        flat_rate = FlatRateShipping(10)
        weight_based = WeightBasedShipping(2)
        distance_based = DistanceBasedShipping(1.5)
        third_party = ThirdPartyAPIShipping(7.5, 0.02)
        
        # Create context with initial strategy
        shipping_service = ShippingCostService(flat_rate)
        
        print("\n--- Order1: Using Flat Rate Shipping Strategy ---")
        shipping_service.calculate_cost(order1)
        
        print("\n--- Order1: Switching to Weight Based Shipping Strategy ---")
        shipping_service.set_strategy(weight_based)
        shipping_service.calculate_cost(order1)
        
        print("\n--- Order1: Switching to Distance Based Shipping Strategy ---")
        shipping_service.set_strategy(distance_based)
        shipping_service.calculate_cost(order1)
        
        print("\n--- Order1: Switching to Third Party API Shipping Strategy ---")
        shipping_service.set_strategy(third_party)
        shipping_service.calculate_cost(order1)
        
         # Adding a NEW strategy is easy:
        # 1. Create a new class implementing ShippingStrategy (e.g., FreeShippingStrategy)
        # 2. Client can then instantiate and use it:
        #    free_shipping = FreeShippingStrategy()
        #    shipping_service.set_strategy(free_shipping)
        #    shipping_service.calculate_shipping_cost(prime_member_order)
        # No modification to ShippingCostService is needed!
        
if __name__ == "__main__":
    ShippingDemo.main()