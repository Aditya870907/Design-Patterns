from .notification_creator import NotificationCreator
from products.email_notification import EmailNotification

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return EmailNotification()