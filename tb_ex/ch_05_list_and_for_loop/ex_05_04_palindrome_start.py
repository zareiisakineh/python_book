# file: ex_05_04_palindrome_start.py



# --- Part 1: single word palindrome ---

# TODO: Check if the string is a palindrome using slicing
#       Hint: text[::-1] reverses a string
#       Print the result
#       Example: '"racecar" is a palindrome.'
#                '"hello" is not a palindrome.'
ord1 = input("Skriv et ord for å sjekke om det er palindrom: ")
snu_ord1 = ord1[::-1]
if ord1 == snu_ord1:
    print(f"{ord1} er en palindrom")
else:
    print(f"{ord1} er IKKE en palindrom")

# --- Part 2: multi-word palindrome (ignore spaces) ---

# TODO: Remove spaces from the string and convert to lowercase
#       Hint: text.replace(" ", "").lower()

# TODO: Check if the result is a palindrome and print
#       Example: '"never odd or even" is a palindrome (ignoring spaces).'
setning1 = input("Skriv en setning for å sjekke om den er palindrom: ")
renset = setning1.replace(" ", "").lower()
setning2 = renset[::-1]
if renset == setning2:
    print(f"{setning1} er en palindrom")
else:
    print(f"{setning1} er IKKE en palindrom")