import numpy as np


def simpson_repetida(a, b, f, n):
    """Calcula a integral definida pela regra de Simpson repetida.

    Parâmetros:
        [a] (float): Valor do limite de integração inferior.
        [b] (float): Valor do limite de integração superior.
        [f] (function): Integrando.
        [n] (int): Número par de intervalos igualmente espaçados.

    Retorno:
        Valor da integral definida (float)"""
    h = (b - a) / n

    x = np.arange(a, b + h, h)
    I = 0

    for i in range(0, n, 2):
        I += f(x[i]) + 4 * f(x[i + 1]) + f(x[i + 2])

    I = h * I / 3

    return I


if __name__ == "__main__":
    a = -1
    b = 1
    f = lambda x: 1 / (x + 2)
    n = 500
    I = simpson_repetida(a, b, f, n)
