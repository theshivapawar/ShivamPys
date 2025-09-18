from functools import reduce


class Cart:
    items = []

    @staticmethod
    def add_to_cart(desert):
        Cart.items.append(desert)

    @staticmethod
    def clear_cart():
        Cart.items = []

    @staticmethod
    def get_total_cost():
        return reduce(lambda d1, d2 : d1.get_cost() + d2.get_cost(), Cart.items)

    @staticmethod
    def print_invoice():
        for item in Cart.items:
            print(f'{item.__class__.__name__} -- {Cart.get_total_cost()}')

        print(f'Total -- {Cart.get_total_cost()}')
