def tridiagonal(a, b):
    n = len(b)
    t = []
    for i in range(1, n):
        t.append(a[i][i-1])

    r = []
    for i in range(0, n):
        r.append(a[i][i])
    
    d = []
    for i in range(0, n - 1):
        d.append(a[i][i + 1])
    
    for i in range(1, n - 1):
        mult = t[i]/r[i - 1]
        r[i] -= mult*d[i - 1]
        b[i] -= mult*b[i - 1]
    
    # t[0] = 0
    # d[n - 1] = 0
    x = [0]*n
    x[n - 1] = b[n - 1]/r[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - d[i]*x[i + 1])/r[i]
    
    return x

a = [
    [2, 1, 0, 0, 0],
    [1, 2, 1, 0, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 1, 2, 1],
    [0, 0, 0, 1, 2]
]

b = [4, 4, 0, 0, 2]

x = tridiagonal(a, b)
print(x)
