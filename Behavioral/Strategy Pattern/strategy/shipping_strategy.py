from abc import ABC, abstractmethod
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping_cost(self, order):
        pass