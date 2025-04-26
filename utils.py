# Arquivo contendo funções básicas para matrizes em Python

#matriz = [[1, 2], [3, 4]]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Loop de repetição que percorre toda a matriz
def percorrer_matriz(matriz):
    print("Matriz: ")
    for i in range(len(matriz)):
        print("|", end="")
        # Loop da linha da matriz
        for j in range(len(matriz[i])):
            # Loop de cada célula da matriz
            print(matriz[i][j], end="|")
        print()
    print()


# Pegar diagonal principal da matriz
def pega_diagonal_principal(matriz):
    # Como não podemos utilizar o append, criamos um vetor com a quantidade de linhas de uma matriz
    diagonal_principal = [i for i in range(len(matriz))]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Aqui é onde fariamos o append
            if i == j:
                diagonal_principal[i] = matriz[i][j]
            

    return diagonal_principal


# Pegar diagonal principal da matriz
def pegar_diagonal_secundaria(matriz):
    # Repetimos o que fizemos na função anterior
    diagonal_secundaria = [i for i in range(len(matriz))]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i + j == len(matriz[i]) - 1:
                # Aqui é onde fariamos o append
                diagonal_secundaria[i] = matriz[i][j]

    return diagonal_secundaria

# Execuções do código

# Função sem retorno
percorrer_matriz(matriz)

# Funções com retorno
print(f"Diagonal Principal: {pega_diagonal_principal(matriz)}")
print(f"Diagonal Secundária: {pegar_diagonal_secundaria(matriz)}")
