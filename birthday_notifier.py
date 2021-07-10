from date_object import date, current_date
from replit import db


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
    date_obj = date(lst[0], lst[1], lst[2])
    
    return date_obj


def add_birthday(username, date): # username in discord, date object
    # if already exists, birthday gets replaced
    db[username] = date


def get_birthday(username):
    return db[username]


def remove_birthday(username):
    del db[username]


def print_all_users():
    for item in db.keys():
        print(item)
