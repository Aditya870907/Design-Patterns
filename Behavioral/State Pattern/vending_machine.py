from state.idle_state import IdleState
class VendingMachine:
    def __init__(self):
        self.current_state = IdleState() # Initial State
        self.selected_item = ""
        self.inserted_amount = 0.0
    
    def set_state(self, new_state):
        self.current_state = new_state # Change to new state
    
    def set_selected_item(self, item_code):
        self.selected_item = item_code 
    
    def set_inserted_amount(self, amount):
        self.inserted_amount = amount
    
    def get_selected_item(self):
        return self.selected_item
    
    def select_item(self, item_code):
        self.current_state.select_item(self, item_code)
    
    def insert_coin(self, amount):
        self.current_state.insert_coin(self, amount)
    
    def dispense_item(self):
        self.current_state.dispense_item(self)
    
    def reset(self):
        self.current_state = IdleState()
        self.selected_item = ""
        self.inserted_amount = 0.0