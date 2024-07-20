ValueError, IndexError

from datetime import datetime

class BirthdayFormatError(Exception):
    pass

def days_to_birthday(date: str) -> int:
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise BirthdayFormatError("Birthday should be in format %Y-%m-%d")


try:
    days_to_birthday('2000.07.17')
except BirthdayFormatError:
    print('Error')
