# file: ex_02_11_date_reformat_start.py

# Read a date in the format YYYY-MM-DD
date = input("Enter a date (YYYY-MM-DD): ")
år = date[:4]
måned = date[5:7]
dag = date[8:]
print(f"{dag}/{måned}/{år}")
# TODO: use slicing to pull out the three parts.
#   The year is the first four characters, then the
#   month, then the day. Do not use split().
#   year  = ...
#   month = ...
#   day   = ...

# TODO: print it in European format DD.MM.YYYY, e.g.
#   In European format: 15.01.2024
