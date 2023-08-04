import numpy as np
def lu(a, b):
    print("\nA:\n", np.array(a))
  
    # Descobrir L e U
    for k in range(len(a[0])):
        # Aqui o k representa as colunas de L e as linhas de U que vamos descobrir
        # Calcular a coluna k de L:
        for i in range(k, len(a)):
            #l[i][k] = a[i][k]
            for p in range(k):
                a[i][k] -= a[i][p]*a[p][k] 
        # Calcular a linha k de U:
        for j in range(k + 1, len(a[0])):
            #u[k][j] = a[k][j]
            for p in range(k):
                a[k][j] -= a[k][p]*a[p][j]
            a[k][j] /= a[k][k]

    print("\nA:\n", np.array(a))

    # Ly = b (Substituição direta)
    y = [0]*len(a[0])
    for i in range(len(a)):
        y[i] = b[i]
        for j in range(i):
            y[i] -= a[i][j]*y[j]
        y[i] /= a[i][i]
    
    print("\nY:\n", y)

    # Ux = y (Retrosubstituição)
    x = [0]*len(a[0])
    x[len(a[0]) - 1] = y[len(a) - 1]
    for i in range(len(a)-1, -1, -1):
        soma = 0
        for j in range(i+1, len(a[0])):
            soma += a[i][j]*x[j]
        x[i] = (y[i] - soma)

    print("\nX:\n", x)

    return x
    
a = [[1, 1, 2], [3, -5, 1], [2, 1, -1]]
ca = [[1, 1, 2], [3, -5, 1], [2, 1, -1]]
b = [27, -9, -1]
x = lu(a, b)
# Resíduos
residuo = [0]*len(a[0])
for i in range(len(a)):
    for j in range(len(a[0])):
        residuo[i] += ca[i][j]*x[j]
    residuo[i] -= b[i]
print("\nVetor Resíduo:")
print(np.array(residuo))
