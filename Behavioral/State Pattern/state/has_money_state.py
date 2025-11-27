from .machine_state import MachineState
from .dispensing_state import DispensingState
import time

class HasMoneyState(MachineState):
    def select_item(self, context, item_code):
        print("Cannot change item after inserting money")
    
    def insert_coin(self, context, amount):
        print("Money already inserted")
    
    def dispense_item(self, context):
        print(f"Dispensing item: {context.get_selected_item()}")
        context.set_state(DispensingState())

        # Simulate dispensing
        time.sleep(2)
        print("Item dispensed successfully.")
        context.reset()