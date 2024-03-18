import unittest
from unittest import TestCase

from src.order import Order
from test.fixtures import ADDRESS, ITEM


class OrderTest(TestCase):
    def test_add_item(self):
        order = Order(
            shipping_address=ADDRESS,
            items=[]
        )
        guitar = ITEM
        order.add_item(guitar)
        self.assertEqual(order.items, [guitar])


if __name__ == '__main__':
    unittest.main()
