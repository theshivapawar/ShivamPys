from functools import reduce

from assignment3.candy import Candy
from assignment3.cart import Cart

cart = Cart()

candy1 = Candy('oreo', 200, 50)
candy2 = Candy('parleg', 200, 50)

cart.add_to_cart(candy1)
cart.add_to_cart(candy2)

print(reduce(lambda a, b : a.get_cost() + b.get_cost(), cart.items))
print(len([]))