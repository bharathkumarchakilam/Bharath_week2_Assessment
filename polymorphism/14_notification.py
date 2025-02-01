class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")

notification_type = input("Enter notification type (Email, SMS): ")

if notification_type == "Email":
    notification = EmailNotification()
elif notification_type == "SMS":
    notification = SMSNotification()
else:
    print("Invalid notification type")
    exit()

notification.send()
