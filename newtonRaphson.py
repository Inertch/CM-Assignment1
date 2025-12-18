from functionsAndDerivatives import f, df


def newton_raphson(x, E, max_iter):
    for i in range(max_iter):
        if df(x) == 0:
            return print("No convergence")
        x1 = x - f(x) / df(x)
        if abs(f(x)) < E:
            return x1
        x = x1
    return x
