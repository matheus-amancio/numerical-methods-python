import numpy as np


def ajuste_polinomial(x, y, n=2):
    """Calcula os coeficientes de um polinômio de grau (n-1) que melhor se \
ajusta ao conjunto de pontos passado.

    Parâmetros:
        [x] (numpy.array): valores de x.
        [y] (numpy.array): valores de y ou f(x).
        [n] (int): Grau do polinômio desejado + 1.

    Retorno:
        Coeficientes do polinômio de ajuste (numpy.array)"""
    A = np.zeros([n, n])
    b = np.zeros(n)
    m = len(x)

    for i in range(n):
        for j in range(n):
            A[i, j] = 0
            for k in range(m):
                A[i, j] = A[i, j] + x[k] ** (i + j)
            A[j, i] = A[i, j]
        b[i] = 0
        for k in range(m):
            b[i] = b[i] + y[k] * x[k] ** (i)

    coeffs = np.linalg.solve(A, b)
    return coeffs


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x = np.array([0, 0.25, 0.5, 0.75, 1])
    y = np.array([1, 1.284, 1.6487, 2.117, 2.7183])
    coeffs_reta = ajuste_polinomial(x, y)
    coeffs_parabola = ajuste_polinomial(x, y, 3)

    x_teste = np.linspace(-1, 2, 100)

    # Ajuste com reta
    reta_ajustada = 0
    N = len(coeffs_reta)
    for i in range(N):
        reta_ajustada += coeffs_reta[i] * x_teste ** i

    # Ajuste com parábola
    parabola_ajustada = 0
    N = len(coeffs_parabola)
    for i in range(N):
        parabola_ajustada += coeffs_parabola[i] * x_teste ** i

    fig, ax = plt.subplots(1, 1)
    ax.scatter(x, y)
    ax.plot(x_teste, reta_ajustada, "--c")
    ax.plot(x_teste, parabola_ajustada, "--g")
    plt.show()
