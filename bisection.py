from functionsAndDerivatives import f


def bisection(a, b, E, max_iter):
    if (f(a) * f(b)) >= 0:
        return print("Incompatible points")
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < E or (b - a) / 2 < E:
            return c
        if (f(a) * f(c)) >= 0:
            a = c
        else:
            b = c
    return (a + b) / 2
