# file: ex_04_04_days_in_month_start.py

# TODO: Read a month name from the user
#       Normalize with .strip().lower() so any capitalization works
måned = input("Skriv en måned-navn for å få beskjed om hvor mange dager er denne måneden: ")
måned_navn = måned.strip().lower()
# TODO: Use match-case to display the number of days
#       Hint: group months with the same number of days in one branch:
#             case "april" | "june" | "september" | "november":
#       February: display "28 or 29 days"
#       Default case (_): display "Unknown month."
match måned_navn:
    case "april" | "juni" | "september" | "november":
        dager = "30 dager"
    case "januar" | "mars" | "mai" | "juli" | "august" | "oktober" | "desember":
        dager = "31 dager"
    case "februar":
        dager = "28 eller 29 dager"
    case _:
        dager = None
        
if dager:
    print(f"{måned} har {dager}")
else:
    print("ugylidig måned")
         
    

# TODO: Print the result
#       Example: "October has 31 days."
#                "february has 28 or 29 days."
