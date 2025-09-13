accounts = {}

def create_account(id, name, balance):
    if id in accounts:
        print('Account already exist.')
        return

    if balance < 0:
        print('Enter a valid balance.')
        return

    account = {
        'name': name,
        'balance': balance
    }

    accounts[id] = account


def withdraw(id, amount):
    if id not in accounts:
        print('Account doest not exist.')
        return

    if amount <= 0:
        print('Enter a valid amount.')
        return

    if accounts[id]['balance'] < amount:
        print('Insufficient Balance')
        return

    accounts[id]['balance'] -= amount
    print(id, 'withdrawn', amount)


def deposit(id, amount):
    if id not in accounts:
        print('Account doest not exist.')
        return

    if amount <= 0:
        print('Enter a valid amount.')
        return

    accounts[id]['balance'] += amount
    print(id, 'deposited', amount)


def transfer(sender_id, receiver_id, amount):
    if sender_id not in accounts:
        print('Sender doest not exist.')
        return

    if receiver_id not in accounts:
        print('Receiver doest not exist.')
        return

    if amount <= 0:
        print('Enter a valid amount.')
        return

    if accounts[sender_id]['balance'] < amount:
        print('Insufficient Balance')
        return

    accounts[sender_id]['balance'] -= amount
    print(sender_id, 'withdrawn', amount)

    accounts[receiver_id]['balance'] += amount
    print(receiver_id, 'deposited', amount)




create_account(101, 'Shivam', 10000)
create_account(102, 'Satyam', 0)

transfer(101, 102, 25000)

print(accounts[102])


