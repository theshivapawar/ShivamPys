from assignment3.EmptyCartException import EmptyCartException
from assignment3.InvalidValueException import InvalidValueException
from assignment3.console import Console
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
            choice = Console.read_number('Choice', 1, 5)

            if choice == 5:
                print('Thank you :)')
                if Cart.is_empty():
                    raise EmptyCartException()
                Cart.print_invoice()
                break

            match choice:
                case 1:
                    name = input('Name: ')
                    weight = int(Console.read_number('Weight (grams)', 1, 1000))
                    price_kg = int(Console.read_number('Price (kg)', 1, 1000))
                    Cart.add_to_cart(Candy(name, weight, price_kg))

                case 2:
                    name = input('Name: ')
                    units = int(Console.read_number('Units', 1, 1000))
                    price_dozen = int(Console.read_number('Price (Dozen)', 1, 1000))
                    Cart.add_to_cart(Cookie(name, units, price_dozen))

                case 3:
                    name = input('Name: ')
                    units = int(Console.read_number('Units', 1, 1000))
                    price_unit = int(Console.read_number('Price (Unit)', 1, 1000))
                    Cart.add_to_cart(IceCream(name, units, price_unit))

                case 4:
                    name = input('Name: ')
                    units = int(Console.read_number('Units', 1, 1000))
                    price_unit = int(Console.read_number('Price (Unit)', 1, 1000))

                    toppings = []
                    while True:
                        add_topping = input('Add topping? (yes / no): ').lower()
                        if add_topping == 'no':
                            break

                        topping_name = input('Name: ')
                        topping_units = int(Console.read_number('Units', 1, 1000))
                        topping_price_unit = int(Console.read_number('Price (Unit)', 1, 1000))

                        toppings.append(Topping(topping_name, topping_units, topping_price_unit))
                    Cart.add_to_cart(Sundae(name, units, price_unit, toppings))

    @staticmethod
    def display_menu():
        print(f'\nMenu\n1. Candy\t2. Cookie\t3. IceCream\t4. Sundae\t5. Exit\n')




order = Order()
try:
    order.take_order()
except EmptyCartException as e:
    print(e)
except InvalidValueException as e:
    print(e)
except ValueError as e:
    print('Please enter a valid value.')
except Exception as e:
    print(e)