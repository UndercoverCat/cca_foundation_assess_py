import unittest
from unittest import TestCase

from src.warehouse import Warehouse


class WarehouseTest(TestCase):
    def test_initialise_empty_warehouse(self):
        warehouse = Warehouse(catalogue=[])
        self.assertEqual(warehouse.catalogue, [])


if __name__ == '__main__':
    unittest.main()
