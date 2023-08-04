from time import time
from math import exp
def f(x):
    return exp(x)/x

def trapezio(a, b, n, f):
    h = (b - a)/n
    xs = []
    for i in range(n + 1):
        xs.append(a + i*h)

    ys = [f(x) for x in xs]

    r = ys[0]
    for i in range(1, len(xs)):
        r += 2*ys[i]

    r += ys[-1]
    r *= h/2

    return r

def integral(a, b, f, erro):
    n = 20
    xk = trapezio(a, b, n-10, f)
    xkp1 = trapezio(a, b, n, f)
    while abs(xkp1 - xk) > erro:
        n+=10
        xk = xkp1
        xkp1 = trapezio(a, b, n, f)
    print(n)
    return xkp1

# s = time()
# print(integral(0, 0.8, f, 1e-8))
# e = time()
# print(e - s)

print(trapezio(1, 2, 4, f))