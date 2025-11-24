from .shipping_strategy import ShippingStrategy
class DistanceBasedShipping(ShippingStrategy):
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km
    
    def calculate_shipping_cost(self, order):
        print(f"Calculation with distance based strategy: {self.rate_per_km}/km")
        return order.distance * self.rate_per_km