from .payment_processor import PaymentProcessor
import time
class InHousePaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.transaction_id = None
        self.is_payment_successful_flag = False

    def process_payment(self, amount, currency):
        print(f"Processing payment of {amount} {currency} using InHousePaymentProcessor")
        self.transaction_id = f"TXN_{int(time.time() * 1000)}"
        self.is_payment_successful_flag = True
        print(f"InHousePaymentProcessor: Payment of {amount} {currency} successful with transaction ID: {self.transaction_id}")
    
    def is_payment_successful(self):
        return self.is_payment_successful_flag
    
    def get_transaction_id(self):
        return self.transaction_id