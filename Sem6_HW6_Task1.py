date_to_prove = '12.5.-2022'

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                return False
            elif (month == 2 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))) and day > 28:
                return False
            elif month == 2 and day > 29:
                return False
            elif year < 1:
                return False
            return True
        else:
            return False
    except ValueError:
        return False


result = is_valid_date(date_to_prove)
print(result)