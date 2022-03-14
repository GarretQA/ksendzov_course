def user_info(email, user_emails, users_storage):
    if email in user_emails:
        message = 'User email: ' + email, '\nUser info: ', users_storage[email]
    else:
        message = 'No User with this Email found'
    print(*message, end='\n\n')


def all_users_info(users_storage):
    for key, value in users_storage.items():
        message_1 = 'User email: ' + key
        message_2 = 'User Data: ', value
        print(message_1, *message_2, sep='\n', end='\n\n')
    print('All users info was read.')
