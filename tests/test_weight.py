import unittest
from lib.Weight import create_euclidean_weight
from lib.Pixel import Pixel


class TestEuclideanWeights(unittest.TestCase):
    def test_default_weight(self):
        p1 = (1,1)
        p2 = (4, 5)
        w = create_euclidean_weight()
        assert w(p1, p2) == 1 / 25.

    def test_z_esp_weight(self):
        z = 3
        eps = 0.02
        p1 = (1, 1)
        p2 = (4, 5)
        w = create_euclidean_weight(z, eps)
        assert w(p1, p2) == 1 / (5.**z + eps)
