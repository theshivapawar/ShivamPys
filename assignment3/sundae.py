from assignment3.desert import Desert
from functools import reduce


class Sundae(Desert):
    def __init__(self, name, units, price_unit, toppings):
        super().__init__(name)
        self.units = units
        self.price_unit = price_unit
        self.toppings = toppings

    def get_cost(self):
        if len(self.toppings) == 0:
            return self.units * self.price_unit

        # toppings_cost = reduce(lambda t1.getCost(), t2,getCost(): t1.get_cost() + t2.get_cost(), self.toppings)
        toppings_cost = map(lambda t : t.get_cost(), self.toppings)
        total_toppings_cost = reduce(lambda c1, c2 : c1 + c2, toppings_cost)
        print(list(toppings_cost))
        return (self.units * self.price_unit) + total_toppings_cost