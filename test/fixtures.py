from src.address import Address
from src.countries import Country
from src.warehouse import Entry
from src.order import Item
from src.product import Product

ADDRESS = Address(
    '173',
    'Stoke Newington Church Street',
    'London',
    'N16 0UL',
    Country.UNITED_KINGDOM
)

PRODUCT = Product(id=1, description='guitar', price=250)

ITEM = Item(PRODUCT, 1)

ENTRY = Entry(PRODUCT, stock=10)
