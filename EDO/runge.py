from math import tan, sin
def f(x, y):
    return y/tan(x)

# def runge2(a, b, y0, f, n):
#     h = (b - a)/n
#     xs = []
#     for i in range(n + 1):
#         xs.append(a + i*h)


#     print(xs)
#     ys = [0]*(n+1)
#     ys[0] = y0
#     for i in range(1, n + 1):
#         k1 = h*f(xs[i - 1], ys[i - 1])
#         k2 = h*f(xs[i-1] + h, ys[i - 1] + k1)
#         ys[i] = ys[i - 1] + (1/2)*(k1 + k2)
#     print(ys)


# runge2(0, 3, 10, f, 3)

def runge4(a, b, y0, f, n):
    h = (b - a)/n
    xs = []
    for i in range(n + 1):
        xs.append(a + i*h)


    print(xs)
    ys = [0]*(n+1)
    ys[0] = y0
    for i in range(1, n + 1):
        k1 = h*f(xs[i - 1], ys[i - 1])

        k2 = h*f(xs[i - 1] + h/2, ys[i - 1] + k1/2)
        k3 = h*f(xs[i - 1] + h/2, ys[i - 1] + k2/2)
        k4 = h*f(xs[i - 1] + h, ys[i - 1] + k3)
        ys[i] = ys[i - 1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    print(ys)
    return ys


ys = runge4(1, 1.5, 0.841470984807897, f, 5)

xs = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
print([sin(x) for x in xs])

print([abs(ys[i] - sin(xs[i])) for i in range(len(xs))])