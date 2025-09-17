def evens_odds_primes(numbers):
    evens = []
    odds = []
    primes = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

        if number == 0 or number == 1:
            continue

        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                break
        else:
            primes.append(number)

    return {'Evens': evens, 'Odds': odds, 'Primes': primes}

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(evens_odds_primes(numbers))