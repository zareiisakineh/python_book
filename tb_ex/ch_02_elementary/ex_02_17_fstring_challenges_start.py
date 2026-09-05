# file: ex_02_17_fstring_challenges_start.py

# --- Exercise 1 - Decimal places ---
price = 19.9876
# TODO: use an f-string to print "Price: 19.99" - do not use round()
print(f"Price: {price:.2f}")

# --- Exercise 2 - Field width and alignment ---
# TODO: use an f-string to print "Coffee         42.50"
# product field: 12 characters, price field: 8 characters, right-aligned, 2 decimals
product = "Coffee"
price = 42.5

print(f"{'produkt':12}{'Price':>9}")
print(f"{product:12}{price:>8.2f}")
print("------------------------------------------------------")

# --- Exercise 3 - Thousands separator ---
# TODO: print "Population: 5,834,127" using the , format specifier
# TODO: then print the same number using _ as the separator instead
population = 5834127
print(f"population: {population:,}")
print("--------------------------------------------------------")

# --- Exercise 4 - Percentage ---
# TODO: print "Score: 85.0%" using the percentage format specifier (%)
#       do not multiply by 100 yourself
correct = 17
total = 20
score = correct / total
print(f"Score: {score:.0%}")
print("----------------------------------------------------------")

# --- Exercise 5 - A small table ---
# TODO: print a header line "Name              Score"
# TODO: print name1/score1 and name2/score2 so the columns line up,
#       using field width and alignment (not manually typed spaces)
name1 = "Alice"
score1 = 87.456
name2 = "Christopher"
score2 = 91.2

name_width = 15
score_width = 15
print(f"{'name':{name_width}}{'score':>{score_width}}")
print(f"{name1:{name_width}}{score1:>{score_width}.2f}")
print(f"{name2:{name_width}}{score2:>{score_width}.2f}")
print("------------------------------------------------------------")

# --- Exercise 6 - User-controlled decimal places ---
# TODO: ask the user for a number (value) and a number of decimal places (decimals)
# TODO: print "Result: ..." using a format specifier built from the decimals variable
#       hint: f"{value:.{decimals}f}"
tall = float(input("Skriv et desimal tall: "))
ant_desimal = int(input("Hvor mange desimaler skal tallet ha? "))
print(f"Resultat: {tall:.{ant_desimal}f}")
print("------------------------------------------------------------")

# --- Exercise 7 - Singular or plural? ---
# TODO: use one f-string with a conditional expression to print:
#       "There is 1 apple."   when apples == 1
#       "There are 5 apples." when apples == 5
#       (change the value of apples and re-run to check both cases)
apples = int(input("Hvor mange epler? "))
print(f"There {'is' if apples == 1 else 'are'} {apples} {'apple' if apples == 1 else 'apples'}")
print("--------------------------------------------------------------")

# --- Exercise 8 - Dynamic receipt ---
# TODO: ask the user for: product, quantity, price per item, decimal places(
    # TODO: compute the total cost
# TODO: print a single f-string such as:
#       "3 notebooks cost 37.50 in total."
#       "1 notebook costs 12.50 in total."
#       using conditional expressions for the plural/verb form,
#       and the user's chosen decimal places in the format specifier
product = input("Skriv produktets navn: ")
antall = int(input("Hvor mange av dette produktet skal du kjøpe? "))
pris = float(input("Hva er pris per enhet? "))
desimal = int(input("Hvor mange desimaler? "))
total = pris * antall
print(f"{antall} {product if antall == 1 else product + 's'}  {'costs' if antall == 1 else 'cost'}  {pris if {antall} == 1 else total:.{desimal}f} totalt")
