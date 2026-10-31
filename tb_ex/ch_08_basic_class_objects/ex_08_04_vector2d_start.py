# file: ex_08_04_vector2d_start.py
import math

class Vector2D:
    def __init__(self, x, y):
        # TODO: store _x and _y
        self._x = x
        self._y = y

    def __str__(self):
        # TODO: return "Vector2D(x, y)"
        return f"Vector2D{(self._x, self._y)}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        # TODO: return new Vector2D with summed components
        new_x = self._x + other._x
        new_y = self._y + other._y
        return Vector2D(new_x, new_y)

    def __sub__(self, other):
        # TODO: return new Vector2D with subtracted components
        new_x = self._x - other._x
        new_y = self._y - other._y
        return Vector2D(new_x, new_y)

    def __mul__(self, scalar):
        # TODO: return new Vector2D scaled by scalar
        new_x = self._x * scalar
        new_y = self._y * scalar
        return Vector2D(new_x, new_y)

    def __neg__(self):
        # TODO: retuTF  km <rn new Vector2D with negated components
        new_x = self._x * -1
        new_y = self._y * -1
        return Vector2D(new_x, new_y)

    def __abs__(self):
        # TODO: return the magnitude: sqrt(x^2 + y^2)
        return math.sqrt(math.pow(self._x, 2) + math.pow(self._y, 2))

    def __eq__(self, other):
        # TODO: equal if both components are equal
        return self._x == other._x and self._y == other._y

    def dot(self, other):
        # TODO: return dot product: x1*x2 + y1*y2
        return self._x * other._x + self._y * other._y


if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"v1:          {v1}")
    print(f"v2:          {v2}")
    print(f"v1 + v2:     {v1 + v2}")
    print(f"v1 - v2:     {v1 - v2}")
    print(f"v1 * 3:      {v1 * 3}")
    print(f"-v1:         {-v1}")
    print(f"|v1|:        {abs(v1)}")
    print(f"v1.dot(v2):  {v1.dot(v2)}")
    print(f"v1 == v2:    {v1 == v2}")
