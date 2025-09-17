from assignment3.candy import Candy
from assignment3.cart import Cart


class Order:
    cart = Cart()

    @staticmethod
    def take_order():
        while True:
            Order.display_menu()
            choice = int(input('Choice: '))

            if choice == 5:
                print('Thank you :)')
                break

            match choice:
                case 1:
                    name = input('Name: ')
                    weight = input('Weight (grams): ')
                    price_kg = input('Price (kg): ')
                    Order.cart.add_to_cart(Candy(name, weight, price_kg))

                case 2:
                    name = input('Name: ')
                    weight = input('Units: ')
                    price_dozen = input('Price (Dozen): ')
                    Order.cart.add_to_cart(Candy(name, weight, price_dozen))

                case 3:
                    name = input('Name: ')
                    weight = input('Units: ')
                    price_unit = input('Price: ')
                    Order.cart.add_to_cart(Candy(name, weight, price_unit))

                case 4:
                    name = input('Name: ')
                    weight = input('Units: ')
                    price_unit = input('Price: ')
                    Order.cart.add_to_cart(Candy(name, weight, price_unit))





    @staticmethod
    def display_menu():
        print(f'\nMenu\n1. Candy\t2. Cookie\t3. IceCream\t4. Sundae\t5. Exit\n')


order = Order()
order.take_order()