# file: ex_05_03_collatz_start.py
colatz_list = []
# TODO: Read a starting number from the user
tall = int(input("Skriv et nummer for å regne ut Collatz: "))
colatz_list.append(tall)
while tall != 1:
    if tall % 2 == 0:
        tall = tall // 2
    elif tall % 2 == 1:
        tall = tall * 3 + 1
# TODO: Build the Collatz sequence in a list
    colatz_list.append(tall)
# TODO: Print the sequence with " -> " between numbers
print(" -> ".join(str(x) for x in colatz_list))
# TODO: Print the length of the sequence
print(f"Sequence length: {len(colatz_list)}")

# Start with the starting number in the list
#       Use a while loop that continues until the last number is 1:
#         - If the last number is even: next = last // 2
#         - If the last number is odd:  next = last * 3 + 1
#         - Append the next number to the list


#       Hint: " -> ".join(str(x) for x in sequence)


#       Example: "Sequence length: 15"
