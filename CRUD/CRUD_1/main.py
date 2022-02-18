from create_1 import create_user
from delete_1 import delete_user
from help_1 import help_crud
from read_1 import user_info, all_users_info
from update_1 import update_parameter, update_user_info

user_emails = []
users_storage = {}
options_list = ['create', 'read', 'update', 'delete', 'quit', 'help']

while True:
    command = input(
        'Please enter commands: "Create", "Read", "Update", "Delete". Enter "Quit" to terminate the session. '
        'Enter "Help" for FAQ.\n')
    command.lower()
    if command == 'create':
        print('You have chosen', command, 'mode.')
        create_user(user_emails, users_storage)

    elif command == 'read':
        print('You have chosen', command, 'mode.')
        read_option = input(
            'Read all users data or Read specified user data? Enter "Read all" or "Read User". Enter "Quit" to '
            'terminate the session\n')
        read_option.lower()
        if read_option == 'read user':
            user_email = input('Enter User Email: ')
            print(user_info(user_email, user_emails, users_storage))
        elif read_option == 'read all':
            all_users = all_users_info(users_storage)
            print(all_users)
        elif read_option == 'quit':
            exit()
        else:
            print('This option is unsupported, please enter correct option.')

    elif command == 'update':
        print('You have chosen', command, 'mode.')
        update_email = input('Enter Email to specify user: ')
        if update_email in user_emails:
            update_option = input('Enter Update option: "Update Parameter" or "Update user data"?')
            update_option.lower()
            if update_option == 'update parameter':
                updated_parameter = update_parameter(update_email, users_storage)
                print('User', update_email, 'new data: \n', updated_parameter)
            elif update_option == 'update user data':
                updated_user_data = update_user_info(update_email, users_storage)
                print('User', update_email, 'new data: \n', updated_user_data, end='\n\n')
        else:
            print('No user with this email found.')

    elif command == 'delete':
        print('You have chosen', command, 'mode.')
        delete_email = input('Enter to specify user: ')
        deleted_user = delete_user(delete_email, user_emails, users_storage)
        print('User', delete_email, 'was deleted from user storage')

    elif command == 'help':
        print('Seems You need some help.')
        help_option = input(
            'Which command do you need help with? Enter one of these: "Create", "Read", "Update", "Delete", "Quit"\n')
        help_option.lower()
        help_result = help_crud(help_option, options_list)
        print(help_result)
    elif command == 'quit':
        exit()
    else:
        print('Unsupported command.')
