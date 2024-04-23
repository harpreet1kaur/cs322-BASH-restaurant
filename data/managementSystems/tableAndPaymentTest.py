from tableManagement import Table
from tableManagement import TableManager
from paymentManagement import Payment


#TABLES
table1 = Table(1)
print("Table 1 Status:", table1.get_status())  # Output: Ready

# Set the status of the table
table1.set_status("Reserved")
print("Table 1 Status:", table1.get_status())  # Output: Reserved

# Assign staff to the table
table1.set_waiter("Doe, John, 123, Waiter")
print("Waiter Assigned to Table 1:", table1.get_waiter())  # Output: Doe, John, 123, Waiter

# Set party size
table1.set_party_size(4)
print("Party Size for Table 1:", table1.get_party_size())  # Output: 4


#PAYMENT

# Create a payment transaction with cash payment type
payment1 = Payment(payment_type="Cash")


# Define a list of items with their costs
order_list = [("Item1", 10.99), ("Item2", 5.50), ("Item3", 7.25)]

# Calculate the total cost and print the receipt
total_cost = payment1.get_total(order_list)
payment1.print_receipt(order_list)

# Send the bill and payment type
print("Bill:", payment1.send_bill())  # Output: Bill: $23.74
print("Payment Type:", payment1.send_payment_type())  # Output: Payment Type: /CASH/


# Set payment status to confirmed
payment1.set_status("Confirmed")

# Send payment status
print("Payment Status:", payment1.send_payment_status())  # Output: Payment Status: /CONFIRMED/


# Get the transaction number
print("Transaction Number:", payment1.get_transaction_number())  # Output: Transaction Number: 1

#Should work as intended, I will probably have to edit once i can see the other classes.

#MANAGERS

#Table Manager:
num_tables = int(input("Enter the number of tables: "))
manager = TableManager(num_tables)
check = True
while check == True:
    check = manager.menu()
    
    #Current Bugs:
    # - When writing to file for data logging, it is writing the date and time as follows:
    #       23-04-24/16:02/XX:XX/
    #       23-04-24/16:03/16:03/
    #   When it should be: 
    #       23-04-24/16:02/16:03/
    # - Have not done edge case work yet so if a menu input is not matching a valid one, crash occurs.