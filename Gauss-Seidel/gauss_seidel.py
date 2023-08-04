def seidel(a, b, w, erro):

    # Verificar se a convergência é garantida
    # ...
    
    # Inicializa o vetor das incógnitas
    x = [0]*len(a[0])

    # Inicializa o vetor das aproximações
    xk = [0]*len(a[0])

    # Inicializa a variável que guarda a máxima diferença absoluta
    max_abs_diff = 100

    # Inicializa o contador de iterações
    k = 0
    # Enquanto não atingirmos a condição de parada
    while max_abs_diff >= erro: 
        #print(max_abs_diff) 
        #print(".", end = "")
        # Para valor do vetor
        for i in range(len(x)):
            xk[i] = b[i]
            soma = 0
            for j in range(i):
                soma += a[i][j]*xk[j]

            for j in range(i + 1, len(x)):
                soma += a[i][j]*x[j]
            
            xk[i] -= soma
            xk[i] /= a[i][i]
            
           

        # Calcula a máxima diferença absoluta
        max_abs_diff = 0
        for i in range(len(xk)):
            new = abs(xk[i] - x[i])
            if max_abs_diff < new:
                max_abs_diff = new

        for i in range(len(x)):
            x[i] = w*xk[i] + (1 - w)*x[i]

        k += 1

    return x, k, max_abs_diff

matrix = [
    [4, 1, 2],
    [1, 2, 1],
    [1, 0.1, 1]
]

constants = [1, 4, -3]
best_w = 3
best_k = 1000
for w in range(1, 200):
    w /= 100
    print("-", end = "")
    x, k, max_abs_diff = seidel(matrix, constants, w, 1e-13)
    if k < best_k:
        best_k = k
        best_w = w
print()
x, k, max_abs_diff = seidel(matrix, constants, best_w, 1e-13)
print(x)
print(k)
print(max_abs_diff)
print(best_w)