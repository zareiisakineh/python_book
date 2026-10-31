# file: ex_08_01_rectangle_start.py

class Rectangle:
    def __init__(self, width, height):
        # TODO: store _width and _height
      self._width = width
      self._height = height

    def area(self):
        # TODO: return the area
        return self._width * self._height

    def perimeter(self):
        # TODO: return the perimeter
        return (self._width + self._height) * 2

    def is_square(self):
        # TODO: return whether the rectangle is a square
        return self._width == self._height
             

    def __str__(self):
        # TODO: return e.g. "Rectangle(width=10, height=5)"
        return f"Rekrangel(width={self._width}, height={self._height})"

    def __eq__(self, other):
        # TODO: two rectangles are equal if they have the same area
        return self.area() == other.area()

    def __lt__(self, other):
        # TODO: a rectangle is less than another if its area is smaller
        return self.area() < other.area()


if __name__ == "__main__":
    r1 = Rectangle(10, 5)
    r2 = Rectangle(6, 12)
    r3 = Rectangle(7, 7)

    print(r1)
    print(f"Area:      {r1.area()}")
    print(f"Perimeter: {r1.perimeter()}")
    print(f"Square?    {r1.is_square()}")
    print(f"Square?    {r3.is_square()}")
    print(f"r1 == r2?  {r1 == r2}")
    print(f"r1 < r2?   {r1 < r2}")
    print(f"r1 > r2?   {r1 > r2}")
