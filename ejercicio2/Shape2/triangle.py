from shape import Shape
from point import Point

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        vertices = [p1, p2, p3]
        super().__init__(vertices)

    def compute_area(self):
        a = self.edges[0].get_length()
        b = self.edges[1].get_length()
        c = self.edges[2].get_length()
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c))**0.5

    def compute_inner_angles(self):
        return None
