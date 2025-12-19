from functionsAndDerivatives import g


def fixed_point(x, E, max_iter):
    for i in range(max_iter):

        if abs(g(x) - x) < E:
            return g(x)
        x = g(x)
    return x
