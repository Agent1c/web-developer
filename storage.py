account = []

def request_manu():
    user_input = input('Choose your Option: ')

    if user_input == '1':
        user_input.append(account)
        print(f'You have successfully adden an item: {user_input}')
    else:
        store_items()
request_manu()

def store_items():
    print(f'You Have: {account} items in your Box')