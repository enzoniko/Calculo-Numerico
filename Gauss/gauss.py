def gauss(a, b):

    # Com pivotamento parcial
    # Escolher linha pivot
    if a[0][0] == 0:
        a0 = a[0]
        for i, linha in enumerate(a):
            if linha[0] != 0:
                a[0] = linha
                a[i] = a0 
                break
    # Fim pivotamento
    print(a)
    # Escalonamento (Triangularização)
    l = len(a)
    c = len(a[0])
    for k in range(l - 1):
        for  i in range(k + 1, l):
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

    print(x)

    # Resíduos
    for i in range(l):

        r = 0
        for j in range(c):
            r += a[i][j]*x[j]
        r -= b[i]

        print(i, r)

# Testar e corrigir possíveis problemas
        
     
matrix1 = [[0, 2, 3], [2, -4, -1], [-1, 1, 4]]
constants1 = [7, 1, -5]

gauss(matrix1, constants1)

matrix2 = [[-0.421, 0.784, 0.279], [0.448, 0.832, 0.193], [0.421, 0.784, -0.207]]
constants2 = [0, 1, 0]

gauss(matrix2, constants2)