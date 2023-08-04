A = {
    2: [1, 1],
    3: [0.888888888888888888, 0.55555555555555, 0.5555555555555555555],
    4: [0.65214515486254614262693, 0.65214515486254614262693, 0.34785484513745385737, 0.34785484513745385737],
    5: [0.568888888888888888888888, 0.4786286704993664680412915, 0.4786286704993664680412915, 0.23692688505618908751426, 0.23692688505618908751426]
}

ts = {
    2: [-0.577350269189625764509148, 0.57735026918962576450914],
    3: [0, -0.7745966692414833770358531, 0.7745966692414833770358531],
    4: [-0.33998104358485626480267, 0.33998104358485626480267, -0.861136311594052575223946, 0.861136311594052575223946],
    5: [0, -0.5384693101056830910363144, 0.5384693101056830910363144, -0.9061798459386639927976269, 0.9061798459386639927976269]
}


def gaussian_quadrature(a, b, f, n):
    I = 0
    
    for i in range(n):
        x = (1/2)*(b - a)*ts[n][i] + (1/2)*(b + a)
        dx = (1/2)*(b - a)
        I += A[n][i]*f(x)*dx

    print(I)
import math
def f(x):
    return x*math.exp(x)

gaussian_quadrature(0, 3, f, 4)

