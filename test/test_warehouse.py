import unittest
from unittest import TestCase

from src.warehouse import Warehouse
from test.fixtures import ENTRY


class WarehouseTest(TestCase):
    def test_initialise_empty_warehouse(self):
        warehouse = Warehouse(catalogue=[])
        self.assertEqual(warehouse.catalogue, [])

    def test_initialise_warehouse(self):
        entry = ENTRY
        warehouse = Warehouse(catalogue=[entry])
        self.assertEqual(warehouse.catalogue, [entry])


if __name__ == '__main__':
    unittest.main()
