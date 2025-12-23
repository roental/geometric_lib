import unittest

from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = rectangle_area(5, 10)
        self.assertEqual(res, 50)

    def test_perimeter_normal(self):
        res = rectangle_perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_perimeter_square(self):
        res = rectangle_perimeter(10, 10)
        self.assertEqual(res, 40)


class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        res = triangle_area(10, 5)
        self.assertEqual(res, 25.0)

    def test_perimeter_normal(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_zero_side(self):
        res = triangle_perimeter(0, 4, 5)
        self.assertEqual(res, 9)


class CircleTestCase(unittest.TestCase):
    def test_area_radius_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_perimeter_radius_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)


class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = square_area(4)
        self.assertEqual(res, 16)

    def test_perimeter_normal(self):
        res = square_perimeter(4)
        self.assertEqual(res, 16)


if __name__ == '__main__':
    unittest.main()
