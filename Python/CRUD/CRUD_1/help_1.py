def help_crud(help_option, options_list):
    help_option.lower()
    if help_option not in options_list:
        print('Rocket Science, yeaahhh!')

    else:
        match help_option:
            case 'create':
                print(
                    'This mode allows You to create a new user.\n Fields requirements:\n'
                    'Name: from 1 to 64 symbols, A-z, a-z, digits, chars, space.\n'
                    'Email: RFC 5322 standard. This is a unique parameter.\n'
                    'Password: from 6 to 64 symbols, A-z, a-z, digits, chars.\n'
                    'Phone: from 10 to 20 digits, + before digits.')
            case 'read':
                print('This mode allows You to read info about the users that registered before.')
                read_option = input('Pls choose "Read user" or "Read all": ')
                read_option.lower()
                if read_option == 'read user':
                    print('This option allows You to read data abt specified user by searching via email.')
                elif read_option == 'read all':
                    print('This option allows You to read data abt all users in database.')
                else:
                    print('No such read mode option')
            case 'update':
                print('This mode allows You to update info about the users that registered before.')
                update_option = input('Pls choose "Update parameter" or "Update user data": ')
                update_option.lower()
                if update_option == 'update parameter':
                    print('This option allows You to Update any parameter of specified user by searching via email.')
                elif update_option == 'update user data':
                    print('This option allows You to Update all parameters of specified user by searching via email.')
                else:
                    print('No such update mode option')
            case 'delete':
                print('This mode allows You to delete info about the users that registered before.')
            case 'quit':
                print('This command terminates session.')
            case _:
                print('"You are a dumb')
