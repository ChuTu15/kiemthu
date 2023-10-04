def area(length, width):
    if length <= 0 or width <= 0:
        return "error: Invalid input"
    return length * width

import unittest

class TestArea(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(10, 5), 50)

    def test_area_2(self):
        self.assertEqual(area(-1, 5), "error: Invalid input")


if __name__ == '__main__':
    unittest.main()