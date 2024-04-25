from utils.roles.basicClass import BasicClass
from utils.roles.basicClass import BasicClass

class ChefClass(BasicClass):
    def __init__(self, name, order, menuItem):
        super().__init__(name)
        self.order = order
        self.menuItem = menuItem

    def get_order(self):
        return self.order

    def set_order(self, order):
        self.order = order

    def get_menuItem(self):
        return self.menuItem
    
    def set_menuItem(self, menuItem):
        self.menuItem = menuItem


