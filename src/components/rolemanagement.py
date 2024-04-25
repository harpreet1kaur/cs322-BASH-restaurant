class Role:
    def __init__(self, name, permissions=None):
        self.name = name
        self.permissions = permissions or []

    def add_permission(self, system_name):
        self.permissions.append(system_name)

    def has_permission(self, system_name):
        return system_name in self.permissions

class RoleManagementSystem:
    def __init__(self):
        self.roles = {}

    def create_role(self, name, permissions=None):
        role = Role(name, permissions)
        self.roles[name] = role

    def assign_role(self, employee, role_name):
        if role_name in self.roles:
            employee.role = self.roles[role_name]
            print(f"Role '{role_name}' assigned to {employee.username}")
        else:
            print(f"Role '{role_name}' does not exist.")

    def get_role(self, employee):
        return employee.role

    def has_permission(self, employee, system_name):
        if employee.role:
            return employee.role.has_permission(system_name)
        return False

    def login(self, username, password):
        # Here, you would typically have some authentication logic
        # For simplicity, this example just checks hardcoded credentials
        if username == "chef" and password == "password":
            employee = Employee(username, password)
            employee.role = self.roles["Chef"]  # Default role
            return employee
        elif username == "busboy" and password == "password":
            employee = Employee(username, password)
            employee.role = self.roles["Busboy"]  # Default role
            return employee
        elif username == "waiter" and password == "password":
            employee = Employee(username, password)
            employee.role = self.roles["Waiter"]  # Default role
            return employee
        elif username == "host" and password == "password":
            employee = Employee(username, password)
            employee.role = self.roles["Host"]  # Default role
            return employee
        elif username == "manager" and password == "password":
            employee = Employee(username, password)
            employee.role = self.roles["Manager"]  # Default role
            return employee
        elif username == "developer" and password == "password":
            employee = Employee(username, password)
            employee.role = self.roles["Developer"]  # Default role
            return employee
        else:
            print("Invalid credentials.")
            return None

class Employee:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = None

# Usage
role_system = RoleManagementSystem()

# Create roles with respective permissions
role_system.create_role("Chef", ["Order Management", "Menu Management"])
role_system.create_role("Busboy", ["Table Management"])
role_system.create_role("Waiter", ["Order Management", "Table Management", "Payment Management"])
role_system.create_role("Host", ["Table Management"])
role_system.create_role("Manager", ["All Management Systems"])
role_system.create_role("Developer", ["All Management Systems"])

# Create employees
chef = role_system.login("chef", "password")  # Chef
busboy = role_system.login("busboy", "password")  # Busboy
waiter = role_system.login("waiter", "password")  # Waiter
host = role_system.login("host", "password")  # Host
manager = role_system.login("manager", "password")  # Manager
developer = role_system.login("developer", "password")  # Developer

# Assign roles
role_system.assign_role(chef, "Chef")
role_system.assign_role(busboy, "Busboy")
role_system.assign_role(waiter, "Waiter")
role_system.assign_role(host, "Host")
role_system.assign_role(manager, "Manager")
role_system.assign_role(developer, "Developer")

# Check permissions
print(role_system.has_permission(chef, "Menu Management"))  # True
print(role_system.has_permission(busboy, "Patron Interaction"))  # False
print(role_system.has_permission(developer, "Kitchen Management"))  # True

# Get employee roles
print(role_system.get_role(chef).name)  # Chef
print(role_system.get_role(busboy).name)  # Busboy
print(role_system.get_role(developer).name)  # Developer



