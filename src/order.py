from dataclasses import dataclass

from address import Address
from product import Product


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    shipping_address: Address
    items: list[Item]

    def add_item(self, item: Item):
        self.items.append(item)
