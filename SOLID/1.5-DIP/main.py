class CreditCardPayment:
    def process_credit_card(self, amount: float, card_number: str):
        print(f"Processing credit card payment of ${amount} with card number {card_number}")

class PayPalPayment:
    def process_paypal(self, amount: float, email: str):
        print(f"Processing PayPal payment of ${amount} with email {email}")

class PaymentProcessor:
    def __init__(self):
        self.credit_card_payment = CreditCardPayment()
        self.paypal_payment = PayPalPayment()

    def process_payment(self, method: str, amount: float, details: str):
        if method == "credit_card":
            self.credit_card_payment.process_credit_card(amount, details)
        elif method == "paypal":
            self.paypal_payment.process_paypal(amount, details)
        else:
            raise ValueError("Unsupported payment method")
