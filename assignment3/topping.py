class Topping:
    def __init__(self, units, price_unit):
        self.units = units
        self.price_unit = price_unit

    def get_cost(self):
        return self.units * self.price_unit