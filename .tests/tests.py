import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame

from src.utils.MenuRender.chefButton import chef_clicked
from src.utils.MenuRender.waiterButton import table_clicked
from src.components.EmployementManagementSystem import EmployeeManagement
from src.components.MenuManagement import Item, Menu
from src.components.OrderManagement import Order, TableOrder, Orders
from src.components.tablemanagement import TableManagement
from src.components.rolemanagement import Role, Employee, RoleManagementSystem
class TestChefButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.box_rect = pygame.Rect(400, 400, 150, 200)
        self.font = pygame.font.Font(None, 24)
        self.employee_management = EmployeeManagement("Test")
        self.item1 = Item("Chicken", 10.0, 1, 5.0, True)
        self.item2 = Item("Beef", 15.0, 2, 7.5, True)
        self.menu = Menu()
        self.order1 = Order()
        self.order2 = Order()
        self.table_order = TableOrder(1)
        self.orders = Orders()
        self.table_management = TableManagement()
        self.role_management_system = RoleManagementSystem()
        
        
    def test_chef_clicked(self):
        self.assertEqual(chef_clicked(self.screen, self.box_rect, False, self.font), True)

        pygame.mouse.set_pos((450, 450))
        self.assertEqual(chef_clicked(self.screen, self.box_rect, False, self.font), True)

        pygame.mouse.set_pos((0, 0))
        self.assertEqual(chef_clicked(self.screen, self.box_rect, True, self.font), True)

    def test_table_clicked(self):
        self.assertEqual(table_clicked(self.screen, self.box_rect, False), True)

        pygame.mouse.set_pos((450, 450))
        self.assertEqual(table_clicked(self.screen, self.box_rect, False), True)

        pygame.mouse.set_pos((0, 0))
        self.assertEqual(table_clicked(self.screen, self.box_rect, True), True)

    def test_employee_management(self):
        self.employee_management.addUser("test", "password", 1, "role")
        self.assertEqual(self.employee_management.fetch("test", "password"), {'name': 'test', 'password': 'password', 'employee_id': 1, 'role': 'role'})

        self.employee_management.modifyUser("test", "new_role")
        self.assertEqual(self.employee_management.fetch("test", "password"), {'name': 'test', 'password': 'password', 'employee_id': 1, 'role': 'new_role'})

        self.employee_management.removeUser("test")
        self.assertEqual(self.employee_management.fetch("test", "password"), False)

    def test_order(self):
        self.order1.addItem(self.item1)
        self.assertEqual(self.order1.items, [self.item1])
        self.order1.removeItem(self.item1)
        self.assertEqual(self.order1.items, [])

    def test_table_order(self):
        self.table_order.add_order(self.order1)
        self.assertEqual(self.table_order.orders, [self.order1])
        self.table_order.remove_order(self.order1)
        self.assertEqual(self.table_order.orders, [])
        
    def test_item(self):
            self.assertEqual(str(self.item1), "Chicken - $10.00")
            self.item1.update_price(12.0)
            self.assertEqual(self.item1.price, 12.0)
            self.item1.update_cost(6.0)
            self.assertEqual(self.item1.cost, 6.0)
            self.item1.changeStatus(False)
            self.assertEqual(self.item1.status, False)

    def test_menu(self):
        self.menu.add_item(self.item1)
        self.assertEqual(self.menu.items, [self.item1])
        self.menu.add_item(self.item2)

    def test_table_management(self):
        self.table_management.setTableStatus(1, "available")
        self.assertEqual(self.table_management.getTableStatus(1), "available")

        self.table_management.setTableStatus(1, "occupied")
        self.assertEqual(self.table_management.getTableStatus(1), "occupied")

        self.table_management.setTableStaff("Staff 1", 1)
        self.assertEqual(self.table_management.getTableStaff(1), "Staff 1")

        self.table_management.setPartySize(4, 1)
        self.assertEqual(self.table_management.getPartySize(1), 4)
            
    def test_role_management_system(self):
        self.role_management_system.create_role("Chef", ["Order Management", "Menu Management"])
        chef = self.role_management_system.login("chef", "password")
        self.assertEqual(chef.role.name, "Chef")
        self.assertEqual(self.role_management_system.has_permission(chef, "Menu Management"), True)
        self.assertEqual(self.role_management_system.has_permission(chef, "Table Management"), False)
        
if __name__ == '__main__':
    unittest.main()