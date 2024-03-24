import math


class ShapeCalculator:
    def __init__(self):
        pass

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_triangle_area(self, side1, side2, side3):
        p = (side1 + side2 + side3) / 2
        return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

    def check_right_triangle(self, side1, side2, side3):
        sides = [side1, side2, side3]
        max_side = max(sides)
        sides.remove(max_side)
        if max_side ** 2 == sides[0] ** 2 + sides[1] ** 2:
            return True
        return False


# Юнит-тесты
import unittest


class TestShapeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ShapeCalculator()

    def test_circle_area(self):
        self.assertEqual(round(self.calculator.calculate_circle_area(3), 2), 28.27)

    def test_triangle_area(self):
        self.assertEqual(self.calculator.calculate_triangle_area(3, 4, 5), 6)

    def test_right_triangle(self):
        self.assertTrue(self.calculator.check_right_triangle(3, 4, 5))
        self.assertFalse(self.calculator.check_right_triangle(3, 4, 6))


if __name__ == "__main__":
    unittest.main()
