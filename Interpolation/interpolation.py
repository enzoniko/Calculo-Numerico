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

    # print("\nVetor solução x:")
    # print(numpy.array(x))

    # print("\nVetor Ordenamento, das trocas de linha: ")
    # print(o)
    # # Resíduos
    # residuo = [0]*c
    # for i in range(l):
    #     r = 0
    #     for j in range(c):
    #         r += a[i][j]*x[j]
    #     r -= b[i]
    #     residuo[i] = r
    # print("\nVetor Resíduo:")
    # print(numpy.array(residuo))
    return x
def build_matrix(xs):
    n = len(xs)
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(xs[i]**j)
    return matrix

def interpolation(xs, ys):
    a = build_matrix(xs)
    b = ys
    p = gauss(a, b)
    
    return p

def point_evaluation(p, x):
    result = 0
    for i in range(len(p)):
        result += p[i]*x**i
    print(result)

import time 
xs = [0, 0.5, 1]
ys = [-1, -1.14872, -1.71828]
p = interpolation(xs, ys)
print(p)
point_evaluation(p, 0.7)