from .shipping_strategy import ShippingStrategy
class ThirdPartyAPIShipping(ShippingStrategy):
    def __init__(self, base_fee, percentage_fee):
        self.base_fee = base_fee
        self.percentage_fee = percentage_fee
    
    def calculate_shipping_cost(self, order):
        print(f"Calculation with third party API strategy: base fee {self.base_fee}, percentage fee {self.percentage_fee}")
        return self.base_fee + order.value * self.percentage_fee