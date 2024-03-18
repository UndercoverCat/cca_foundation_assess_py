import unittest
from unittest import TestCase

from test.fixtures import ITEM, ORDER


class OrderTest(TestCase):
    def test_add_item(self):
        order = ORDER
        guitar = ITEM
        order.add_item(guitar)
        self.assertEqual(order.items, [guitar])


if __name__ == '__main__':
    unittest.main()
