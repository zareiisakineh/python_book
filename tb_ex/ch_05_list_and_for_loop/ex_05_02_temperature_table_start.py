# file: ex_05_02_temperature_table_start.py

# TODO: Print a header row with two columns: "Celsius" and "Fahrenheit"
#       Use f-string field widths to align the columns


# TODO: Loop from 0 to 100 in steps of 10 using range()
#       Hint: range(0, 101, 10)
print(f"{'Celsius':12}{'Fahrenheit':>12}")
for c in range(0, 101, 10):
    f = c * 9 / 5 + 32
    
    print(f"{c}{f:>18}")
    # TODO: Convert Celsius to Fahrenheit: F = C * 9 / 5 + 32

    # TODO: Print one row per temperature with aligned columns
