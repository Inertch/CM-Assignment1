def f(x):
    return x**2 - 2


def df(x):
    return x*2


def newton_raphson(x0, E, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No convergence.")
        x_new = x - fx/dfx
        print(f"Iter {i + 1}: {x}")
        if abs(fx) < E:
            return x_new
        x = x_new
    return x


# Example usage
root = newton_raphson(1.0, 1e-3, 50)
print("Root:", root)
