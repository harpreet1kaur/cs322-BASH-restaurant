#Table:
# Attributes:
# - Status: Reserved/Ready/Full/Dirty/
# - Number: index from table array
# - StaffAssigned: Employee name or number assigned to table
# - Party Size: integer of number of people
#Functions:
# - getStatus()
# - setStatus(status)
# - getStaffAssigned()
# - setStaffAssigned(staff)
# = getPartySize()
# - setPartySize()
#Data Management:
# When table is updated to active:
# - send date in DD-MM-YYYY,
# - send start time in XX:XX
# - send party size in XX
#When table is updated to inactive:
# - send end time
import os
import random
import datetime

class Table: 
    def __init__(self, number, status="Ready", busboy=None, waiter=None, party_size=0):
        self.number = number
        self.status = status
        self.busboy = busboy
        self.waiter = waiter
        self.party_size = party_size
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
    
    def get_waiter(self):
        return self.waiter
    
    def set_waiter(self, waiter):
        self.waiter = waiter
        
    def get_busboy(self):
       return self.busboy
    
    def set_waiter(self, busboy):
        self.busboy = busboy
        
    def get_party_size(self):
        return self.party_size
    
    def set_party_size(self, size):
        self.party_size = size
      
#Table Manager        
class TableManager:
    def __init__(self, num_tables):
        self.tables = [Table(number) for number in range(1, num_tables + 1)]
        self.staff = self.load_staff_data()
        self.assign_staff_to_tables()
    #Menu Functions
    def menu(self):
        os.system('cls')
        print("Table Manager Menu:")
        print("1. Manage Table")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        os.system('cls')
        if choice == 1:
            table_number = int(input("Enter table number: "))
            table = self.lookup_table(table_number)
            if table:
                os.system('cls')
                print("Table ", table.number, " Menu:")
                print("Status: " + table.get_status())
                print("Waiter: ", table.get_waiter())
                print("Busboy: ", table.get_busboy())
                print("1. Update Status")
                print("2. Manage Staff")
                print("3. Exit")
                choice_b = int(input("Enter your choice: "))
                if choice_b == 1:
                    os.system('cls')
                    self.change_status(table)
                    return True
                elif choice_b == 2:
                    os.system('cls')
                    self.manage_staff(table)
                    return True
                elif choice_b == 3:
                    os.system('cls')
                    print("Exiting...")
                    return True
        elif choice == 2:
            os.system('cls')            
            print("Exiting...")
            return False
        else:
            print("Invalid choice.")

    def lookup_table(self, table_number):
        if 1 <= table_number <= len(self.tables):
            return self.tables[table_number - 1]
        else:
            print("Error: Table not found.")
            return None

    def change_status(self, table):
        print("Table: ", table.number)
        status = table.get_status()
        print("Status: " + status)
        print("Choices: ")
        if status == "Ready":
            print("1. Reserve Table")
            print("2. Fill Table")
            print("3. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                table.set_status("Reserved")                
            elif choice == 2:
                table.set_status("Full")
                self.write_table_data(table)
            elif choice == 3:
                return True
            else:
                print("Invalid choice!")
        elif status == "Reserved":
            print("1. Fill Table")
            print("2. Cancel Reservation")
            print("3. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                table.set_status("Full")
                self.write_table_data(table)
            elif choice == 2:
                table.set_status("Ready")
            elif choice == 3:
                return True
            else:
                print("Invalid choice!")
        elif status == "Full":
            print("1. Dirty Table")
            print("2. Exit")
            choice = 1
            if choice == 1:
                table.set_status("Dirty")
            elif choice == 2:
                return True
            else:
                print("Invalid choice!")
        elif status == "Dirty":
            print("1. Clean Table")
            print("2. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                table.set_status("Ready")
                self.write_table_data(table)
            elif choice == 2:
                return True
            else:
                print("Invalid choice!")
        else:
            print("Table has invalid status.")

        # Return to Table Manager menu
        return True

    def write_table_data(self, table):
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%y")  # Day-Month-Year format with 2-digit year
        start_time = now.strftime("%H:%M")  # Hours:Minutes format

        table_data = f"{date}/{start_time}/"

        if table.get_status() == "Ready":
            end_time = now.strftime("%H:%M")  # Use the same start time as end time for "Ready" status
            table_data += f"{end_time}/"
        else:
            table_data += "XX:XX/"

        # If the table status is changing from Full to Ready or Dirty to Ready, append the end time
        if table.get_status() in ["Ready", "Full", "Dirty"] and table.get_status() != table.status:
            end_time = now.strftime("%H:%M")
            table_data += f"{end_time}/"

        table_data += "\n"

        with open('data/managementSystems/tableDataTest.txt', 'a') as file:
            file.write(table_data)




    #Employee Functions
    def assign_staff_to_tables(self):
        busboys = [(staff_name, staff_info) for staff_name, staff_info in self.staff.items() if staff_info['role'] == 'busboy']
        waiters = [(staff_name, staff_info) for staff_name, staff_info in self.staff.items() if staff_info['role'] == 'waiter']

        num_tables = len(self.tables)
        num_busboys = len(busboys)
        num_waiters = len(waiters)

        busboy_tables = num_tables // num_busboys
        waiter_tables = num_tables // num_waiters

        for i, table in enumerate(self.tables):
            busboy_idx = i % num_busboys
            waiter_idx = i % num_waiters

            busboy, busboy_info = busboys[busboy_idx]
            waiter, waiter_info = waiters[waiter_idx]

            table.busboy = busboy
            table.waiter = waiter
            self.staff[busboy] = busboy_info
            self.staff[waiter] = waiter_info
            self.staff[busboy]['table_assigned'] = str(table.number)
            self.staff[waiter]['table_assigned'] = str(table.number)





    
    def load_staff_data(self):
        staff_data = {}
        with open('data/managementSystems/employees.csv', 'r') as file:
            next(file)
            for line in file:
                last_name, first_name, number, role, table_assigned = line.strip().split(',')
                staff_data[(last_name, first_name)] = {
                    'number': number,
                    'role': role,
                    'table_assigned': table_assigned
                }
        return staff_data

    
    def manage_staff(self, table):
        print("Manage Table Staff: ")
        
        # Display currently assigned staff
        print("Currently Assigned Staff:")
        print("Busboy:", table.busboy)
        print("Waiter:", table.waiter)

        print("All Staff:")
        busboys = [(staff, info) for staff, info in self.staff.items() if info['role'] == 'busboy']
        waiters = [(staff, info) for staff, info in self.staff.items() if info['role'] == 'waiter']
        print("Busboys:")
        for i, (staff, info) in enumerate(busboys, start=1):
            print(f"{i}. {staff[0]}, {staff[1]}")
        print("Waiters:")
        for j, (staff, info) in enumerate(waiters, start=1):
            print(f"{j}. {staff[0]}, {staff[1]}")

        print("1. Reassign Busboy")
        print("2. Reassign Waiter")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Assigning Busboy to Table...")
            # Prompt for busboy selection
            busboy_choice = int(input("Enter the number of the busboy to reassign to Table " + str(table.number) + ":"))

            if 1 <= busboy_choice <= len(busboys):
                chosen_busboy, _ = busboys[busboy_choice - 1]
                if chosen_busboy == table.busboy:
                    print("This busboy is already assigned to this table.")
                else:
                    # Reassign the busboy
                    self.staff[table.busboy]['table_assigned'] = '0'
                    self.staff[chosen_busboy]['table_assigned'] = str(table.number)
                    table.busboy = chosen_busboy
                    print(f"{chosen_busboy[0]}, {chosen_busboy[1]} (busboy) assigned to Table {table.number}")
            else:
                print("Invalid busboy choice!")
        elif choice == 2:
            print("Assigning Waiter to Table...")
            # Prompt for waiter selection
            waiter_choice = int(input("Enter the number of the waiter to reassign to Table " + str(table.number) + ":"))
            if 1 <= waiter_choice <= len(waiters):
                chosen_waiter, _ = waiters[waiter_choice - 1]
                if chosen_waiter == table.waiter:
                    print("This waiter is already assigned to this table.")
                else:
                    # Reassign the waiter
                    self.staff[table.waiter]['table_assigned'] = '0'
                    self.staff[chosen_waiter]['table_assigned'] = str(table.number)
                    table.waiter = chosen_waiter
                    print(f"{chosen_waiter[0]}, {chosen_waiter[1]} (waiter) assigned to Table {table.number}")
            else:
                print("Invalid waiter choice!")
        elif choice == 3:
            print("Exiting...")
            return False
        else:
            print("Invalid choice.")
            return True









