def bisect(f, xl, xu, es, imax):
    iter = 0
    fl = f(xl)
    xr = 0
    while True:
        xr_old = xr
        xr = (xl + xu) / 2
        fr = f(xr)
        iter += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr)
        test = fl * fr
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
            fl = fr
        else:
            ea = 0
        if ea < es or iter >= imax:
            break
    return xr


if __name__ == "__main__":
    import math

    fc = lambda c: (9.81 * 68.1 / c) * (1 - math.exp(-c * 10 / 68.1)) - 40
    root = bisect(fc, 12, 16, 0.0005, 15)
    print(root, fc(root))
