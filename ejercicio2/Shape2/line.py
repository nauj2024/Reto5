from point import Point

class Line():
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def get_start_point(self):
        return self.start_point

    def set_start_point(self, new):
        self.start_point = new
        self.length = self.compute_length()

    def get_end_point(self):
        return self.end_point

    def set_end_point(self, new):
        self.end_point = new
        self.length = self.compute_length()

    def get_length(self):
        return self.length

    def compute_length(self):
        return self.start_point.compute_distance(self.end_point)
