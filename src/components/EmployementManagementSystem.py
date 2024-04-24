class EmployeeManagement:
    def __init__(self, name):
        self.name = name
        self.employees = [] # this ends up being the worker database

    def fetch(self, username, password):
        for employee in self.employees:
            if employee['name'] == username and employee['password'] == password:
                return employee
        return False

    def addUser(self, name, password, employee_id, role):
        new_user = {'name': name, 'password': password, 'employee_id': employee_id, 'role': role}
        self.employees.append(new_user)

    def removeUser(self, name):
        for employee in self.employees:
            if employee['name'] == name:
                self.employees.remove(employee)
                break

    def modifyUser(self, name, role):
        for employee in self.employees:
            if employee['name'] == name:
                employee['role'] = role
                break
