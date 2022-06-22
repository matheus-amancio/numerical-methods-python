import numpy as np


def trapezio_repetida(a, b, f, n):
    """Calcula a integral definida pela regra do trapézio repetida.

    Parâmetros:
        [a] (float): Valor do limite de integração inferior.
        [b] (float): Valor do limite de integração superior.
        [f] (function): Integrando.
        [n] (int): Número de intervalos igualmente espaçados.

    Retorno:
        Valor da integral definida (float)"""
    h = (b - a) / n

    x = np.arange(a, b + h, h)
    I = 0.5 * h * (f(x[0]) + 2 * f(x[1:-1]).sum() + f(x[-1]))

    return I


if __name__ == "__main__":
    a = -1
    b = 1
    f = lambda x: 1 / (x + 2)
    n = 500
    I = trapezio_repetida(a, b, f, n)
