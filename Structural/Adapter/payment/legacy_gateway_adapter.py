from .payment_processor import PaymentProcessor
class LegacyGatewayAdapter(PaymentProcessor):
    def __init__(self, legacy_gateway):
        self.legacy_gateway = legacy_gateway
        self.current_ref = None
    
    def process_payment(self, amount, currency):
        print(f"Adapter: Translating process_payment() for {amount} {currency}")
        self.legacy_gateway.execute_transaction(amount, currency)
        self.current_ref = self.legacy_gateway.get_transaction_reference()
    
    def is_payment_successful(self):
        return self.legacy_gateway.check_status(self.current_ref)
    
    def get_transaction_id(self):
        return f"LEGACY_TXN_{self.current_ref}"