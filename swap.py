# module swap
''' swapRows(v, i, j).
    Troca linhas i e j de uma matriz ou vetor [v].

    swapCols(v, i, j).
    Troca colunas de uma matriz [v].
'''


def swapRows(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]


def swapCols(v, i, j):
    v[:, [i, j]] = v[:, [j, i]]
