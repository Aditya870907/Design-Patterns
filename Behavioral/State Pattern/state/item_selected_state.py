from .machine_state import MachineState
from .has_money_state import HasMoneyState
class ItemSelectedState(MachineState):
    def select_item(self, context, item_code):
        print(f"Item already selected: {context.get_selected_item()}")
    
    def insert_coin(self, context, amount):
        print(f"Inserted {amount} for item: {context.get_selected_item()}")
        context.set_inserted_amount(amount)
        context.set_state(HasMoneyState())
    
    def dispense_item(self, context):
        print("Insert coin before dispensing.")