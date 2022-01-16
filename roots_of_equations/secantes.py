# -*- encoding: utf-8 -*-


def secantes(func, x0, x1, tol, max_iter=16):
    """Implementação do método das secantes para a \
resolução de zero de função.

    Parâmetros:
        [func] (function): Função a qual se deseja obter zero.
        [x0] (float): Aproximação inicial.
        [x1] (float): Aproximação inicial.
        [tol] (float): Tolerância admissível.
        [max_iter] (int): Número máximo de iterações permitidas.

    Retorno:
        Zero da função.
    """
    if abs(func(x0)) < tol:
        print(f"{x0} é zero da função.")
        return x0
    if abs(func(x1)) < tol:
        print(f"{x1} é zero da função.")
        return x1
    x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
    if abs(func(x2)) < tol:
        print(f"{x2} é zero da função.")
        return x2
    iter = 0
    print(f"Iteração, x, f(x)")
    while abs(func(x2)) > tol and iter < max_iter:
        iter += 1
        print(f"{iter}, {x1}, {func(x1)}")
        x0 = x1
        x1 = x2
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
    iter += 1
    print(f"{iter}, {x2}, {func(x2)}")
    print(f"{x2} é zero da função.")
    return x2


if __name__ == "__main__":

    def f(x):
        return x ** 3 - 9 * x + 3

    secantes(f, 0, 1, 5e-4, 15)
