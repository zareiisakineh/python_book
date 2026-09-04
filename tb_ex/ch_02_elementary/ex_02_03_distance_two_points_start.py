# file: ex_02_03_distance_two_points_start.py
import math

# TODO: Read x1, y1 for point 1 from the user (as floats)
x1 = float(input("Skriv veriden for x1: "))
y1 = float(input("Skriv veriden for y1: "))

# TODO: Read x2, y2 for point 2 from the user (as floats)
x2 = float(input("Skriv veriden for x2: "))
y2 = float(input("Skriv veriden for y2: "))

# TODO: Calculate the distance using the Pythagorean theorem
#       d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#       Hint: use math.sqrt() and ** for squaring
d = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)) 

# TODO: Print the result with 2 decimal places
#       Example: "The distance between the points is 5.00"
print(f"Avstanden mellom puktene du har oppgitt er: {d:.2f}")
