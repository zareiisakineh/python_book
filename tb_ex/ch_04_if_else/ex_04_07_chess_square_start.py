# file: ex_04_07_chess_square_start.py
column_letter = input("Choose a column letter: (a-h)")
row_num = int(input("Choose a row number: (1-8)"))
character_value = ord(column_letter) - ord('a') +1
if (character_value + row_num) % 2 == 0:
    color = "dark"
else:
    color = "light"
print(f"{column_letter}{row_num} is {color} square")


# TODO: Read the column letter (a-h) and row number (1-8) from the user
# TODO: Convert the column letter to a number 1-8
#       Hint: ord(column) - ord('a') + 1
#             ord() returns the ASCII value of a character (see chapter 3)


# TODO: Determine the color of the square
#       Hint: if (column_num + row) is even -> dark square
#             if (column_num + row) is odd  -> light square
#       Use modulo (%) to check even/odd

# TODO: Print the result
#       Example: "a1 is a dark square."
