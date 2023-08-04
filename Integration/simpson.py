from time import time
from math import exp
def f(x):
    return x*exp(x)

def simpson(a, b, n, f):
    h = (b - a)/n
    xs = []
    for i in range(n + 1):
        xs.append(a + i*h)
    ys = [f(x) for x in xs]

    r = ys[0]
    for i in range(1, n//2 + 1):
        r += 4*ys[(2*i)-1]
    for i in range(1, n//2):
        r += 2*ys[2*i]

    r += ys[-1]
    r *= h/3
    print(xs)
    print(ys)
    return r

def integral(a, b, f, erro):
    n = 20
    xk = simpson(a, b, n-10, f)
    xkp1 = simpson(a, b, n, f)
    e = abs(xkp1 - xk)
    while e > erro:
        n+=10
        xk = xkp1
        xkp1 = simpson(a, b, n, f)
        e = abs(xkp1 - xk)
    print(n)
    return xkp1

print(simpson(0, 3, 8, f))
# s = time()
# print(integral(1, 2, f, 1e-8))
# e = time()
# print(e - s)