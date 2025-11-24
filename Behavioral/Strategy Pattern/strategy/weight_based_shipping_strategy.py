from .shipping_strategy import ShippingStrategy
class WeightBasedShipping(ShippingStrategy):
    def __init__(self, rate_per_kg):
        self.rate_per_kg = rate_per_kg
    
    def calculate_shipping_cost(self, order):
        print(f"Calculation with weight based strategy: {self.rate_per_kg}/kg")
        return order.weight * self.rate_per_kg