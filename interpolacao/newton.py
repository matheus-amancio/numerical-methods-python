import numpy as np


def newton(x, y, x_ponto):
    """Calcula o valor interpolado pelo Método de Newton.

    Parâmetros:
        [x] (numpy.array): valores de x.
        [y] (numpy.array): valores de y ou f(x).
        [x_ponto]: abscissa de interesse.

    Retorno:
        Valor interpolado (float)"""
    n = len(x)

    D = np.zeros([n, n])

    D[:, 0] = y

    for j in range(1, n):
        for i in range(j, n):
            D[i, j] = (D[i, j - 1] - D[i - 1, j - 1]) / (x[i] - x[i - j])

    valor_interpolado = 0

    for i in range(n):
        prod = 1
        for j in range(i):
            prod *= x_ponto - x[j]
        valor_interpolado += prod * D[i, i]

    return valor_interpolado


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x = np.array([-1, 0, 2])
    y = np.array([4, 1, -1])
    x_testes = np.linspace(-2, 3, 100)
    y_interpolado = list(map(lambda t: newton(x, y, t), x_testes))

    fig, ax = plt.subplots(1, 1)
    ax.scatter(x, y)
    ax.plot(x_testes, y_interpolado, "--c")
    plt.show()
