import numpy as np


def newton_discreto(func, chute_inicial, tolerancia=1e-6, max_iter=20, h=0.01):
    """Resolve um sistema linear de forma aproximada usando \
o método de Newton Discreto.

    Parâmetros:
        [func] (function): Função de interesse.
        [chute_inicial] (numpy.array): Chute inicial do método iterativo.
        [tolerancia] (float): Critério de tolerância.
        [max_iter] (int): Número máximo de iterações permitidas.
        [h] (float): Incremento para avaliar a derivada.

    Retorno:
        Vetor com a solução (numpy.array)
"""
    x0 = chute_inicial

    f0 = func(*x0)

    if np.linalg.norm(f0) < tolerancia:
        x = x0
        print(f"A solução aproximada do sistema é o vetor: {x}")
        return x

    n = len(f0)

    jacob = np.zeros([n, n])

    n_iter = 0

    while True:
        for i in range(n):
            e = np.eye(1, n, i)[0]
            jacob[:, i] = (func(*(x0 + h * e)) - func(*x0)) / h
        s = np.linalg.solve(jacob, -1 * func(*x0))
        x = x0 + s
        print(x)
        dist = np.linalg.norm(x - x0)
        if dist < tolerancia or n_iter > max_iter:
            break
        n_iter += 1
        x0 = np.copy(x)

    print(f"A solução aproximada do sistema é o vetor: {x}")
    return x


if __name__ == "__main__":
    F = lambda x1, x2: np.array([x1 + x2 - 3, x1 ** 2 + x2 ** 2 - 9])
    J = lambda x1, x2: np.array([[1, 1], [2 * x1, 2 * x2]])
    chute = np.array([1, 5])
    newton_discreto(F, chute)
