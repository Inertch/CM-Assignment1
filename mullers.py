from functionsAndDerivatives import f
import cmath


def muller(x0, x1, x2, E, max_iter):
    global x3
    for i in range(max_iter):
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f(x1) - f(x0)) / h1
        delta2 = (f(x2) - f(x1)) / h2
        d = (delta2 - delta1) / (h2 + h1)

        a = d
        b = delta2 + h2 * d
        c = f(x2)

        rad = cmath.sqrt(b ** 2 - 4 * a * c)

        if abs(b + rad) > abs(b - rad):
            denom = b + rad
        else:
            denom = b - rad

        if denom == 0:
            return print("No convergence")

        x3 = x2 - (2 * c) / denom

        if abs(f(x3)) < E:
            return x3

        x0, x1, x2 = x1, x2, x3

    return x3
