# file: ex_04_03_letter_grade_start.py

# TODO: Read a score (0-100) from the user
karakter = int(input("Skriv tall-karakter: "))
if karakter >= 90:
    print(f"din bogstav-karakter er: A")
elif karakter >= 80:
    print(f"din bogstav-karakter er: B")
elif karakter >= 60:
    print(f"din bogstav-karakter er: C")
elif karakter >= 50:
    print(f"din bogstav-karakter er: D")
elif karakter >= 40:
    print(f"din bogstav-karakter er: E")
else:
    print(f"din bogstav-karakter er: F")
# TODO: Determine the letter grade using if-elif-else:
#       90 or above -> A
#       80 or above -> B
#       60 or above -> C
#       50 or above -> D
#       40 or above -> E
#       below 40   -> F
#
#       Hint: because elif only runs when previous conditions were False,
#             you only need to check the lower bound of each range

# TODO: Print the result
#       Example: "Grade: C"
