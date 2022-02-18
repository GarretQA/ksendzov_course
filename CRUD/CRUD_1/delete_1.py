def delete_user(email, email_list, users_database):
    if email in email_list:
        users_database.pop(email)
        email_list.remove(email)