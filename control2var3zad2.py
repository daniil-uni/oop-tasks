class Payment:
def __init__(self, amount, currency):
self.__amount = amount 
self._currency = currency 

def get_amount(self):
return self.__amount


class CashPayment(Payment):
def calculate_fee(self):
return 0 

def process_payment(self):
return self.get_amount() * 5


class CardPayment(Payment):
def calculate_fee(self):
return self.get_amount() * 0.02

def process_payment(self):
return self.get_amount() / 5


class OnlinePayment(CashPayment, CardPayment):
def __init__(self, amount, currency):
super().__init__(amount, currency)

def process_payment_from_cash(self):
return CashPayment.process_payment(self)


pay = OnlinePayment(100, "KZT")

result = pay.process_payment_from_cash()
print(f"Результат метода process_payment из CashPayment: {result}")