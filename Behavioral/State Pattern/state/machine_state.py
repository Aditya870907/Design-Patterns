from abc import ABC, abstractmethod
class MachineState(ABC):
    @abstractmethod
    def select_item(self, context, item_code):
        pass
    
    @abstractmethod
    def insert_coin(self, context, amount):
        pass
    
    @abstractmethod
    def dispense_item(self, context):
        pass