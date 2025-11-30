from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, currency):
        raise NotImplementedError
    
    @abstractmethod
    def is_payment_successful(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_transaction_id(self):
        raise NotImplementedError