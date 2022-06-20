import numpy as np


def vandermonde(x, y):
    """Calcula os coeficientes de um polinômio interpolador \
pelo Método de Vandermonde.

    Parâmetros:
        [x] (numpy.array): valores de x.
        [y] (numpy.array): valores de y ou f(x).

    Retorno:
        Vetor com os coeficientes (numpy.array)
"""
    n = len(x)

    A = np.zeros([n, n])

    for i in range(n):
        for j in range(n):
            A[i, j] = x[i] ** j

    coeffs = np.linalg.solve(A, y)

    print(f"Os coeficientes do polinômio interpolador são: {coeffs}")
    return coeffs


if __name__ == "__main__":
    x = np.array([-1, 0, 2])
    y = np.array([4, 1, -1])
    vandermonde(x, y)
