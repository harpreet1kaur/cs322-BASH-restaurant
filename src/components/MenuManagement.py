class Item:
    #constructor
    def __init__(self, name, price, ID, cost, status):
        self.name = name
        self.price = price
        self.ID = ID
        self.cost = cost
        self.status = status

    #update the new price
    def update_price(self,price):
        self.price = price
    
    #update the cost
    def update_cost(self,cost):
        self.cost = cost

    #change the status(available or not)
    def changeStatus(self, status):
        self.status = status    

    #convert to string
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Menu:
    #constructor
    def __init__(self):
        self.items = []

    #add item to the menu
    def add_item(self, item):
        self.items.append(item)
    
    #remove item from the menu
    def  remove_item(self, item):
        self.items.reove(item)

    #subtitue one item with another
    def substitute(self,old_item, new_item):
        for i, item in enumerate(self.items):
            if item == old_item:
                self.items[i] = new_item
                
    #display the menu
    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(item)
