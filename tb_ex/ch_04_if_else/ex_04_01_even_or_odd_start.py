# file: ex_04_01_even_or_odd_start.py

# TODO: Read an integer from the user
tall = int(input("Skriv et heltall: "))
# TODO: Use the modulo operator (%) to check if the number is even or odd
#       Hint: a number is even if number % 2 == 0
if tall % 2 == 0:
    print(f"{tall} er partall")
else:
    print(f"{tall} er oddetall")

# TODO: Print the result
#       Example: "42 is even."  or  "17 is odd."
