from .notification import Notification
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email notification: {message}")