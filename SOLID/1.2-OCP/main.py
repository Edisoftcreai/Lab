class NotificationService:
    def send_notification(self, method: str, message: str):
        if method == "email":
            self.send_email(message)
        else:
            raise ValueError(f"Unsupported notification method: {method}")

    def send_email(self, message: str):
        print(f"Sending email with message: {message}")