import numpy as np


def gauss_seidel(A, b, chute_inicial, tolerancia=1e-6, max_iter=20):
    """Resolve um sistema linear de forma aproximada usando \
o método de Gauss-Seidel.

    Parâmetros:
        [A] (numpy.array): Matriz triangular superior (coeficientes).
        [b] (numpy.array): Vetor das constantes.
        [chute_inicial] (numpy.array): Chute inicial do método iterativo.
        [tolerancia] (float): Critério de tolerância.
        [max_iter] (int): Número máximo de iterações permitidas.

    Retorno:
        Vetor com a solução (numpy.array)
"""
    n = len(A)
    x0 = chute_inicial

    n_iter = 0

    x = np.zeros(n)

    while True:
        for i in range(n):
            s0 = b[i]
            s1 = 0
            for j in range(i):
                s0 -= A[i, j] * x[j]
            for j in range(i + 1, n):
                s1 -= A[i, j] * x0[j]
            x[i] = (s0 + s1) / A[i, i]
        print(x)
        dist = np.linalg.norm(x - x0)
        if dist < tolerancia or n_iter > max_iter:
            break
        n_iter += 1
        x0 = np.copy(x)


if __name__ == "__main__":
    A = np.array([[3, 1, 1], [1, 4, 2], [0, 2, 5]])
    b = np.array([7, 4, 5])
    chute = np.array([0, 0, 0])
    gauss_seidel(A, b, chute)
