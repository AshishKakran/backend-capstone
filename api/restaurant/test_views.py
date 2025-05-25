from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemViewTests(APITestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title='Pasta', price=12.99, inventory=10)
        self.menu2 = Menu.objects.create(title='Pizza', price=15.99, inventory=5)

    def test_list_menu_items(self):
        url = reverse('menu-list')  # Use the correct basename as registered in your router
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_menu_item(self):
        url = reverse('menu-detail', args=[self.menu1.id])
        response = self.client.get(url)
        serializer = MenuSerializer(self.menu1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
