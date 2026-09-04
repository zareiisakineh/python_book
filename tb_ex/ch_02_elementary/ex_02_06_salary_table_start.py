# file: ex_02_06_salary_table_start.py

# TODO: Read name, age and monthly salary for three people
#       Use int() for age and float() for salary

navn1 = input("Hva heter du? ")
alder1 = int(input("Hvor gammel er du? "))
inntekt1 = float(input("Hvor mye tjener du hver måned? "))

navn2 = input("Hva heter du? ")
alder2 = int(input("Hvor gammel er du? "))
inntekt2 = float(input("Hvor mye tjener du hver måned? "))

navn3 = input("Hva heter du? ")
alder3 = int(input("Hvor gammel er du? "))
inntekt3 = float(input("Hvor mye tjener du hver måned? "))

print(f"{'navn':20}{'alder':6}{'inntekt':>18}")
print(f"{navn1:20}{alder1:6}{inntekt1:>18}")
print(f"{navn2:20}{alder2:6}{inntekt2:>18}")
print(f"{navn3:20}{alder3:6}{inntekt3:>18}")

navn_width = 20
alder_width = 6
inntekt_width = 18

print(f"{'navn':{navn_width}} {'alder':{alder_width}} {'månedintekt':>{inntekt_width}}")
print(f"{navn1:{navn_width}}{alder1:{alder_width}}{inntekt1:{inntekt_width},.2f}")
print(f"{navn2:{navn_width}}{alder2:{alder_width}}{inntekt2:{inntekt_width},.2f}")
print(f"{navn3:{navn_width}}{alder3:{alder_width}}{inntekt3:{inntekt_width},.2f}")

# TODO: Print a header row with three columns: Name, Age, Monthly salary
#       Use f-string field widths to align the columns
#       Hint: text columns default to left-aligned, number columns to right-aligned
#       Example: f"{'Name':20}{'Age':6}{'Monthly salary':18}"

# TODO: Print one row per person using the same field widths
#       Hint: use {salary:18,.2f} for comma-separated salary with 2 decimal places


# --- Part 2 ---
# TODO: Store the field widths in variables:
#       name_width = 20
#       age_width = 6
#       salary_width = 18

# TODO: Rewrite the header and data rows using the width variables
#       instead of hardcoded numbers
#       Hint: f"{name:{name_width}}" uses a variable as the field width

# TODO: Try changing name_width to 25 - does the whole table adjust?
