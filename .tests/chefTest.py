import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame

from src.utils.MenuRender.chefButton import chef_clicked
from src.utils.MenuRender.waiterButton import table_clicked

class TestChefButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.box_rect = pygame.Rect(400, 400, 150, 200)
        self.font = pygame.font.Font(None, 24)

    def test_chef_clicked(self):
        self.assertEqual(chef_clicked(self.screen, self.box_rect, False, self.font), True)

        pygame.mouse.set_pos((450, 450))
        self.assertEqual(chef_clicked(self.screen, self.box_rect, True, self.font), True)

        pygame.mouse.set_pos((0, 0))
        self.assertEqual(chef_clicked(self.screen, self.box_rect, True, self.font), True)

    def test_waiter(self):
        self.assertEqual(table_clicked(self.screen, self.box_rect, False), True)

        pygame.mouse.set_pos((450, 450))
        self.assertEqual(table_clicked(self.screen, self.box_rect, True), True)

        pygame.mouse.set_pos((0, 0))
        self.assertEqual(table_clicked(self.screen, self.box_rect, True), True)

if __name__ == '__main__':
    unittest.main()