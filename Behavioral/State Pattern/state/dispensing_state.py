from .machine_state import MachineState
class DispensingState(MachineState):
    def select_item(self, context, item_code):
        print("Please wait, dispense in progress.")
    
    def insert_coin(self, context, amount):
        print("Please wait, dispense in progress")
    
    def dispense_item(self, context):
        print("Already dispensing. Please wait")