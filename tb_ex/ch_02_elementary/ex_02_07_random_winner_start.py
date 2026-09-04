# file: ex_02_07_random_winner_start.py
import random

# TODO: Ask the user to enter participant names separated by spaces
#       Hint: use .split() to turn the input string into a list of names
deltakere = input("Skriv navnet til 5 personer, det må være mellomrom mellm navnene: ").split()

# TODO: Use random.choice() to select a random winner from the list
vinner = random.choice(deltakere)

# TODO: Print the winner's name
print(f"vinneren er: {vinner}")
