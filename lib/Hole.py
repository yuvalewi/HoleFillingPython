import enum
from Weight import create_euclidean_weight


class Connectivity(enum.Enum):
    """
    A class that represents connectivity type of a hole.
    """
    four_connectivity = 4
    eight_connectivity = 8


class Hole:
    """
    A class that represents a hole - can be eaither 4 or 8 connected.
    """

    def __init__(self, image, connect_type, weight=create_euclidean_weight()):
        self.image = image
        self.boundary = set()
        self.hole = set()
        self.connect_type = connect_type
        self.weight = weight

    def fix_hole(self):
        for pixel in self.hole:
            total_weight = 0.
            weighted_values = 0.
            for bound in self.boundary:
                w = self.weight(bound, pixel)
                weighted_values += w * self.image[bound[0], bound[1]]
                total_weight += w
            self.image[pixel] = weighted_values / total_weight
