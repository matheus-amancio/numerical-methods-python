# -*- encoding: utf-8 -*-

def bissecao(func, a, b, tol, max_iter=16):
    """Implementação do método da bisseção para a \
resolução de zero de função.

    Parâmetros:
        [func] (function): Função a qual se deseja obter zero.
        [a] (float): Extremidade esquerda do intervalo.
        [b] (float): Extremidade direita do intervalo.
        [tol] (float): Tolerância admissível.
        [max_iter] (int): Número máximo de iterações permitidas.

    Retorno:
        Zero da função.
    """
    if func(a) == 0:
        print(f'{a} é zero da função.')
        return a
    if func(b) == 0:
        print(f'{b} é zero da função.')
        return b
    if func(a)*func(b) < 0:
        ze = (a + b) / 2
        if abs(func(ze)) < tol:
            print(f'{ze} é zero da função.')
            return ze
        iter = 0
        print(f'Iteração, x, f(x)')
        while abs(func(ze)) > tol and iter < max_iter:
            iter += 1
            print(f'{iter}, {ze}, {func(ze)}')
            if func(a)*func(ze) < 0:
                b = ze
            elif func(ze)*func(b) < 0:
                a = ze
            ze = (a + b) / 2
        iter += 1
        print(f'{iter+1}, {ze}, {func(ze)}')
        print(f'{ze} é zero da função.')
        return ze
    else:
        print('Escolha outro intervalo.')


if __name__ == '__main__':
    def f(x): return x**3 - 9*x + 3
    bissecao(f, 0, 1, 1e-3, 15)
