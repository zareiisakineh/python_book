# file: ex_06_05_format_list_start.py

# TODO: Write a function format_list(items: list) -> str
#       Returns a human-readable string from a list of items:
#         []                              -> ""
#         ["apple"]                       -> "apple"
#         ["apple", "banana"]             -> "apple and banana"
#         ["apple", "banana", "cherry"]   -> "apple, banana and cherry"
#
#       Hint for the general case (3+ items):
#         all items except the last are joined with commas,
#         and the last one is attached with "and"


def format_list(items: list) -> str:
        if len(items) == 0:
            return ("[]")
        elif len(items) == 1:
            return (items[0])
        elif len(items) == 2:
            return (" and ". join(items))
        else:
           # return ", ". join(items[:-1]) + " and " + items[-1]
           return ", ".join(items[:-1]) + f" and " + items[-1]
  


if __name__ == "__main__":
    # Test your function with these cases:
    print(format_list([]))
    print(format_list(["apple"]))
    print(format_list(["apple", "banana"]))
    print(format_list(["apple", "banana", "cherry"]))
    print(format_list(["a", "b", "c", "d"]))

    # TODO (extension): Add a parameter conjunction="and" with a default value
    #   so the caller can write format_list(items, "or")
    def format_list(items: list, conjunction="og") -> str:
        if len(items) == 0:
            return ("[]")
        elif len(items) == 1:
            return (items[0])
        elif len(items) == 2:
            return (" og ". join(items))
        else:
           # return ", ". join(items[:-1]) + " and " + items[-1]
           return ", ".join(items[:-1]) + f" {conjunction} " + items[-1]
    
    print(format_list([]))
    print(format_list(["eple"]))
    print(format_list(["eple", "banan"]))
    print(format_list(["eple", "banan", "jordbær"]))
    print(format_list(["a", "b", "c", "d"]))