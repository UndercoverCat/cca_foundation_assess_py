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

PRODUCT = Product(id=1, description='guitar', price=250)

ITEM = Item(PRODUCT, 1)

ORDER = Order(
    shipping_address=ADDRESS,
    items=[]
)

ENTRY = Entry(PRODUCT, stock=10)

EMPTY_WAREHOUSE = Warehouse(catalogue=[])
WAREHOUSE = Warehouse(catalogue=[ENTRY])
