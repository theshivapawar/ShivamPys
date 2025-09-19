from assignment3.desert import Desert


class Sundae(Desert):
    def __init__(self, name, units, price_unit, toppings):
        super().__init__(name)
        self.units = units
        self.price_unit = price_unit
        self.toppings = toppings

    def get_cost(self):
        toppings_cost = 0
        for topping in self.toppings:
            toppings_cost += topping.get_cost()

        return (self.units * self.price_unit) + toppings_cost