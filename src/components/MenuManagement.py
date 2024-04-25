class Item:
    def __init__(self, name, price, ID, cost, status):
        self.name = name
        self.price = price
        self.ID = ID
        self.cost = cost
        self.status = status

    def update_price(self,price):
        self.price = price
    
    def update_cost(self,cost):
        self.cost = cost

    def changeStatus(self, status):
        self.status = status    

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def  remove_item(self, item):
        self.items.reove(item)

    def substitute(self,old_item, new_item):
        for i, item in enumerate(self.items):
            if item == old_item:
                self.items[i] = new_item
                
    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(item)