# file: ex_02_04_extract_digits_start.py
import math
# TODO: Read a four-digit integer from the user
tall = int(input("Skriv et 4-siffer tall: "))

# TODO: Extract the digits one by one using % and //
#       Hint: number % 10 gives the last digit
#             number // 10 removes the last digit
#       Do this four times to get all four digits
siffer4= tall % 10
siffer3 = (tall // 10) % 10
siffer2 = (tall // 100) % 10
siffer1 = (tall // 100) // 10
print(f"siffer1: {siffer1} siffer2: {siffer2} siffer3: {siffer3} siffer4: {siffer4}")
print(f"reversert tall er: {siffer4}{siffer3}{siffer2}{siffer1}")

# TODO: Print the digits in reverse order
#       Example: "The number in reverse order is: 8265"
