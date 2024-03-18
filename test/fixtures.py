from src.address import Address
from src.countries import Country
from src.warehouse import Entry, Warehouse
from src.order import Item, Order
from src.product import Product

ADDRESS = Address(
    '173',
    'Stoke Newington Church Street',
    'London',
    'N16 0UL',
    Country.UNITED_KINGDOM
)

GUITAR = Product(id=1, description='guitar', price=250)
PIANO = Product(id=2, description='piano', price=5000)

ITEM = Item(GUITAR, 1)
EXCESS_ITEM = Item(GUITAR, 100)

ORDER = Order(
    shipping_address=ADDRESS,
    items=[]
)

ENTRY = Entry(GUITAR, stock=10)

EMPTY_WAREHOUSE = Warehouse(catalogue=[])
WAREHOUSE = Warehouse(catalogue=[ENTRY])
