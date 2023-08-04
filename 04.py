from typing import Literal, Any, Protocol, Sized
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    color: Literal['red', 'blue', 'green']


def draw(p: Point):
    print(p.x, p.y)


p = Point(x=10, y=20, color='red')
draw(p)

@dataclass
class Table:
    price: int
    description: str
    def discount(self, amount: int) -> "Table":
        self.price -= amount
        return self

@dataclass
class Chair:
    price: int
    image_url: str


class HasPrice(Protocol):
    price: int
    def discount(self, amount: int) -> "HasPrice":
        pass



class ShoppingCart:
    products: list[HasPrice]

    def __init__(self):
        self.products = []

    def price(self):
        return sum(p.price for p in self.products)

sp = ShoppingCart()
t1 = Table(price=10, description='a nice table')
c1 = Chair(price=20, image_url='....')

sp.products.append(t1)
sp.products.append(c1)
print(sp.price())




def longer_than(min_len: int, *items: Sized) -> list[Sized]:
    return [i for i in items if len(i) > min_len]


print(longer_than(3, [1, 2, 3], [10, 20, 30, 40], [99, 99, 99, 99, 99, 99]))







