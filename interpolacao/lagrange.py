import numpy as np


def lagrange(x, y, x_ponto):
    n = len(x)

    valor_interpolado = 0

    for i in range(n):
        prod = 1
        for k in range(n):
            if k != i:
                prod *= (x_ponto - x[k]) / (x[i] - x[k])
        valor_interpolado += prod * y[i]

    return valor_interpolado


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x = np.array([-1, 0, 2])
    y = np.array([4, 1, -1])
    x_testes = np.linspace(-2, 3, 100)
    y_interpolado = list(map(lambda t: lagrange(x, y, t), x_testes))

    fig, ax = plt.subplots(1, 1)
    ax.scatter(x, y)
    ax.plot(x_testes, y_interpolado, "--c")
    plt.show()
