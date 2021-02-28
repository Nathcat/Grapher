import numpy as np
from Grapher import *


def f(x):
    return np.square(x)


grapher = Grapher()

grapher.calc_points(f, -5, 5)

grapher.render_graph()
