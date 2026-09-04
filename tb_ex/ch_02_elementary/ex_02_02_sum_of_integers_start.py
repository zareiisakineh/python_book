# file: ex_02_02_sum_of_integers_start.py

# TODO: Read a positive integer n from the user
tall = int(input("Skriv et positivt heltall: "))

# TODO: Calculate the sum using the formula: n * (n + 1) // 2
#       Hint: use // (integer division) to get a whole number result
sum = tall * (tall + 1) // 2

# TODO: Print the result
#       Example: "The sum of all integers from 1 to 10 is 55."
print(f"summen av alle tall fra 1 til {tall} er {sum} ")