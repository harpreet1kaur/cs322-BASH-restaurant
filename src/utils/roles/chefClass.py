from utils.roles.basicClass import BasicClass

class ChefClass(BasicClass):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

    def cook(self, dish):
        print(f"{self.name} is cooking {dish}.")

    def serve(self, dish):
        print(f"{self.name} is serving {dish}.")


# Import OrderManagement and MenuManagement classes
from orderManagement import OrderManagement
from menuManagement import MenuManagement

# Define the Employee class
class Employee:
    def __init__(self, employee_id, first_name, last_name, password, username):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username

# Define the Chef class inheriting from Employee
class Chef(Employee):
    def __init__(self, employee_id, first_name, last_name, password, username, specialty):
        super().__init__(employee_id, first_name, last_name, password, username)
        self.specialty = specialty

    def changeItemStatus(self, item_id, status):
        # Access MenuManagement to change the status of a menu item
        menu_mgmt = MenuManagement()
        menu_mgmt.change_item_status(item_id, status)

    def setOrderStatus(self, order_id, status):
        # Access OrderManagement to set the status of an order
        order_mgmt = OrderManagement()
        order_mgmt.set_order_status(order_id, status)
