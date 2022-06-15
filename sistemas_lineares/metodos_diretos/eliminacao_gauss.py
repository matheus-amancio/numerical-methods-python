import numpy as np

from triangular_superior import triangular_superior


def eliminacao_gauss(A, b):
    """Resolve um sistema linear utilizando o método da \
eliminação de Gauss.

    Parâmetros:
        [A] (numpy.array): Matriz de coeficientes.
        [b] (numpy.array): Vetor das constantes.

    Retorno:
        Vetor com a solução (numpy.array)
"""
    n = len(A)

    for k in range(n):
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i] = A[i] - m * A[k]
            b[i] = b[i] - m * b[k]

    x = triangular_superior(A, b)

    return x


if __name__ == "__main__":
    A = np.array([[3, 2, 4], [1, 1, 2], [4, 3, -2]], dtype=float)
    b = np.array([1, 2, 3], dtype=float)

    eliminacao_gauss(A, b)
