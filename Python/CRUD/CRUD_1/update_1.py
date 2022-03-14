import re


def update_parameter(email, users_storage):
    user_data = users_storage.get(email)
    while True:
        param = input(
            'What parameter You need to update? Select of "Name", "Password" or "Phone". Enter Save" to update user data or '
            '"Quit" to'
            'terminate the session \n')
        if param == 'Quit':
            exit()
        elif param == 'Save':
            break
        else:
            if param in list(user_data):
                if param == 'Name':
                    value = input('Enter new Name: ')
                    while not re.fullmatch(r"[A-Za-z\d\W_]{1,64}", value):
                        print('Enter correct name.')
                        value = input('Enter new Name: ')
                    user_data[param] = value
                if param == 'Password':
                    value = input('Enter new Password: ')
                    while not re.fullmatch("[A-Za-z\d\W_]{6,64}", value):
                        print('Enter correct Password.')
                        value = input('Enter new Password: ')
                    user_data[param] = value
                if param == 'Phone':
                    value = input('Enter new Phone: ')
                    while not re.fullmatch("^[+][\d]{10,20}", value):
                        print('Enter correct Phone.')
                        value = input('Enter new Phone: ')
                    user_data[param] = value
                other_param = input('Any other parameter needs to be updated? Yes or No please.\n')
                if other_param == 'Yes':
                    continue
                elif other_param == 'No':
                    break
                else:
                    print('No such option found!')
            else:
                print('No such parameter found. Select of "Name", "Password" or "Phone".')
    return user_data


def update_user_info(email, users_storage):
    user_data = users_storage[email]
    for key, value in user_data.items():
        if key == 'Name':
            value = input('Enter new Name: ')
            while not re.fullmatch(r"[A-Za-z\d\W_]{1,64}", value):
                print('Enter correct name.')
                value = input('Enter new Name: ')
            user_data[key] = value
        if key == 'Password':
            value = input('Enter new Password: ')
            while not re.fullmatch("[A-Za-z\d\W_]{6,64}", value):
                print('Enter correct Password.')
                value = input('Enter new Password: ')
            user_data[key] = value
        if key == 'Phone':
            value = input('Enter new Phone: ')
            while not re.fullmatch("^[+][\d]{10,20}", value):
                print('Enter correct Phone.')
                value = input('Enter new Phone: ')
            user_data[key] = value
    return user_data
