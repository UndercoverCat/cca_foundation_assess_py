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


if __name__ == '__main__':
    unittest.main()
