# file: ex_03_01_char_info_start.py

# TODO: Read a single character from the user

# TODO: Use ord() to get the decimal value of the character
tall = ord(input("skriv en karakter"))
# TODO: Print the decimal value
#       Example: "Decimal:     65"
print(f"Decimal: {tall}")
# TODO: Print the binary representation using bin()
#       Example: "Binary:      0b1000001"
print(f"Binary: {bin(tall)}")
# TODO: Print the hexadecimal representation using hex()
#       Example: "Hexadecimal: 0x41"
print(f"Hexadecimal: {hex(tall)}")
# TODO: Use chr() to find the next character (decimal value + 1)
#       and print it
#       Example: "Next character: B"
print(f"Next character is: {chr(tall + 1)}")
