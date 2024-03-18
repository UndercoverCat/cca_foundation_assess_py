from dataclasses import dataclass

from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


@dataclass
class Warehouse:
    """
    warehouse
        catalogue
            entry
                product
                    id
                    description
                    price
                stock
    """
    catalogue: list[Entry]

    def check_stock(self, product: Product) -> int:
        for entry in self.catalogue:
            if entry.product == product:
                print(f"{entry.product.description} stock = {entry.stock}")
            else:
                print(f"No {entry.product.description} in stock!")
        return next(
            (entry.stock for entry in self.catalogue if entry.product == product),
            0,
        )

    def adjust_stock(self, product: Product, quantity: int):
        for entry in self.catalogue:
            if entry.product == product:
                entry.stock += quantity
                print(f"{entry.product.description} stock = {entry.stock}")
            else:
                print(f"No {entry.product.description} in stock!")

    # def add_entry(self, entry: Entry):
    #     self.catalogue.append(entry)

    # def remove_entry(self, entry: Entry):
    #     self.catalogue.remove(entry)


if __name__ == '__main__':
    guitar = Product(id=1, description='guitar', price=250)
    entry = Entry(guitar, stock=10)
    warehouse = Warehouse(catalogue=[entry])
    warehouse.check_stock(guitar)
    print(f"Stock {guitar.description} = {warehouse.check_stock(guitar)}")
    print(warehouse.check_stock(guitar) == 10)
    print(warehouse.check_stock(Product(id=2, description='piano', price=5000)) == 0)
    warehouse.adjust_stock(guitar, 5)
    print(f"Stock {guitar.description} = {warehouse.check_stock(guitar)}")
