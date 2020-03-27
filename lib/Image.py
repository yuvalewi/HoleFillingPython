from Hole import Connectivity, Hole


class Image:
    def __init__(self, image, mask, connectivity=Connectivity.eight_connectivity):
        self.mask = mask
        self.image = image
        self.hole = Hole(image, connectivity)
        self.connectivity = connectivity
        self._find_hole()

    def _find_hole(self):
        hole = self.hole.hole
        boundary = self.hole.boundary

        m, n = self.mask.shape
        for i in xrange(m):
            for j in xrange(n):
                if self.mask[(i, j)] == 0:
                    hole.add((i, j))

        for p in hole:
            for point in [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]:
                if point not in hole and point not in boundary:
                    boundary.add(point)
            if self.connectivity == Connectivity.eight_connectivity:
                for point in [(p[0] - 1, p[1] - 1), (p[0] + 1, p[1] - 1), (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1)]:
                    if point not in hole and point not in boundary:
                        boundary.add(point)