import random
import string

import names
import numpy as np


def phone_generator(user_qty):
    phones_list = []
    for _ in range(user_qty):
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)

        last = (str(random.randint(1, 9998)).zfill(4))
        # while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        #     last = (str(random.randint(1, 9998)).zfill(4))
        phone = '{}-{}-{}'.format(first, second, last)
        phones_list.append(phone)
    return phones_list


def gender_generator(user_qty, p=None):
    if not p:
        # default probabilities
        p = (0.49, 0.49, 0.01, 0.01)
    gender = ("M", "F", "O", "")
    return np.random.choice(gender, size=user_qty, p=p)


def salary_generator(user_qty):
    values = np.random.randint(1000, 3000, user_qty)
    return values


def names_generator(user_qty):
    names_list = []
    for _ in range(user_qty):
        name = names.get_full_name()
        names_list.append(name)
    return names_list


def emails_generator(user_qty):
    emails_list = []
    for _ in range(user_qty):
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 64)))
        email = username + '@gmail.com'
        emails_list.append(email)
    return emails_list
