from rectangle import Rectangle
from point import Point

class Square(Rectangle):
    def __init__(self, bottom_left: Point, side: float):
        super().__init__(bottom_left, side, side)
