"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
# TODO write 3 tests as described above
class CircleTest(unittest.TestCase):


    def test_valid(self):
        c = Circle(3)
        c1 = Circle(4)
        result = c.add_area(c1)
        self.assertIsInstance(result, Circle)



    def test_add_area_is_radii_positive(self):
        for i in [-1,-2,-3,-4]:
            with self.assertRaises(ValueError):
                c1 = Circle(i)
                c2 = Circle(i)



    def test_add_area_when_one_is_zero(self):
        c = Circle(0)
        c1 = Circle(5)
        result = c.add_area(c1)
        c1_radius = c1.get_radius()
        result_radius = result.get_radius()
        self.assertEquals(c1_radius,result_radius)