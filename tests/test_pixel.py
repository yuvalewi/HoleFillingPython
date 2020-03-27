import unittest
from lib.Pixel import Pixel


class TestPixelDistance(unittest.TestCase):
    def test_same_pixel_distance(self):
        p = Pixel(8, 6)
        assert p.calculate_distance(p) == 0

    def test_commutative_pixel_distance(self):
        p1 = Pixel(8, 6)
        p2 = Pixel(11, 10)
        assert p1.calculate_distance(p2) == 5
        assert p1.calculate_distance(p2) == p1.calculate_distance(p2)
