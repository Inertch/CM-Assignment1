from newtonRaphson import newton_raphson
from bisection import bisection
from fixedPoint import fixed_point
from secant import secant

nrRoot = newton_raphson(1, 1e-3, 50)
print("Root with Newton-Raphson:", nrRoot)

bRoot = bisection(-4, 3, 1e-3, 50)
print("Root with bisection:", bRoot)

fpRoot = fixed_point(1, 1e-3, 50)
print("Root with fixed-point:", fpRoot)

sRoot = secant(1, 3, 1e-3, 50)
print("Root with Secant:", sRoot)
