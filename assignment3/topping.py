class Topping:
    def __init__(self, name, units, price_unit):
        self.name = name
        self.units = units
        self.price_unit = price_unit

    def get_cost(self):
        return self.units * self.price_unit