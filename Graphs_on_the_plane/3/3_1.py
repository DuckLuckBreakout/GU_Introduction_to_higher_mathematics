from math import cos, sin
def polar_to_cartesian(r, alpha):
    x = r*cos(alpha)
    y = r*sin(alpha)
    return x, y
