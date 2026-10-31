# file: ex_06_02_magic_dates_start.py

# TODO: Write a function is_magic_date(day: int, month: int, year: int) -> bool
#       A magic date is one where day * month == the last two digits of year
#       Hint: year % 100 gives the last two digits
def is_magic_date(day: int, month: int, year: int) -> bool:
    if day * month == year % 100:
        return True
    else:
        return False

# TODO: Use if __name__ == "__main__" to guard the main program
#       In the main program:
#         - Use nested loops to iterate over all years (1900-1999),
#           months (1-12) and days (1-31)
if __name__ == "__main__":
    print("Magic dates in the 20th century:")
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
#         - Call is_magic_date() for each combination
                if is_magic_date(day, month, year):
#         - Print magic dates in the format DD/MM/YYYY
                    print(f"{day:02d}/{month:02d}/{year}")
               
               


#           Example: "01/01/1901"
