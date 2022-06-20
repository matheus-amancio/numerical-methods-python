import numpy as np


def newton(func, jacob, chute_inicial, tolerancia=1e-6, max_iter=20):
    """Resolve um sistema linear de forma aproximada usando \
o método de Newton Modificado.

    Parâmetros:
        [func] (function): Função de interesse.
        [jacob] (function): Jacobiana da função.
        [chute_inicial] (numpy.array): Chute inicial do método iterativo.
        [tolerancia] (float): Critério de tolerância.
        [max_iter] (int): Número máximo de iterações permitidas.

    Retorno:
        Vetor com a solução (numpy.array)
"""
    x0 = chute_inicial

    if np.linalg.norm(func(*x0)) <= tolerancia:
        x = x0
        print(f"A solução aproximada do sistema é o vetor: {x}")
        return x

    n_iter = 0

    J0 = jacob(*x0)

    while True:
        s = np.linalg.solve(J0, -1 * func(*x0))
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
    newton(F, J, chute)
