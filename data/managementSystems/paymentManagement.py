#Payment:
# Attributes:
# - Transaction Number: increasing int with every transaction
# - Total: total cost of all the orders
# - Payment Type: Cash,Credit,Debit
# - Status: Confirmed/Failed
# - Reciept: list of items in order with cost and total
# Functins:
# - setTransactionNumber()
# - getTransactionNumber()
# - getTotal(order list)
# - getStatus()
# - setStatus(status)
# - printReciept(order list)
#Data Management:
# - Send bill in the form of XX.XX
# - Send payment type /CREDIT/DEBIT/CASH/
# - Send payment status /CONFIRMED/FAILED/
class Payment:
    transaction_counter = 0  # Class variable to track transaction numbers
    
    def __init__(self, payment_type="Cash"):
        Payment.transaction_counter += 1
        self.transaction_number = Payment.transaction_counter
        self.total = 0
        self.payment_type = payment_type
        self.status = "Confirmed"
        self.receipt = []

    def set_transaction_number(self, transaction_number):
        self.transaction_number = transaction_number

    def get_transaction_number(self):
        return self.transaction_number

    def get_total(self, order_list):
        total = sum(item[1] for item in order_list)
        self.total = total
        return total

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def print_receipt(self, order_list):
        print("Receipt:")
        for item, cost in order_list:
            print(f"{item}: ${cost:.2f}")
        print(f"Total: ${self.total:.2f}")

    def send_bill(self):
        return f"${self.total:.2f}"

    def send_payment_type(self):
        return f"{self.payment_type.upper()}"

    def send_payment_status(self):
        return f"{self.status.upper()}"
