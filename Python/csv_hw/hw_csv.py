import csv
import random
import string

import names
import pandas as pd

from random_time_pandas import random_datetimes_or_dates
from user_data_generators import phone_generator, gender_generator, emails_generator, salary_generator, names_generator

file_path = '/Ksendzov_study/Python/csv_txt_files/'

# 1) Создать пустой empty.csv файл
digits_file_csv = 'empty.csv'
empty_csv_create = file_path + digits_file_csv
with open(empty_csv_create, 'w', newline='') as empty_csv:
    writer = csv.writer(empty_csv)

# 2) Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
digits_file_csv = 'digits.csv'
digits_csv_create = file_path + digits_file_csv
with open(digits_csv_create, 'w') as digits_csv:
    for digit in range(151):
        digits_csv.write('%s\n' % digit)

# 3) Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
names_file_csv = 'names.csv'
names_csv_create = file_path + names_file_csv
with open(names_csv_create, 'w') as names_csv:
    for _ in range(100):
        name = names.get_full_name()
        names_csv.write('%s\n' % name)

# 4) Вариант 1. Создать emails.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
emails_file_csv = 'emails.csv'
emails_csv_create = file_path + emails_file_csv
with open(emails_csv_create, 'w') as emails_csv:
    for _ in range(100):
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 64)))
        email = username + '@gmail.com'
        emails_csv.write('%s\n' % email)

# 5) Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк.
#    Имя и часть email до @ должны совпадать.
nne_csv = 'nne.csv'
data_table_csv_create = file_path + nne_csv
with open(data_table_csv_create, 'w', newline='') as table_csv:
    columns = ['Number', 'Name', 'Email']
    writer = csv.DictWriter(table_csv, fieldnames=columns)
    writer.writeheader()
    for i in range(1, 101):
        name_user = names.get_first_name()
        email_username = name_user + '@gmail.com'
        user = {
            'Number': i,
            'Name': name_user,
            'Email': email_username
        }
        writer.writerow(user)

# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк
# с числами от 10 до 310
digits_10_310 = 'digits_10_310.csv'
digits_10_310_create = file_path + digits_10_310
digit_list = [i for i in range(10, 311)]
with open(digits_10_310_create, 'w', newline='') as new_digits_csv:
    column_digit = ['Number']
    writer = csv.DictWriter(new_digits_csv, fieldnames=column_digit)
    writer.writeheader()
    for _ in digit_list:
        new_digits_csv.write('%s\n' % _)

# 7) Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк
#    с разными именами
names_2 = 'names_2.csv'
names_2_create = file_path + names_2
names_list = [names.get_full_name() for _ in range(400)]
with open(names_2_create, 'w', newline='') as new_names_csv:
    column_name = ['Name']
    writer = csv.DictWriter(new_names_csv, fieldnames=column_name)
    writer.writeheader()
    for name in names_list:
        new_names_csv.write('%s\n' % name)

# 8) Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с
#    разными имейлами что-то@gmail.com
emails_2 = 'emails_2.csv'
emails_2_create = file_path + emails_2
email_list = []
for _ in range(400):
    username_for_list = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 64)))
    email_for_list = username_for_list + '@gmail.com'
    email_list.append(email_for_list)
with open(emails_2_create, 'w', newline='') as new_emails_csv:
    column_email = ['Email']
    writer = csv.DictWriter(new_emails_csv, fieldnames=column_email)
    writer.writeheader()
    for email in email_list:
        new_emails_csv.write('%s\n' % email)

# 9) Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк.
#   Имя и часть email до @ должны совпадать.
nne_2_csv = 'nne_2.csv'
nne_2_csv_create = file_path + nne_2_csv
nne_2_list = []
for i in range(1, 451):
    name_user = names.get_first_name()
    email_username = name_user + '@gmail.com'
    user_nne_2 = {
        'Number': i,
        'Name': name_user,
        'Email': email_username
    }
    nne_2_list.append(user_nne_2)
with open(nne_2_csv_create, 'w', newline='') as nne_2:
    writer = csv.DictWriter(nne_2, fieldnames=columns)
    writer.writeheader()
    writer.writerows(nne_2_list)

# 10) Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем.
#     Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)
nne_2_pd = pd.read_csv(nne_2_csv_create)
nne_2_pd["Date"] = ""
nne_2_pd.to_csv(nne_2_csv_create, index=False)
idx1_start = pd.to_datetime('1980-01-01')
idx1_end = pd.to_datetime('1990-12-31')
idx_1 = random_datetimes_or_dates(idx1_start, idx1_end, 50)

idx2_start = pd.to_datetime('1991-01-01')
idx2_end = pd.to_datetime('2000-12-31')
idx_2 = random_datetimes_or_dates(idx2_start, idx2_end, 100)

idx3_start = pd.to_datetime('2001-01-01')
idx3_end = pd.to_datetime('2010-12-31')
idx_3 = random_datetimes_or_dates(idx3_start, idx3_end, 150)

idx4_start = pd.to_datetime('2011-01-01')
idx4_end = pd.to_datetime('2021-12-31')
idx_4 = random_datetimes_or_dates(idx4_start, idx4_end, 150)

combined = idx_1.union(idx_2).union(idx_3).union(idx_4)

nne_2_pd = pd.read_csv(nne_2_csv_create)
nne_2_pd["Date"] = combined
nne_2_pd.to_csv(nne_2_csv_create, index=False)

# 11) Создать файл combo.csv с полями Name, Email, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.
combo_csv = file_path + 'combo.csv'
columns_for_combo = ['Name', 'Email', 'Date', 'Phone', 'Gender', 'Salary']
ini_data_for_combo = []
df = pd.DataFrame(ini_data_for_combo, columns=columns_for_combo)
df.to_csv(combo_csv, index=False)

df = pd.read_csv(combo_csv)
df2 = pd.read_csv(nne_2_csv_create, usecols=['Name', 'Email', 'Date'])

df = df.reindex_like(df2).assign(**{'Name': df2['Name'],
                                    'Email': df2['Email'],
                                    'Date': df2['Date'],
                                    'Phone': None,
                                    'Gender': None,
                                    'Salary': None})
df.to_csv(combo_csv, index=False)

phones_list = phone_generator(450)
gender_list = gender_generator(450)
salary_list = salary_generator(450)
df = pd.read_csv(combo_csv)
df['Phone'] = phones_list
df['Gender'] = gender_list
df['Salary'] = salary_list
df.to_csv(combo_csv, index=False)

add_phones_list = phone_generator(550)
add_gender_list = gender_generator(550)
add_salary_list = salary_generator(550)
add_names_list = names_generator(550)
add_emails_list = emails_generator(550)
add_dates_list = []

dates_add_start = pd.to_datetime('1950-01-01')
dates_add_end = pd.to_datetime('2020-12-31')
df_dates_add = random_datetimes_or_dates(dates_add_start, dates_add_end, 550)

result_list_to_add = [add_names_list, add_emails_list, add_phones_list, add_gender_list,
                      add_salary_list]
df_add = pd.DataFrame(result_list_to_add, index=['Name', 'Email', 'Phone', 'Gender', 'Salary'])
df_add_transposed = df_add.T
df_add_transposed.insert(2, 'Date', df_dates_add)
union = pd.concat([df, df_add_transposed])
union.to_csv(combo_csv, index=False)
