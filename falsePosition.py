from functionsAndDerivatives import f


def false_position(a, b, E, max_iter):
    if f(a) * f(b) >= 0:
        return print("Invalid interval: f(a) and f(b) must have opposite signs")

    for i in range(max_iter):
        c = b - f(b) * (b - a) / (f(b) - f(a))

        if abs(f(c)) < E:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c
