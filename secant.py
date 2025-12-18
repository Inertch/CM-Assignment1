from functionsAndDerivatives import f


def secant(x0, x1, E, max_iter):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            return print("No convergence")
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(f(x2)) < E:
            return x2
        x0, x1 = x1, x2

    return x1
