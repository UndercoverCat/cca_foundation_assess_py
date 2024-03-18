import unittest
from unittest import TestCase

from test.fixtures import EMPTY_WAREHOUSE, ENTRY, WAREHOUSE


class WarehouseTest(TestCase):
    def test_initialise_empty_warehouse(self):
        warehouse = EMPTY_WAREHOUSE
        self.assertEqual(warehouse.catalogue, [])

    def test_initialise_warehouse(self):
        entry = ENTRY
        warehouse = WAREHOUSE
        self.assertEqual(warehouse.catalogue, [entry])

    def test_adjust_stock(self):
        warehouse = WAREHOUSE
        guitar = ENTRY.product
        warehouse.adjust_stock(guitar, 5)
        self.assertEqual(warehouse.check_stock(guitar), 15)


if __name__ == '__main__':
    unittest.main()
