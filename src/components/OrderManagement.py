class Order:
    def __init__ (self):
        self.orderNumber = 0
        self.items = []
        self.status = True

    def setNumber(self, number):
        self.orderNumber = number

    def changeStatus(self, status):
        self.status = status        

    def addItem(self, item):
        if(item.status == True):
            self.items.append(item)
        else:
            print("Item not available")
    
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not in the order")
    
class Orders():
    def __init__(self):
        self.orders = []
        self.completedOrder = []
    
    def getOrder(self, index):
        if (self.orders.__sizeof__ - 1 > index):
            return (self.orders[index])
        else:
            print ("No order")
    
    def addOrder(self,order):
        self.orders.append(order)
        index = self.orders.index(order)
        order.setNumber(index)

    def removeOrder(self, index):
        if (self.orders.__sizeof__ - 1 > index):
            self.orders.pop(index)
            self.update()
        else:
            print ("No order")

    def completeOrder(self, order):
        order.changeStatus(False)
        self.completedOrder.append(order)
        self.orders.remove(order)
        self.update()
        index = self.completedOrder.index(order)
        order.setNumber(index)

    def update(self):
        for order in self.orders:
            index = self.orders.index(order)
            order.setNumber(index)





        

