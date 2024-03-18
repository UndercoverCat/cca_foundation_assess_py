import unittest
from unittest import TestCase

from test.fixtures import EXCESS_ITEM, ITEM, ORDER, WAREHOUSE


class OrderTest(TestCase):
    def test_add_item(self):
        order = ORDER
        guitar = ITEM
        order.add_item(guitar)
        self.assertEqual(order.items, [guitar])

    def test_add_item_stock(self):
        warehouse = WAREHOUSE
        order = ORDER
        guitar = ITEM
        order.add_item(guitar)
        self.assertGreaterEqual(warehouse.check_stock(guitar.product), guitar.quantity)

    def test_add_item_no_stock(self):
        warehouse = WAREHOUSE
        order = ORDER
        guitars = EXCESS_ITEM
        order.add_item(guitars)
        self.assertLess(warehouse.check_stock(guitars.product), guitars.quantity)


if __name__ == '__main__':
    unittest.main()
