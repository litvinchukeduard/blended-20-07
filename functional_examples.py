import re
from datetime import datetime

def print_hello():
    print('Hello')

def print_element(element):
    print(element)

def square(element):
    return element ** 2 # element * element

# print_hello()

# other_print_hello = lambda: print('Hello')

# other_print_hello()

# print(list(map(square, [1, 2, 3, 4])))
print(list(map(lambda element: element ** 2, [1, 2, 3, 4])))

'''
Написати функцію, яка буде приймати список з рядків та прибирати з рядка голосні літери
'''

def process_strings(string_list: list[str]) -> list[str]:
    result_list = []
    for element in string_list:
        new_element = re.sub(r'[^aeiou]', '', element)
        result_list.append(new_element)
    return result_list

print(process_strings(['Hello', 'world']))

def process_strings_functional(string_list: list[str]) -> list[str]:
    return list(map(lambda element: re.sub(r'[^aeiou]', '', element), string_list))

print(process_strings_functional(['Hello', 'world']))

'''
Написати функцію, яка буде отримувати список з дат та повертати лише дати, які є цього року
'''

# 1 - Перетворити рядок на число
# 2 - Відсіяти числа не цього року
# 3 - Перетворити числа назад у рядки
def get_dates_this_year(dates: list[str]) -> list[str]:
    datetime_dates = []
    for date in dates:
        datetime_dates.append(datetime.strptime(date, '%Y-%m-%d'))

    # dates_this_year = []
    # for date in dates:
    #     today = datetime.today()
    #     if date.year == today.year:
    #         dates_this_year.append(date)

    dates_this_year = []
    for date in datetime_dates:
        today = datetime.today()
        if date.year != today.year:
            continue
        dates_this_year.append(date)

    string_dates = []
    for date in dates_this_year:
        string_dates.append(datetime.strftime(date, '%Y-%m-%d'))

    return string_dates

# print(get_dates_this_year(['2000-01-01', '2024-01-02', '2025-01-03']))

# def is_date_this_year(date: datetime) -> bool:
#     today = datetime.today()
#     return date.year == today.year

def is_date_this_year(date: datetime) -> bool:
    return date.year == datetime.today().year

def get_dates_this_year_functional(dates: list[str]) -> list[str]:
    # return list(map(lambda date: datetime.strftime(date, '%Y-%m-%d'), \
    #                 filter(lambda date: date.year == datetime.today().year, \
    #                     map(lambda date: datetime.strptime(date, '%Y-%m-%d'), dates))))
    
    # # 1 - Перетворити рядок на число
    datetime_dates = map(lambda date: datetime.strptime(date, '%Y-%m-%d'), dates)

    # # 2 - Відсіяти числа не цього року
    # # filter(is_date_this_year, dates)
    dates_this_year = filter(lambda date: date.year == datetime.today().year, datetime_dates)

    # # 3 - Перетворити числа назад у рядки
    return list(map(lambda date: datetime.strftime(date, '%Y-%m-%d'), dates_this_year))

print(get_dates_this_year_functional(['2000-01-01', '2024-01-02', '2025-01-03']))
