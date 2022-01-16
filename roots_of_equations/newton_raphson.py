# -*- encoding: utf-8 -*-


def newton_raphson(func, diff, x0, tol, max_iter=16):
    """Implementação do método do ponto fixo para a \
resolução de zero de função.

    Parâmetros:
        [func] (function): Função a qual se deseja obter zero.
        [diff] (function): Derivada da função a qual se deseja obter zero.
        [x0] (float): Aproximação inicial.
        [tol] (float): Tolerância admissível.
        [max_iter] (int): Número máximo de iterações permitidas.

    Retorno:
        Zero da função.
    """
    if abs(func(x0)) < tol:
        print(f"{x0} é zero da função.")
        return x0
    x1 = x0 - func(x0) / diff(x0)
    if abs(func(x1)) < tol:
        print(f"{x1} é zero da função.")
        return x1
    iter = 0
    print(f"Iteração, x, f(x)")
    while abs(func(x1)) > tol and iter < max_iter:
        iter += 1
        print(f"{iter}, {x1}, {func(x1)}")
        x0 = x1
        x1 = x0 - func(x0) / diff(x0)
    iter += 1
    print(f"{iter}, {x1}, {func(x1)}")
    print(f"{x1} é zero da função.")
    return x1


if __name__ == "__main__":

    def f(x):
        return x ** 3 - 9 * x + 3

    def df(x):
        return 3 * x ** 2 - 9

    newton_raphson(f, df, 0.5, 1e-4, 15)
