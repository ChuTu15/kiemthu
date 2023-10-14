def area(length, width):
    if length <= 0 or width <= 0:
        return "error: Invalid input"
    return length * width

import unittest

class TestArea(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_2_1(self):
        self.assertEqual(area(-10, -10), "error: Invalid input")

    def test_area_2_2(self):
        self.assertEqual(area(10, -10), "error: Invalid input")

    def test_area_2_3(self):
        self.assertEqual(area(-10, 10), "error: Invalid input")

    def test_area_2_4(self):
        self.assertEqual(area(0, 10), "error: Invalid input")

    def test_area_2_5(self):
        self.assertEqual(area(10, 0), "error: Invalid input")

if __name__ == '__main__':
    unittest.main()