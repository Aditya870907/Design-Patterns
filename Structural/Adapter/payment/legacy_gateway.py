import time
class LegacyGateway:
    def __init__(self):
        self.transaction_reference = None
        self.is_payment_successful_flag = False

    def execute_transaction(self, total_amount, currency):
        print(f"LegacyGateway: Executing transaction for {total_amount} {currency}")
        self.transaction_reference = time.time_ns()
        self.is_payment_successful_flag = True
        print(f"LegacyGateway: Transaction executed successfully. Txn ID: {self.transaction_reference}")
    
    def check_status(self, transaction_reference):
        print(f"LegacyGateway: Checking status for transaction {transaction_reference}")
        return self.is_payment_successful_flag
    
    def get_transaction_reference(self):
        return self.transaction_reference