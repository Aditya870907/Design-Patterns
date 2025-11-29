from abc import ABC, abstractmethod
class TextView(ABC):
    @abstractmethod
    def render(self):
        pass