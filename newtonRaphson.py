from functionsAndDerivatives import f, df


def newton_raphson(x0, E, max_iter):
    x = x0
    for i in range(max_iter):
        if df(x) == 0:
            raise ValueError("No convergence")
        x_new = x - f(x) / df(x)
        if abs(f(x)) < E:
            return x_new
        x = x_new
    return x
