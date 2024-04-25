

# Define the BusBoy class inheriting from TableManagement
class BusBoy(TableManagement):
    def __init__(self):
        super().__init__()

    def getTableStatus(self, table_number):
        # Access TableManagement to get the status of a table
        return super().getTableStatus(table_number)

    def setTableStatus(self, table_number, status):
        # Access TableManagement to set the status of a table
        super().setTableStatus(table_number, status)
