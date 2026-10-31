# file: ex_06_06_ordinal_numbers_start.py

# TODO: Write a function ordinal(n: int) -> str
#       Returns the ordinal string for a positive integer
def ordinal(n: int) -> str:
    if n % 100 in (11, 12, 13):
        return f"{n}th"
    elif n % 10 == 1:
        return f"{n}st"
    elif n % 10 == 2:
        return f"{n}nd"
    elif n % 10 == 3:
        return f"{n}rd"
    else:
        return f"{n}th"
#       Rules:
#         n % 100 in (11, 12, 13) -> "th"  (check this FIRST)
#         n % 10 == 1             -> "st"
#         n % 10 == 2             -> "nd"
#         n % 10 == 3             -> "rd"
#         all others              -> "th"
#
#       Return the number and suffix as a string, e.g. "21st"

if __name__ == "__main__":
    # TODO: Print ordinals for 1 to 25 in rows of 10
    #       Example: "1st   2nd   3rd ..."
    for n in range(1, 26):
        print(f"{ordinal(n):<5}", end="")
        if n % 10 == 0:
            print()
    print()
    # TODO: Read a number from the user and print its ordinal
    ord_num = int(input("Skriv et tall: "))
    print(ordinal(ord_num))
