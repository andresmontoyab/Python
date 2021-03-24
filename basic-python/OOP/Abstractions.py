# Abstractions

class Payment:
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("This is the concrete credit card impl")

class DebitPayment(Payment):
    def pay(self):
        print("This is the Debit card impl")

payment = Payment()
payment.pay()

credit_card = CreditCardPayment()
credit_card.pay()

debit_payment = DebitPayment()
debit_payment.pay()

print(isinstance(debit_payment, Payment))