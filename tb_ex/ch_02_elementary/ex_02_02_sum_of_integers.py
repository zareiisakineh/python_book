# file: ex_02_02_sum_of_integers.py

#n = int(input("Enter a positive integer n: "))
#total = n * (n + 1) // 2
#print(f"The sum of all integers from 1 to {n} is {total}.")

# TODO: ask the user for: product, quantity, price per item, decimal places(
product = input("Skriv produktets navn: ")
antall = int(input("Hvor mange av dette produktet skal du kjøpe? "))
pris = float(input("Hva er pris per enhet? "))
desimal = int(input("Hvor mange desimaler? "))
total = pris * antall
print(f"{antall} {product if antall == 1 else product + 's'}{' costs' if antall == 1 else ' cost'}  {pris if {antall} == 1 else total:.{desimal}f}")
# TODO: compute the total cost
# TODO: print a single f-string such as:
#       "3 notebooks cost 37.50 in total."
#       "1 notebook costs 12.50 in total."
#       using conditional expressions for the plural/verb form,
#       and the user's chosen decimal places in the format specifier

