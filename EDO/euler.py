def euler(a, b, y0, f, n):
    h = (b - a)/n
    xs = []
    for i in range(n + 1):
        xs.append(a + i*h)

    print(xs)
    ys = [0]*(n+1)
    ys[0] = y0
    for i in range(1, n + 1):
        ys[i] = ys[i - 1] + h*f(xs[i - 1], ys[i - 1])
    print(ys)
def f(x, y):
    return -2*x -y

euler(0, 0.5, -1, f, 5)