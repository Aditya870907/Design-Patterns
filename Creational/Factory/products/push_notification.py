from .notification import Notification
class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification: {message}")