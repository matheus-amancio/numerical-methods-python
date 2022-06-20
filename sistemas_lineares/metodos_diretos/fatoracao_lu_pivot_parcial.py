import numpy as np


def fatoracao_lu_pivot_parcial(A, b):
    """Resolve um sistema linear utilizando o método da \
fatoração LU com pivoteamento parcial.

    Parâmetros:
        [A] (numpy.array): Matriz de coeficientes.
        [b] (numpy.array): Vetor das constantes.

    Retorno:
        Vetor com a solução (numpy.array)
"""
    A = A.astype(float, copy=True)
    b = b.astype(float, copy=True)

    n = len(A)

    p = np.zeros(n, dtype=int)

    # Vetor representativo das permutações realizadas
    for i in range(n):
        p[i] = i

    # Pivoteamento
    for k in range(n - 1):
        pivo = abs(A[k, k])
        r = k
        for i in range(k + 1, n):
            if abs(A[i, k]) > pivo:
                pivo = abs(A[i, k])
                r = i

        if pivo == 0:
            print("A matriz é singular.")
            return None

        if r != k:
            p[k], p[r] = p[r], p[k]
            for j in range(n):
                A[k, j], A[r, j] = A[r, j], A[k, j]

        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k] = m
            for j in range(k + 1, n):
                A[i, j] = A[i, j] - m * A[k, j]

    c = np.zeros(n)
    y = np.zeros(n)
    x = np.zeros(n)

    # Resolução do sistema c = Pb
    for i in range(n):
        r = p[i]
        c[i] = b[r]

    # Resolução do sistema Ly = c
    for i in range(n):
        soma = 0
        for j in range(n - 1):
            soma += A[i, j] * y[j]
        y[i] = c[i] - soma

    # Resolução do sistema Ux = y
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += A[i, j] * x[j]
        x[i] = (y[i] - soma) / A[i, i]

    print(f"A solução do sistema é o vetor: {x}")
    return x


if __name__ == "__main__":
    A = np.array([[3, -4, 1], [1, 2, 2], [4, 0, -3]])
    b = np.array([9, 3, -2])

    fatoracao_lu_pivot_parcial(A, b)
