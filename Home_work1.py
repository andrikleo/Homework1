import unittest



class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(14)
        self.assertEqual(circle.area(), 615.44)

    def test_Square_area(self):
        square = Square(12.6)
        self.assertEqual(square.area(), 158.76)

    def test_triangle_area(self):
        triangle = Triangle(9, 11)
        self.assertEqual(triangle.area(), 49.5)

if __name__ == '__main__':
    unittest.main()
