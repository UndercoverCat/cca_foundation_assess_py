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
        pen = ITEM
        order.add_item(pen)
        self.assertEqual(order.items, [pen])


if __name__ == '__main__':
    unittest.main()
