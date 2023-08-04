import numpy
# import matplotlib.pyplot as plt
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

    print("\nMatriz A (escalonada):")
    print(numpy.array(a))

    print("\nVetor b:")
    print(b)

    # print("\nVetor solução x:")
    # print(numpy.array(x))

    print("\nVetor Ordenamento, das trocas de linha: ")
    print(o)
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
    return x

def potencia(x, y, m = 1):
    z = [numpy.log(i) for i in y]
    A = numpy.zeros((m + 1, m + 1))
    b = numpy.zeros(m + 1)
    t = [numpy.log(i) for i in x]
    for i in range(m + 1):
        for j in range(i + 1):
            for k in range(len(t)):
                A[i][j] += (t[k]**j)*(t[k]**i)
            A[j][i] = A[i][j]
        for k in range(len(y)):
            b[i] += z[k]*(t[k]**i)
    print(A)
    c = gauss(A, b)
    c[0] = numpy.exp(c[0])
    g = numpy.zeros(len(x))
    for i in range(len(x)):
        g[i] = c[0]*(x[i]**(c[1]))
    
    e = sum((y - g)**2)
    print(e)
    s = numpy.arange(0, 10, 0.01)
    gs = numpy.zeros(len(s))
    for i in range(len(s)): 
        gs[i] = c[0]*(s[i]**(c[1]))

    print("\nVetor das constantes:")
    print(numpy.array(c))

    # plt.plot(x, y, 'o')
    # plt.plot(s, gs)
    # plt.grid(True)
    
    # plt.show()

x=[1.3, 3.4, 5.1, 6.8, 8]
y=[2, 5.2, 3.8, 6.1, 5.8]

x=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
y=[3.16, 2.38, 1.75, 1.34, 1, 0.74, 0.56]

x=[1, 2, 3, 4, 5]
y=[0.5, 1.7, 3.4, 5.7, 8.4]
potencia(x, y)