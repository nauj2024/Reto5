from line import Line

class Shape:
    def __init__(self, vertices: list, regular: bool = False):
        self.regular = regular
        self.vertices = vertices
        self.edges = self.compute_edges()
        self.angles = []

    def compute_edges(self):
        edges = []
        n = len(self.vertices)
        for i in range(n):
            edge = Line(self.vertices[i], self.vertices[(i+1)%n]) 
            edges.append(edge)
        return edges

    def get_regular(self):
        return self.regular

    def set_regular(self,new):
        self.vertices = new

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, new):
        self._vertices = new
        self._edges = self.compute_edges()

    def get_edges(self):
        return self.edges

    def get_angles(self):
        return self.angles

    def set_angles(self, new):
        self._inner_angles = new

    def compute_area(self):
        return None

    def compute_perimeter(self):
        return None

    def compute_inner_angles(self):
        return None
