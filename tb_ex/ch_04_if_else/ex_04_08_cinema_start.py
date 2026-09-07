# file: ex_04_08_cinema_start.py

# TODO: Read age, number of tickets, and whether it is an evening screening
#       Hint: normalize the yes/no input with .strip().lower()
alder = int(input("Hvor gammel er du? "))
ant_biletter = int(input("Hvor mange biletter vil du ha? "))
kveld_avgift = input("er forestllingen etter kl 19? yes/no: ").strip().lower()
er_student = input("Er du student? Yes/No: ").strip().lower()

# TODO: Determine category and base price based on age:
#       Child  (under 12):   $8
#       Student (12-25):     $12
#       Adult  (26-66):      $16
#       Senior (67+):        $12
if alder < 12:
    pris = 8
    kategori = "barn"
elif er_student == 'yes'  and 12<= alder <= 25:
        pris = 12
        kategori = "student"
elif alder >= 67:
    pris = 12
    kategori = "senior"
else:
    pris = 16
    kategori = "voksen"
        
# TODO: Add evening surcharge of $3 for adults at evening screenings
#       All other categories: no surcharge
if kveld_avgift == 'yes' and kategori == "voksen":
    pris += 3
# TODO: Calculate subtotal (price per ticket * number of tickets)
subtotal = ant_biletter * pris
# TODO: Apply 10% group discount if 3 or more tickets
if ant_biletter >= 3:
    rabatt = subtotal * 0.1
    total_pris = subtotal - rabatt
else:
    rabatt = 0
    total_pris = subtotal
# TODO: Print the price breakdown
#       Category: ...
#       Price per ticket: $...
#       Number of tickets: ...
#       Subtotal: $...
#       Group discount (10%): -$...    <- only if discount applies
#       Total: $...
print(f"kategori: {kategori} " )
print(f"pris per bilett: {pris}")
print(f"antall biletter: {ant_biletter}")
if rabatt > 0:
    print(f"Din rabatt er: {rabatt}")
print(f"Tota pris er: {total_pris}")
