class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    

def current_date():
    from datetime import date
    today = date.today()

    d1 = today.strftime("%d/%m/%Y") # 16/09/2019
    temp_lst = d1.split("/")

    day = temp_lst[0]
    month = temp_lst[1]
    year = temp_lst[2]

    current_date_object = date(day, month, year)

    return current_date_object
