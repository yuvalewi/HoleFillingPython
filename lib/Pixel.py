class Pixel:
    """
    A class that represents a pixel.
    """

    def __init__(self, x, y, level=0, value=-1):
        """
        :param x: x coordinate.
        :param y: y coordinate.
        :param value: Pixel's color value in gray scale.
        :param level: Pixel's distance from boundary. Boundary pixels marked by 0.
        """
        self.x = x
        self.y = y
        self.value = value
        self.level = level

    def calculate_distance(self, other):
        """
        Calculates the euclidean distance between two pixels.
        :param other: A pixel parameter
        :return: The euclidean distance between self and other.
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** .5
