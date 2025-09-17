from assignment3.desert import Desert
from functools import reduce


class Sundae(Desert):
    def __init__(self, name, units, price_unit, toppings):
        super().__init__(name)
        self.units = units
        self.price_unit = price_unit
        self.toppings = toppings

    def get_cost(self):
        toppings_cost = reduce(lambda t1, t2: t1.get_cost() + t2.get_cost(), self.toppings)
        return (self.units * self.price_unit) + toppings_cost