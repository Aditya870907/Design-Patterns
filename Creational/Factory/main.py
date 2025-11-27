from creators.email_creator import EmailNotificationCreator
from creators.sms_creator import SMSNotificationCreator
from creators.push_creator import PushNotificationCreator
class Main:
    def main():
        creator = EmailNotificationCreator()
        creator.send("Hello, this is a test email")

        creator = SMSNotificationCreator()
        creator.send("Hello, this is a test SMS")

        creator = PushNotificationCreator()
        creator.send("Hello, this is a test push notification")

if __name__ == "__main__":
    Main.main()