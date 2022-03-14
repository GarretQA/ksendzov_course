import re


def create_user(user_emails, users_storage):
    while True:
        email = input('Enter Email: ')
        if not re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            print('This email is invalid. Please enter valid email.')
            continue
        elif email in user_emails:
            print('User with this email already exists. Please enter another email.')
            continue
        else:
            while True:
                name = input('Enter Name: ')
                if not re.fullmatch(r"[A-Za-z\d\W_]{1,64}", name):
                    print('Enter correct name, please.')
                    continue
                else:
                    break
            while True:
                password = input('Enter Password: ')
                if not re.fullmatch("[A-Za-z\d\W_]{6,64}", password):
                    print('Enter correct password, please.')
                    continue
                else:
                    break
            while True:
                phone = input('Enter Phone: ')
                if not re.fullmatch("^[+][\d]{10,20}", phone):
                    print('Enter correct phone number, please.')
                    continue
                else:
                    break
        break
    user_info = [email, name, password, phone]
    user_emails.append(email)
    users_storage[email] = {'Name': name, 'Password': password, 'Phone': phone}
    print('Created user with following data:', ", ".join(user_info), end='\n\n')
