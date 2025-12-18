from mullers import muller
from newtonRaphson import newton_raphson
from bisection import bisection
from fixedPoint import fixed_point
from secant import secant
from falsePosition import false_position


nrRoot = newton_raphson(1, 1e-3, 50)
print("Root with Newton-Raphson:", nrRoot)

bRoot = bisection(-4, 3, 1e-3, 50)
print("Root with bisection:", bRoot)

fpRoot = fixed_point(1, 1e-3, 50)
print("Root with fixed-point:", fpRoot)

sRoot = secant(1, 3, 1e-3, 50)
print("Root with Secant:", sRoot)

fpRoot = false_position(-4, 3, 1e-3, 50)
print("Root with false position:", fpRoot)

mRoot = muller(-4, -3, -2, 1e-3, 50)
print("Root with Muller's:", mRoot)
