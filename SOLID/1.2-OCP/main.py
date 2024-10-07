from abc import ABC, abstractmethod

#Abstract class for notification methods
class NotificationInterface(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

#Class for email notifications
class EmailNotification(NotificationInterface):
    def send(self, message: str):
        print(f"Sending email with message: {message}")

#Class for SMS notifications
class SMSNotification(NotificationInterface):
    def send(self, message: str):
        print(f"Sending SMS with message: {message}")

#Service for sending notifications
class NotificationService:
    def __init__(self, notification: NotificationInterface):
        self.notification = notification

    def send_notification(self, message: str):
        self.notification.send(message)