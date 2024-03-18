from src.address import Address
from src.countries import Country
from src.order import Item
from src.product import Product

ADDRESS = Address(
    '173',
    'Stoke Newington Church Street',
    'London',
    'N16 0UL',
    Country.UNITED_KINGDOM
)

ITEM = Item(Product(id=1, description='pen', price=2.5), quantity=1)
