class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def compute_distance(self, sec):
        return ((self.x - sec.x)**2+(self.y - sec.y)**2)**0.5
