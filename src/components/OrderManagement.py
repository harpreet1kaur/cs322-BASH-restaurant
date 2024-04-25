class Order:
    #constructor
    def __init__ (self):
        #a number will be assigned later on in Orders
        self.orderNumber = 0
        #a list to store item in an order
        self.items = []
        #a boolean status with true being the order haven't finish
        self.status = True

    #set number status
    def setNumber(self, number):
        self.orderNumber = number
    #set status
    def changeStatus(self, status):
        self.status = status        
    #add item into the order
    def addItem(self, item):
        #if the order status is true, add it to the order
        if(item.status == True):
            self.items.append(item)
        else:
            print("Order not available")
            
    #remove item from an order
    def removeItem(self, item):
        #if the order exists, remove the item
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not in the order")
    
#class to manage order
class Orders():
    #constructor
    def __init__(self):
        self.orders = []
        self.completedOrder = []

    #get the order with the given index from the order system
    def getOrder(self, index):
        if (self.orders.__sizeof__ - 1 > index):
            return (self.orders[index])
        else:
            print ("No order")
    #add new order into the system
    def addOrder(self,order):
        self.orders.append(order)
        #use the index of the order as an identifier
        index = self.orders.index(order)
        order.setNumber(index)

    #remove the order from the system
    def removeOrder(self, index):
        if (self.orders.__sizeof__ - 1 > index):
            self.orders.pop(index)
             #update the system   
            self.update()
        else:
            print ("No order")

    #move the completed orders into another list for data analysis 
    def completeOrder(self, order):
        #mark the order as complete
        order.changeStatus(False)
        #move to another list
        self.completedOrder.append(order)
        #remove from the active list
        self.orders.remove(order)
        #update
        self.update()
        #update the identifier
        index = self.completedOrder.index(order)
        order.setNumber(index)

    #Method to update the order number of all active orders
    def update(self):
        for order in self.orders:
            index = self.orders.index(order)
            order.setNumber(index)





        

