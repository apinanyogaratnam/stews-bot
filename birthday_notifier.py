from date_object import date_obj, current_date
from replit import db


def dates_equivalent(date1, date2):
    return int(date1.day) == int(date2.day) and int(date1.month) == int(date2.month)


def is_anyones_birthday():
    users = db.keys()
    todays_date = current_date()

    lst_of_birthday_users = []
    for user in users:
        if dates_equivalent(get_birthday(user), todays_date):
            lst_of_birthday_users.append(user)
    
    return lst_of_birthday_users


# needs a threading process (runs every hour)
# def notify_birthdays():
#     import datetime
#     now = datetime.datetime.now()

#     if not now.hour == 9: return 

#     lst_of_birthday_users = is_anyones_birthday()
#     lst_of_messages = []

#     for user in lst_of_birthday_users:
#         message = "Happy Birthday"

#     return message


def is_valid_format(possible_date_string):
    lst = possible_date_string.split("/")

    if len(lst) != 3: return False
    if not lst[0].isdigit() or not lst[1].isdigit() or not lst[2].isdigit(): return False

    day = int(lst[0])
    month = int(lst[1])
    year = int(lst[2])

    if day < 0 or day > 31: return False
    if month < 0 or month > 12: return False
    if year < 0 or year > current_date().year: return False

    return True


def format_string_to_date_object(date_string):
    # date_string is as xx/xx/xxxx
    # (day)/(month)/(year)
    # assuming date_string is a valid date_string
    lst = date_string.split("/")
    str_to_date_obj = date_obj(lst[0], lst[1], lst[2])

    return str_to_date_obj


def add_birthday(username, date_string): # username in discord, date_string
    # if already exists, birthday gets replaced
    db[username] = date_string

    return "Birthday of {} for {} added successfully.".format(date_string, username.display_name)


def get_birthday(username):
    return db[str(username)]


def remove_birthday(username):
    del db[username]


def print_all_users():
    for item in db.keys():
        print(item)
