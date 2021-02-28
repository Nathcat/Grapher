import matplotlib.pyplot as plt


class Grapher:
    def __init__(self):
        self.x = []
        self.y = []

    def calc_points(self, f, x0, x1, increment=1):
        for x in range(x0, x1 + 1, increment):
            self.x.append(x)
            self.y.append(f(x))

    def render_graph(self):
        plt.plot(self.x, self.y)
        plt.show()

    def reset_points(self):
        self.x = []
        self.y = []
