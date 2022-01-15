def fixpt(g, x0, es, imax):
    xr = x0
    iter = 0
    while True:
        xr_old = xr
        xr = g(xr_old)
        iter += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        if ea < es or iter >= imax:
            break
    return xr


if __name__ == "__main__":
    import math

    gx = lambda x: math.e ** (-x)
    root = fixpt(gx, 0, 0.05, 15)

    print(root)