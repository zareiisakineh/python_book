# file: ex_02_05_area_and_volume_start.py
import math

# TODO: Read the radius from the user as a float
radius = float(input("Skriv sirkelens radius: "))
areal = math.pi * pow(radius, 2)
print(f"arealen til sirkel med radius {radius} er {areal:.2f} kvadratmeter  ")
# TODO: Calculate the area of a circle: A = pi * r^2
#       Hint: use math.pi and the ** operator

# TODO: Calculate the volume of a sphere: V = (4/3) * pi * r^3
volum = (4 / 3) * math.pi * math.pow(radius, 3)
print(f"volumet til sfæren med radius {radius} er {volum:.2f} kubikkmeter")
# TODO: Print both results formatted to 2 decimal places
#       Example: "The area of the circle is 19.63 square meters."
#                "The volume of the sphere is 65.45 cubic meters."
