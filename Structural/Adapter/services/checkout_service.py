class CheckoutService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor
    
    def checkout(self, amount, currency):
        print(f"CheckoutService: Checking out for {amount} {currency}")
        self.payment_processor.process_payment(amount, currency)
        if self.payment_processor.is_payment_successful():
            print(f"CheckoutService: Payment successful with transaction ID: {self.payment_processor.get_transaction_id()}")
        else:
            print("CheckoutService: Payment failed")