from utils.roles.basicClass import BasicClass

class ChefClass(BasicClass):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

    def cook(self, dish):
        print(f"{self.name} is cooking {dish}.")

    def serve(self, dish):
        print(f"{self.name} is serving {dish}.")


