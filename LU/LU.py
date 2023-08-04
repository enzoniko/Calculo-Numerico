import numpy as np
def lu(a, b):
    l = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            linha.append(0)
        l.append(linha)
    
    u = []
    for i in range(len(a[0])):
        linha = []
        for j in range(len(a)):
            linha.append(0)
        u.append(linha)
    
    print("\nL:\n", np.array(l))
    print("\nU:\n", np.array(u))
    # Descobrir L e U
    for k in range(len(a[0])):
        # Aqui o k representa as colunas de L e as linhas de U que vamos descobrir
        # Calcular a coluna k de L:
        for i in range(k, len(l)):
            l[i][k] = a[i][k]
            for p in range(k):
                l[i][k] -= l[i][p]*u[p][k] 
        # Calcular a linha k de U:
        u[k][k] = 1
        for j in range(k + 1, len(u[0])):
            u[k][j] = a[k][j]
            for p in range(k):
                u[k][j] -= l[k][p]*u[p][j]
            u[k][j] /= l[k][k]

    print("\nL:\n", np.array(l))
    print("\nU:\n", np.array(u))
    print()
    print(np.dot(np.array(l), np.array(u)))

    # Ly = b (Substituição direta)
    y = [0]*len(u[0])
    for i in range(len(l)):
        y[i] = b[i]
        for j in range(i):
            y[i] -= l[i][j]*y[j]
        y[i] /= l[i][i]
    
    print("\nY:\n", y)

    # Ux = y (Retrosubstituição)
    x = [0]*len(u[0])
    x[len(u[0]) - 1] = y[len(l) - 1] / u[len(l) - 1][len(u[0]) - 1]
    for i in range(len(l)-1, -1, -1):
        soma = 0
        for j in range(i+1, len(u[0])):
            soma += u[i][j]*x[j]
        x[i] = (y[i] - soma) / u[i][i]

    print("\nX:\n", x)

    # Resíduos
    residuo = [0]*len(u[0])
    for i in range(len(l)):
        r = 0
        for j in range(len(u[0])):
            r += a[i][j]*x[j]
        r -= b[i]
        residuo[i] = r
    print("\nVetor Resíduo:")
    print(np.array(residuo))

    
a = [[1, 1, 2], [3, -5, 1], [2, 1, -1]]
# matrix2 = [[-0.421, 0.784, 0.279], [0.448, 0.832, 0.193], [0.421, 0.784, -0.207]]
constants1 = [27, -9, -1]
lu(a, constants1)