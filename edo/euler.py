import numpy as np


def euler(f, x, y0):
    """Calcula a pontos da solução de um PVI pelo Método de Euler.

    Parâmetros:
        [f] (function): f(x, y).
        [x] (numpy.array): Valores de x.
        [y0] (function): Valor de y da condição inicial.

    Retorno:
        Valores calculados para y (numpy.array)."""
    y = 0 * x
    y[0] = y0
    h = x[1] - x[0]
    n = len(x)

    for i in range(n - 1):
        y[i + 1] = y[i] + h * f(x[i], y[i])

    return y


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    f = lambda x, y: (np.exp(-x) - y) / 2
    h = 0.1
    x = np.arange(0, 1 + h, h)
    y0 = 0.5
    y_euler = euler(f, x, y0)

    fig, ax = plt.subplots(1, 1)

    ax.plot(x, y_euler)

    plt.show()
