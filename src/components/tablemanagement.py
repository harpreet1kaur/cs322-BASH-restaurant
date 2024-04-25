# Define the TableManagement class
class TableManagement:
    def __init__(self):
        # Initialize table statuses
        self.table_status = {}

        # Initialize table staff assignments
        self.table_staff = {}

        # Initialize party sizes
        self.party_sizes = {}

    def setTableStatus(self, table_number, status):
        # Set the status of the specified table
        self.table_status[table_number] = status
        print(f"Table {table_number} status set to {status}")

    def getTableStatus(self, table_number):
        # Return the status of the specified table
        return self.table_status.get(table_number, "Table not found")

    def getTableStaff(self, table_number):
        # Return the staff assigned to the specified table
        return self.table_staff.get(table_number, "No staff assigned")

    def setTableStaff(self, staff_assigned, table_number):
        # Set the staff assigned to the specified table
        self.table_staff[table_number] = staff_assigned
        print(f"Staff {staff_assigned} assigned to table {table_number}")

    def getPartySize(self, table_number):
        # Return the party size of the specified table
        return self.party_sizes.get(table_number, "Party size not specified")

    def setPartySize(self, party_size, table_number):
        # Set the party size of the specified table
        self.party_sizes[table_number] = party_size
        print(f"Party size set to {party_size} for table {table_number}")
