def jacobi(a, b, erro):

    # Inicializa o vetor das incógnitas
    x = [0]*len(a[0])

    # Inicializa o vetor das aproximações
    xk = [0]*len(a[0])

    # Inicializa a variável que guarda a máxima diferença absoluta
    max_abs_diff = 100

    # Inicializa o contador de iterações
    k = 0
    # Enquanto não atingirmos a condição de parada
    while max_abs_diff > erro:  
        # Para valor do vetor
        for i in range(len(x)):
            xk[i] = b[i]
            soma = 0
            for j in range(len(x)):
                if j != i:
                    soma += a[i][j]*x[j]
            xk[i] -= soma
            xk[i] /= a[i][i]

        # Calcula a máxima diferença absoluta
        max_abs_diff = 0
        for i in range(len(xk)):
            new = abs(xk[i] - x[i])
            if max_abs_diff < new:
                max_abs_diff = new

        x = xk[:]
        k += 1

    return x, k, max_abs_diff

a = [
    [3, -1, -1],
    [1, 3, 1],
    [2, -2, 4]
]

b = [1, 5, 4]

x, k, max_abs_diff = jacobi(a, b, 10e-16)

print(x)
print(k)
print(max_abs_diff)

    