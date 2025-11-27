from .machine_state import MachineState
from .item_selected_state import ItemSelectedState
class IdleState(MachineState):
    def select_item(self, context, item_code):
        print(f"Item {item_code} selected.")
        context.set_selected_item(item_code)
        context.set_state(ItemSelectedState())
    
    def insert_coin(self, context, amount):
        print("Please select an item before inserting coins.")
    
    def dispense_item(self, context):
        print("No item selected. Cannot dispense item.")