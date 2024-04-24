class TableManagement:
    def __init__(self, total_tables):
        self.tables = {i: 'available' for i in range(1, total_tables+1)}
        self.menu = ""

    def accessTable(self, num):
        if num not in self.tables:
            return "Invalid table number"
        if self.tables[num] == 'available':
            return f"Table {num} is available"
        else:
            return f"Table {num} is occupied"

    def reserveTable(self, num):
        if num not in self.tables:
            return "Invalid table number"
        if self.tables[num] == 'available':
            self.tables[num] = 'occupied'
            return f"Table {num} has been reserved"
        else:
            return f"Table {num} is already occupied"

    def releaseTable(self, num):
        if num not in self.tables:
            return "Invalid table number"
        
        if self.tables[num] == 'occupied':
            self.tables[num] = 'available'
            return f"Table {num} has been released"
        else:
            return f"Table {num} is already available"
