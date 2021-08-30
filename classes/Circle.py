class Circle(object):
    # Atributes
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;

    # Methods
    def increase_size(self, plus_size):
        self.radius = self.radius + plus_size

    def draw_circle(self):
        print("Radius:", self.radius)