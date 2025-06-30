from triangle import Triangle
from point import Point

class Equilateral(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.set_angles([60.0, 60.0, 60.0])
