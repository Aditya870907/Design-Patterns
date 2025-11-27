from .notification_creator import NotificationCreator
from products.push_notification import PushNotification

class PushNotificationCreator(NotificationCreator):
    def create_notification(self):
        return PushNotification()