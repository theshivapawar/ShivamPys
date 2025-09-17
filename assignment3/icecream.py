from assignment3.desert import Desert


class IceCream(Desert):
    def __init__(self, name, units, price_unit):
        super().__init__(name)
        self.name = name
        self.units = units
        self.price_unit = price_unit

    def get_cost(self):
        return self.units * self.price_unit