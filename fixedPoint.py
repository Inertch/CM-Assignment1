from functionsAndDerivatives import g


def fixed_point(x, E, max_iter):
    for i in range(max_iter):
        x1 = g(x)
        if abs(x1 - x) < E:
            return x1
        x = x1
    return x
