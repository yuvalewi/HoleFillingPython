import unittest
import cv2
from lib.Image import Image
from lib.Hole import Connectivity


class TestImageInitialization(unittest.TestCase):
    def test_mask_in_eight_connectivity(self):
        img = cv2.imread('penguin-img.png', 0)
        mask = cv2.imread('penguin-mask.png', 0)
        image = Image(img, mask, Connectivity.eight_connectivity)
        hole = image.hole

        assert len(hole.hole) == len(set(hole.hole))
        assert len(hole.hole) == 1215
        for p in hole.hole:
            assert 92 <= p[0] <= 106 and 13 <= p[1] <= 93

        assert len(hole.boundary) == len(set(hole.boundary))
        assert len(hole.boundary) == 196
        for p in hole.boundary:
            assert 91 <= p[0] <= 107 and p[1] in (12, 94) or 12 <= p[1] <= 94 and p[0] in (91, 107)

    def test_mask_in_four_connectivity(self):
        img = cv2.imread('penguin-img.png', 0)
        mask = cv2.imread('penguin-mask.png', 0)
        image = Image(img, mask, Connectivity.four_connectivity)
        hole = image.hole
        assert len(hole.hole) == len(set(hole.hole))
        assert len(hole.hole) == 1215
        for p in hole.hole:
            assert 92 <= p[0] <= 106 and 13 <= p[1] <= 93

        assert len(hole.boundary) == len(set(hole.boundary))
        assert len(hole.boundary) == 192
        for p in hole.boundary:
            assert p not in ((91, 12), (91, 94), (107, 12), (107, 94)) and (
                        91 <= p[0] <= 107 and p[1] in (12, 94) or 12 <= p[1] <= 94 and p[0] in (91, 107))
