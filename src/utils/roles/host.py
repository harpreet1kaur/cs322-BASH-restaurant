# Define the Host class inheriting from TableManagement
class Host(TableManagement):
    def __init__(self):
        super().__init__()

    def getTableStatus(self, table_number):
        # Access TableManagement to get the status of a table
        return super().getTableStatus(table_number)

    def setTableStatus(self, table_number, status):
        # Access TableManagement to set the status of a table
        super().setTableStatus(table_number, status)

    def setPartySize(self, party_size, table_number):
        # Access TableManagement to set the party size of a table
        super().setPartySize(party_size, table_number)
