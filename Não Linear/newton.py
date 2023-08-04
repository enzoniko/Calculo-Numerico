import math
from AOP import *
f_vector = [lambda x1, x2: (x1 - 1)**2 + x2**2 - 4, lambda x1, x2: x1**2 + (x2 - 1)**2 - 4]

jacobian_matrix = [
    [lambda x1, x2: 2*x1 - 2, lambda x1, x2: 2*x2],
    [lambda x1, x2: 2*x1, lambda x1, x2: 2*x2 - 2]
]

def jacobian(x1, x2):
    jacobian = []
    for i in range(len(jacobian_matrix)):
        jacobian.append([])
        for j in range(len(jacobian_matrix)):
            jacobian[i].append(jacobian_matrix[i][j](x1, x2))
    return jacobian

def f(x1, x2):
    f = []
    for i in range(len(f_vector)):
        f.append(f_vector[i](x1, x2))
    return f

import numpy
def gauss(a, b):

    # Com pivotamento parcial sem troca física
    # Escalonamento (Triangularização)
    l = len(a)
    c = len(a[0])
    o = list(range(l))
    for k in range(l - 1):
        
        # Pivotamento parcial
        new_pivot_index = k
        for i in range(k + 1, l):
            if abs(a[o[i]][k]) > abs(a[o[new_pivot_index]][k]):
                new_pivot_index = i

        aux = o[k]
        o[k] = o[new_pivot_index]
        o[new_pivot_index] = aux
        # aux = b[o[k]]
        # b[o[k]] = b[o[new_pivot_index]]
        # b[o[new_pivot_index]] = aux
            
        
        for i in range(k + 1, l):
            m = a[o[i]][k]/a[o[k]][k]
            for j in range(k, c):
                a[o[i]][j] -= (m)*a[o[k]][j]
            b[o[i]] -= (m)*b[o[k]]

    
    # Retrosubstituição
    x = [0]*c
    x[c - 1] = b[o[l - 1]] / a[o[l - 1]][c - 1]
    for i in range(l-1, -1, -1):
        soma = 0
        for j in range(i+1, c):
            soma += a[o[i]][j]*x[j]
        x[i] = (b[o[i]] - soma) / a[o[i]][i]

    # print("\nMatriz A (escalonada):")
    # print(numpy.array(a))

    # print("\nVetor b:")
    # print(b)

    print("\nVetor solução x:")
    print(numpy.array(x))

    # print("\nVetor Ordenamento, das trocas de linha: ")
    # print(o)
    # Resíduos
    residuo = [0]*c
    for i in range(l):
        r = 0
        for j in range(c):
            r += a[i][j]*x[j]
        r -= b[i]
        residuo[i] = r
    # print("\nVetor Resíduo:")
    # print(numpy.array(residuo))
    return x

def non_linear(x0, erro=1e-8):
    xk = [0]*len(x0)
    k = 0
    deltas = [1, 1]
    while max(abs(deltas[0]), abs(deltas[1])) > erro:
        deltas = gauss(jacobian(x0[0], x0[1]), Times(f(x0[0], x0[1]), -1))
        xk = Plus(x0, deltas)
        print(xk)
        x0 = xk
        k+=1
    print("--------------------")
    print("Iterações: ", k)
    print("Solução: ", xk)
    print("Deltas: ", deltas)
    print("Precisão: ", max(abs(deltas[0]), abs(deltas[1])))
    return k

x0 = [1, 2]
non_linear(x0)