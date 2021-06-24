import csv

def get_quotes():
    list_of_quotes_formatted = []
    with open("quotes_all.csv") as file:
        data = csv.reader(file, delimiter=';')

        count = 0
        for item in data:
            if (count == 0):
                count += 1
                continue
            list_of_quotes_formatted.append(item[0] + " -" + item[1])
    return list_of_quotes_formatted

# store data to db
