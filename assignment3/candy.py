from assignment3.desert import Desert

class Candy(Desert):
    KG = 1000

    def __init__(self, name, weight, price_kg):
        super().__init__(name)
        self.weight = weight
        self.price_kg = price_kg

    def get_cost(self):
        return round((self.weight / Candy.KG) * self.price_kg, 2)