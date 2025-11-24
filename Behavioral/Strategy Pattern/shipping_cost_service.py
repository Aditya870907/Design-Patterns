from strategy.shipping_strategy import ShippingStrategy
class ShippingCostService:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: ShippingStrategy):
        print(f"ShippingCostService: Strategy changed to {strategy.__class__.__name__}")
        self.strategy = strategy
    
    def calculate_cost(self, order):
        if self.strategy is None:
            raise ValueError("Shipping strategy not set")
        
        cost = self.strategy.calculate_shipping_cost(order)
        print(f"ShippingCostService: Calculated shipping cost is {cost}"
              f" using {self.strategy.__class__.__name__} strategy")
        return cost