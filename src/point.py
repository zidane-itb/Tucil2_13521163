from __future__ import annotations
from math import sqrt

euclidean_count: int = 0


class Point:
    euclidean_count: int = 0

    def __init__(self, dim, points):
        self.dim = dim
        self.points = points

    def get_distance_to(self, point2: Point) -> float:
        if self.dim != point2.dim:
            raise Exception("dimensions do not match")

        Point.euclidean_count += 1

        sum: float = 0
        for i in range(self.dim):
            sum += pow(self.points[i] - point2.points[i], 2)

        return sqrt(sum)

    def equals(self, point2: Point) -> bool:
        if self.dim != point2.dim:
            raise Exception("dimensions do not match")

        for i in range(self.dim):
            if not self.points[i] == point2.points[i]:
                return False
        return True

    def __repr__(self):
        strs = ''
        for i in range(self.dim):
            strs += 'e' + str(i + 1) + ' : ' + str(self.points[i]) + ' '

        return strs
