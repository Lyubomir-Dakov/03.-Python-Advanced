from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return (self.width * self.height) / 2


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total_area = 0
        for shape in self.shapes:
            total_area += shape.calculate_area()
        return total_area


# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)


# The total area is:  9.0
shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

