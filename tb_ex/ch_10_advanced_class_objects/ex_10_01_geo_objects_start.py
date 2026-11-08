# file: ex_10_01_geo_objects_start.py
import math
from abc import ABC, abstractmethod


class GeoObject(ABC):
    def __init__(self, fill_color="none", line_color="black"):
        # TODO: store _fill_color and _line_color
        self._fill_color = fill_color
        self._line_color = line_color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        # TODO: return e.g. "Circle        area=  78.54  perimeter=  31.42  fill=red"
        # Hint: use type(self).__name__ to get the class name
        
        return f"{type(self).__name__:10}    {self.area():.2f}   {self.perimeter():.2f}  {self._fill_color:10} {self._line_color:10}"


class Circle(GeoObject):
    def __init__(self, radius, fill_color="none", line_color="black"):
        # TODO: call super().__init__() and store _radius
        super().__init__(fill_color, line_color)
        self.radius = radius

    @property
    def radius(self):
        # TODO: return _radius
        return self._radius

    @radius.setter
    def radius(self, value):
        # TODO: validate positive, raise ValueError otherwise
        if value < 0:
            raise ValueError("Radius kan ikke være negativ")
        self._radius = value

    def area(self):
        # TODO: pi * r^2
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        # TODO: 2 * pi * r
        return 2 * math.pi * self.radius


class Rectangle(GeoObject):
    def __init__(self, width, height, fill_color="none", line_color="black"):
        # TODO: call super().__init__() and store _width, _height
        super().__init__(fill_color, line_color)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        # TODO: validate positive
        if value < 0:
            raise ValueError("Width kan ikke være negativ")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height kan ikke være negativ")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    shapes = [
        Circle(5, fill_color="red"),
        Rectangle(4, 6),
        Circle(7),
        Rectangle(10, 5, fill_color="blue"),
    ]

    for s in shapes:
        print(s)

    largest = max(shapes, key=lambda s: s.area())
    print(f"\nLargest area: {largest}")
