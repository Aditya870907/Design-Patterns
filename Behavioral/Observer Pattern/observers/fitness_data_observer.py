from abc import ABC, abstractmethod
class FitnessDataObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass