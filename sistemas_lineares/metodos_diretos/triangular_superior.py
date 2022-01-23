import numpy as np


def triangular_superior(A, b):
    """Resolve um sistema linear com matriz de coeficientes \
triangular superior.

    Parâmetros:
        [A] (numpy.array): Matriz triangular superior (coeficientes).
        [b] (numpy.array): Vetor das constantes.

    Retorno:
        Vetor com a solução (numpy.array)
"""

    n = len(A)
    x = np.zeros(n)

    x[n - 1] = b[n - 1] / A[n - 1, n - 1]

    for k in range(n - 2, -1, -1):
        s = 0
        for j in range(k + 1, n):
            s += A[k, j] * x[j]
            x[k] = (b[k] - s) / A[k, k]

    print(f"A solução do sistema é o vetor: {x}")
    return x


if __name__ == "__main__":
    A = np.array([[2, 1, 3], [0, 1, -1], [0, 0, 2]])
    b = np.array([11, 1, 4])
    triangular_superior(A, b)
