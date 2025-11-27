from .notification import Notification
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")