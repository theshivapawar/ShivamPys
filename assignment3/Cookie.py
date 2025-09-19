from assignment3.desert import Desert


class Cookie(Desert):
    DOZEN = 12

    def __init__(self, name, units, price_dozen):
        super().__init__(name)
        self.name = name
        self.units = units
        self.price_dozen = price_dozen

    def get_cost(self):
        return round((self.units / Cookie.DOZEN) * self.price_dozen, 2)
