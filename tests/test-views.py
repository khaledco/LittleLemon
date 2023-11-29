from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
            self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
            self.item2 = Menu.objects.create(title="Meat", price=90, inventory=150)
    
    def test_getall(self):
        response = self.client.get(reverse('menu_items'))
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
        
        
    
