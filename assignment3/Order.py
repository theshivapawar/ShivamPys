from assignment3.cookie import Cookie
from assignment3.candy import Candy
from assignment3.cart import Cart
from assignment3.icecream import IceCream
from assignment3.sundae import Sundae
from assignment3.topping import Topping


class Order:

    @staticmethod
    def take_order():
        while True:
            Order.display_menu()
            choice = int(input('Choice: '))

            if choice == 5:
                print('Thank you :)')
                Cart.print_invoice()
                break

            match choice:
                case 1:
                    name = input('Name: ')
                    weight = int(input('Weight (grams): '))
                    price_kg = int(input('Price (kg): '))
                    Cart.add_to_cart(Candy(name, weight, price_kg))

                case 2:
                    name = input('Name: ')
                    units = int(input('Units: '))
                    price_dozen = int(input('Price (Dozen): '))
                    Cart.add_to_cart(Cookie(name, units, price_dozen))

                case 3:
                    name = input('Name: ')
                    units = int(input('Units: '))
                    price_unit = int(input('Price: '))
                    Cart.add_to_cart(IceCream(name, units, price_unit))

                case 4:
                    name = input('Name: ')
                    units = int(input('Units: '))
                    price_unit = int(input('Price: '))
                    toppings = []
                    while True:
                        add_topping = input('Add topping? (yes / no): ').lower()
                        if add_topping == 'no':
                            break
                        topping_name = input('Topping Name: ')
                        topping_units = int(input('Topping Units: '))
                        topping_price_unit = int(input('Topping Price: '))
                        toppings.append(Topping(topping_name, topping_units, topping_price_unit))
                    Cart.add_to_cart(Sundae(name, units, price_unit, toppings))



    @staticmethod
    def display_menu():
        print(f'\nMenu\n1. Candy\t2. Cookie\t3. IceCream\t4. Sundae\t5. Exit\n')




order = Order()
order.take_order()
