from datetime import datetime
year_now = str(datetime.today().date()).split('-')[0]


def get_dates(dates_list: list) -> list[str]:
    return list(filter(lambda date: date in dates_list if date.split('-')[0] == year_now else None, dates_list))