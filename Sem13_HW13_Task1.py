import warnings

warnings.filterwarnings('ignore')

class NegativeValueError(Exception):
    """Исключение, возникающее при негативных значениях."""

    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value
        super().__init__(f"{attribute.capitalize()} должна быть положительной, а не {value}")

class Rectangle:
    def __init__(self, width, height=None):
        if width < 0:
            raise NegativeValueError("ширина", width)
        if height is not None and height < 0:
            raise NegativeValueError("высота", height)
        self._width = width
        self._height = height if height is not None else width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeValueError("ширина", value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeValueError("высота", value)

        self._height = value

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        new_width = abs(self.width - other.width)
        new_height = abs(self.height - other.height)
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})" 