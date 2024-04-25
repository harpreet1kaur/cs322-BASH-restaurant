from utils.roles.basicClass import BasicClass

class WaiterClass(BasicClass):
    def __init__(self, name, tableStatus, tableNumber, Order, Bill):
        super().__init__(name)
        self.tableStatus = tableStatus
        self.tableNumber = tableNumber
        self.Order = Order
        self.Bill = Bill

    def checkTableStatus(self):
        return self.tableStatus

    def getTableNumber(self):
        return self.tableNumber

    def getOrder(self):
        return self.Order

    def getBill(self):
        return self.Bill

    def setTableStatus(self, status):
        self.tableStatus = status

    def setTableNumber(self, number):
        self.tableNumber = number

    def setOrder(self, order):
        self.Order = order

    def recievePaymentConf(self, payment):
        if (payment == True):
            return True
        else:
            return False
        
    def createOrder(self, order):
        # call order manager 