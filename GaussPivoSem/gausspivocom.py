import numpy

def gauss(a, b):

    # Com pivotamento parcial com troca física
    # Escalonamento (Triangularização)
    l = len(a)
    c = len(a[0])
    for k in range(l - 1):
        
        # Pivotamento parcial
        new_pivot_index = k
        for i in range(k + 1, l):
            if abs(a[i][k]) > abs(a[new_pivot_index][k]):
                new_pivot_index = i

        aux = a[k][:]
        a[k] = a[new_pivot_index]
        a[new_pivot_index] = aux
        aux = b[k]
        b[k] = b[new_pivot_index]
        b[new_pivot_index] = aux
            
        for i in range(k + 1, l):
            m = a[i][k]/a[k][k]
            for j in range(k, c):
                a[i][j] -= (m)*a[k][j]
            b[i] -= (m)*b[k]

    # Retrosubstituição
    x = [0]*c
    x[c - 1] = b[l - 1] / a[l - 1][c - 1]
    for i in range(l-1, -1, -1):
        soma = 0
        for j in range(i+1, c):
            soma += a[i][j]*x[j]
        x[i] = (b[i] - soma) / a[i][i]

    print("\nMatriz A (escalonada):")
    print(numpy.array(a))

    print("\nVetor b:")
    print(b)

    print("\nVetor solução x:")
    print(numpy.array(x))

    # Resíduos
    residuo = [0]*c
    for i in range(l):

        r = 0
        for j in range(c):
            r += a[i][j]*x[j]
        r -= b[i]
        residuo[i] = r
    
    print("\nVetor Resíduo:")
    print(numpy.array(residuo))

# matrix3 = [
#     [1, 1, 1.5, 1, 1.5, 0, 0, 0, 0, 0],
#     [0, 1, 0.01, 0.51, 1.5, 0.5, 0, 0, 0, 0],
#     [2.9, 1, 2, 1, 1, 0, 5, 0, 0 , 0],
#     [9, 1, 0.2, 1, 1, 0, 0, 1.5, 0, 0],
#     [1, 0, 2, 0, 0, 1, 1, 1, 0, 2],
#     [0, 1, 0, 0, -2, 0, 1, -1, 1, 1],
#     [1, 0, 2, 0, 0, 0, 1, 1, 1, 0],
#     [0, 1, 0, 0, 2, 0, 1, 1, 1, -1],
#     [0, 0, 1, 0, 2, 1, -1, 0, -1, -1],
#     [0, 1, 0, 0, 2, 0, 1, 0, 1, 1]
# ]

# constants3 = [4, -3, 1, -1, -1, 0, -1, 1, 3, -2]

matrix3 = [
    [1, 1, 0, 1],
    [2, 1, -1, -1],
    [-1, -2, 3, -1],
    [3, -1, -1, 2]
]
constants3 = [2, 1, 4, -3]

gauss(matrix3, constants3)