from newtonRaphson import newton_raphson
from bisection import bisection


nrRoot = newton_raphson(1, 1e-3, 50)
print("Root with Newton-Raphson:", nrRoot)

bRoot = bisection(-4, 3, 1e-3, 50)
print("Root with bisection:", bRoot)
