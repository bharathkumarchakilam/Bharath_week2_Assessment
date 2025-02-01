class Payment:
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of {amount}")

payment_type = input("Enter payment type (CreditCard, PayPal, Bitcoin): ")
amount = float(input("Enter payment amount: "))

if payment_type == "CreditCard":
    payment = CreditCardPayment()
elif payment_type == "PayPal":
    payment = PayPalPayment()
elif payment_type == "Bitcoin":
    payment = BitcoinPayment()
else:
    print("Invalid payment type")
    exit()

payment.process_payment(amount)
