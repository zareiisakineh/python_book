# file: ex_06_04_geometry_calculator_start.py
import math

# TODO1: Write rectangle(width: float, height: float) -> tuple
#       Returns (area, perimeter)
def rectangle(width: float, height: float) -> tuple:
    rectangle_areal = width * height
    rectangle_omkrets = 2 * width + 2 * height
    return (rectangle_areal, rectangle_omkrets)

# TODO2: Write circle(radius: float) -> tuple
#       Returns (area, perimeter)
#       Use math.pi
def circle(radius: float) -> tuple:
    sirkel_areal = math.pi * pow(radius, 2)
    sirkel_omkrets =  2 * math.pi * radius
    return (sirkel_areal, sirkel_omkrets)


# TODO3: Write right_triangle(a: float, b: float) -> tuple
#       Returns (area, perimeter)
#       Hint: hypotenuse = math.sqrt(a**2 + b**2)
def right_triangle(a: float, b: float) -> tuple:
    hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
    triangle_areal = (a * b) / 2
    tiangle_omkrets = a + b + hypotenuse
    return (triangle_areal, tiangle_omkrets)

if __name__ == "__main__":
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Right triangle")
    choice = input("Your choice: ")
    
    if choice == "1":
        bredde = float(input("Skriv bredden på rektanglet"))
        lengde = float(input("Skriv lengden på rektanglet"))
        rektangel_areal, rektangel_omkrets = rectangle(bredde, lengde)
        print(f"Rektangel-arealet er: {rektangel_areal:.2f}")
        print(f"Rektangel-omkrets er: {rektangel_omkrets:.2f}")
        
    elif choice == "2":
        radius = float(input("Skriv radiusen til sirkelen"))
        sirkel_areal, sirkel_omkrets = circle(radius)
        print(f"arealet til sirkelen er: {sirkel_areal:.2f}")
        print(f"omkretsen er: {sirkel_omkrets:.2f}")
        
    elif choice == "3":
        a = float(input("Skriv a"))
        b = float(input("Skriv b"))
        trekant_areal, trekant_omkrets = right_triangle(a, b)
        print(f"arealet til trekanten er: {trekant_areal:.2f}")
        print(f"omkretsen er: {trekant_omkrets:.2f}")

    # TODO: Use match-case (or if-elif) to read the right dimensions
    #       and call the correct function
    #       Unpack the returned tuple: area, perimeter = function(...)
    #       Print area and perimeter formatted to 2 decimal places
