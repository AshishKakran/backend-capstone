from django.test import TestCase
from restaurant.models import Booking, Menu

class MenuTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            Title='Pasta',
            Price=12.99,
            Inventory=10
        )

    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.Title, 'Pasta')
        self.assertEqual(self.menu_item.Price, 12.99)
        self.assertEqual(self.menu_item.Inventory, 10)

    def test_menu_item_str(self):
        self.assertEqual('{} : ${}'.format(self.menu_item.Title, self.menu_item.Price) , 'Pasta : $12.99')