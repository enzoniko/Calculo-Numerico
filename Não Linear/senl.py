from scipy.optimize import fsolve
from math import exp
def equations(p):
    x, y = p
    return ((x - 1)**2 + y**2 - 4, x**2 + (y - 1)**2 - 4)

x, y = fsolve(equations, (1, 2))

print((x, y))
