from .notification_creator import NotificationCreator
from products.sms_notification import SMSNotification

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()