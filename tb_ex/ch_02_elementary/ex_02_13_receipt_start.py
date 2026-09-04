# file: ex_02_13_receipt_start.py
name1 = input("Enter item 1 name: ")
price1 = float(input("Enter item 1 price: "))
name2 = input("Enter item 2 name: ")
price2 = float(input("Enter item 2 price: "))
name3 = input("Enter item 3 name: ")
price3 = float(input("Enter item 3 price: "))

# TODO: compute the total
total_price = price1 + price2 + price3
print(f"{'Product':<15}{'Price':>10}")
print(f"{name1:<15}{price1:>10,.2f}")
print(f"{name2:<15}{price2:>10,.2f}")
print(f"{name3:<15}{price3:>10,.2f}")
print("-----------------------------")
print(f"{'Total':<15}{total_price:>10,.2f}")

# TODO: print each item so the name is left-aligned in a
#   field of width 15 and the price is right-aligned in a
#   field of width 10 with 2 decimals and a thousands
#   separator. Example: f"{name1:<15}{price1:>10,.2f}"

# TODO: print a line of 25 dashes, then a Total line in the
#   same format
