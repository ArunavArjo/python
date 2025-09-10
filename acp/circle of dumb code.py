import math

class Triangle:
    """
    A class to represent a triangle.
    """
    def __init__(self, side1, side2, side3):
        """
        Constructs a Triangle object with three side lengths.
        Raises a ValueError if the given sides do not form a valid triangle.
        """
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Invalid triangle: The sum of any two sides must be greater than the third side.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        """
        Computes the area of the triangle using Heron's formula.
        """
        s = (self.side1 + self.side2 + self.side3) / 2  # Semiperimeter
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def calculate_perimeter(self):
        """
        Computes the perimeter of the triangle.
        """
        return self.side1 + self.side2 + self.side3


try:
    triangle1 = Triangle(3, 4, 5)
    print(f"Triangle 1 Area: {triangle1.calculate_area()}")
    print(f"Triangle 1 Perimeter: {triangle1.calculate_perimeter()}")

    triangle2 = Triangle(7, 10, 5)
    print(f"Triangle 2 Area: {triangle2.calculate_area()}")
    print(f"Triangle 2 Perimeter: {triangle2.calculate_perimeter()}")

    
except ValueError as e:
    print(f"Error: {e}")