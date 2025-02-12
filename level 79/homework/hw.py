def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def closest_leap_year(year):
    next_year = year + 1
    prev_year = year - 1

    while not is_leap_year(next_year):
        next_year += 1

    while not is_leap_year(prev_year):
        prev_year -= 1

    if abs(next_year - year) < abs(prev_year - year):
        return next_year
    return prev_year

years = [2100, 2104, 2400]

for year in years:
    if is_leap_year(year):
        print(f"{year} - Yes")
    else:
        print(f"{year} - No, closest leap year: {closest_leap_year(year)}")
