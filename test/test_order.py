import unittest
from unittest import TestCase

from src.address import Address
from src.countries import Country
from src.order import Item, Order
from src.product import Product


class OrderTest(TestCase):
    def test_add_item(self):
        order = Order(
            shipping_address=Address('house', 'street', 'city', 'postcode', Country.UNITED_KINGDOM),
            items=[]
        )
        pen = Item(Product(id=1, description='pen', price=2.5), quantity=1)
        order.add_item(pen)
        self.assertEqual(order.items, [pen])


if __name__ == '__main__':
    unittest.main()
