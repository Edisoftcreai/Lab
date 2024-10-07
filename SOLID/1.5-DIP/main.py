from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CreditCardPayment(PaymentInterface):
    def __init__(self, card_number: str) -> None:
        self.card_number = card_number

    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount} with card number {self.card_number}")

class PayPalPayment(PaymentInterface):
    def __init__(self, email: str) -> None:
        self.email = email

    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount} with email {self.email}")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentInterface) -> None:
        self.payment_method = payment_method

    def process_payment(self, amount: float):
        self.payment_method.process_payment(amount)

