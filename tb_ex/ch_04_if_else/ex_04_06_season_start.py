# file: ex_04_06_season_start.py

# Season start dates:
#   Spring: March 20
#   Summer: June 21
#   Autumn: September 22
#   Winter: December 21

# TODO: Read month name and day from the user
#       Normalize month with .strip().lower()
måned = input("skriv navnet på måneden: ").strip().lower()
dag = int(input("Hvilken dag i måneden vil du sjekke? "))
# Vår
if (måned == "mars" and dag >= 20) or (måned in ("april", "mai")) or (måned == "juni" and dag < 21): 
    Årstid = "Vår"
elif (måned == "juni" and dag >= 21) or måned in ("juli", "august") or (måned == "september" and dag < 22):
    Årstid = "Sommer"
elif (måned == "September" and dag >= 22) or måned in ("oktober", "november") or (måned == "desember" and dag < 21):
    Årstid = "Høst"
elif (måned == "desember" and dag >= 21) or måned in ("januar", "februar") or (måned == "mars" and dag < 21):
    Årstid = "Vinter"
else:
    årstid = "Ikke gyldig"
print(Årstid)
    
     

# TODO: Determine the season using if-elif-else
#       Each season covers parts of two months at the boundaries,
#       and full months in between.
#
#       Example for Spring:
#         (month == "march" and day >= 20)
#         or month in ("april", "may")
#         or (month == "june" and day < 21)
#
#       Hint: use the same pattern for Summer, Autumn and Winter

# TODO: Print the result
#       Example: "Season: Spring"
