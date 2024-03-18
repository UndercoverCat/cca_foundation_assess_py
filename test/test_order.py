from unittest import TestCase

from src.order import Order


class OrderTest(TestCase):
    def test_add_item(self):
        order = Order()
        order.add_item('pen')
        assert TestCase.assertEqual(order.items, ['pen'])
