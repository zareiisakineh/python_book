# file: ex_02_09_sum_of_digits_start.py
number = int(input("Enter an integer with at most three digits: "))
siffer3 = number % 10
siffer2 = (number % 100) // 10
siffer1 = number // 100
summen = siffer1 + siffer2 + siffer3
print
print(f"summen av siffrene er i tallet {number} er: {summen}")
