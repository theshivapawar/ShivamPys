from assignment3.InvalidValueException import InvalidValueException


class Console:
    @staticmethod
    def read_number(prompt, min_value, max_value):
        while True:
            number = float(input(f'{prompt}: '))

            if min_value <= number <= max_value:
                return number
            print(f'Enter a number between {min_value} and {max_value}.')
