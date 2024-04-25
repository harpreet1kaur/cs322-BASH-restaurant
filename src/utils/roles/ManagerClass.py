from utils.roles.basicClass import BasicClass

class ManagerClass(BasicClass):
    def __init__(self, name):
        super().__init__(name)
        
    
    def add_item_to_database(self, specs):
        pass

    def remove_item_from_database(self, specs):
        pass

    def change_item_status(self, item, new_status):
        pass

    def see_hourly_financial_data(self):
        pass

    def see_daily_financial_data(self):
        pass

    def see_hourly_personnel_data(self):
        pass

    def see_daily_personnel_data(self):
        pass

    def modify_data(self):
        pass

    def add_user(self, username, role, password):
        pass

    def delete_user(self, username):
        pass

    def set_role(self, username, role):
        pass

    def get_role(self, username):
        pass