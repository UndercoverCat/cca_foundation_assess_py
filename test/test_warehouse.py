import unittest
from unittest import TestCase

from src.product import Product
from src.warehouse import Entry, Warehouse


class WarehouseTest(TestCase):
    def test_initialise_empty_warehouse(self):
        warehouse = Warehouse(catalogue=[])
        self.assertEqual(warehouse.catalogue, [])

    def test_initialise_warehouse(self):
        entry = Entry(Product(id=1, description='pen', price=2.5), stock=10)
        warehouse = Warehouse(catalogue=[entry])
        self.assertEqual(warehouse.catalogue, [entry])


if __name__ == '__main__':
    unittest.main()
