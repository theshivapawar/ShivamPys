class Cart:
    items = []

    @classmethod
    def add_to_cart(cls, desert):
        cls.items.append(desert)

    @classmethod
    def clear_cart(cls):
        cls.items = []

    @classmethod
    def get_total_cost(cls):
        total_cost = 0
        for item in cls.items:
            total_cost += item.get_cost()
        return round(total_cost, 2)


    @classmethod
    def print_invoice(cls):
        for item in cls.items:
            print(f'{item.__class__.__name__} -- {item.get_name()} -- {item.get_cost()}')

        print(f'Total -- {cls.get_total_cost()}')

    @classmethod
    def is_empty(cls):
        if len(cls.items) == 0:
            return True
        return False
