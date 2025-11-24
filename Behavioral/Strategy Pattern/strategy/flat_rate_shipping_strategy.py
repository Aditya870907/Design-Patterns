from .shipping_strategy import ShippingStrategy
class FlatRateShipping(ShippingStrategy):
        def __init__(self, rate):
            self.rate = rate
        
        def calculate_shipping_cost(self, order):
            print(f"Calculation with flat rate strategy: {self.rate}")
            return self.rate