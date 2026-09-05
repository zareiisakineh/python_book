# file: ex_04_05_classify_triangle_start.py

# TODO: Read the three side lengths from the user as floats
a = float(input("Gi lengden på side 1: "))
b = float(input("Gi lengden på side 2: "))
c = float(input("Gi lengden på side 3: "))

if a + b > c  and  a + c > b  and  b + c > a:
    if a == b and b == c:
        print("Dette er en Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Dette er en Isosceles triangle")
    else:
        print("Dette er en Scalene triangle")
else:
    print("Dette er IKKE en gyldig triangle")

# TODO: Check if the three sides form a valid triangle
#       A triangle is valid if the sum of any two sides is greater than the third:
#         a + b > c  AND  a + c > b  AND  b + c > a
#       If not valid: print "Not a valid triangle." and stop

# TODO: Classify the triangle:
#       - All three sides equal -> "Equilateral triangle."
#       - Exactly two sides equal -> "Isosceles triangle."
#       - All sides different -> "Scalene triangle."
#
#       Hint: check equilateral before isosceles
