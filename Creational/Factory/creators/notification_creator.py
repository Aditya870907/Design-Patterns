from abc import ABC, abstractmethod
from products.notification import Notification
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
    
    def send(self, message):
        notification = self.create_notification()
        notification.send(message)