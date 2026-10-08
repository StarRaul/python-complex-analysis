import cmath
import math


def mySqrt(z):
    rho = abs(z)
    theta = cmath.phase(z)
    return cmath.rect(math.sqrt(rho), theta / 2)


v = 2 + 5j
z = v ** 2
print(mySqrt(z))
print(cmath.sqrt(z))
print(z ** 0.5)


# (2+5j)
# (2+5j)
# (2+5j)

def ecGr2(a, b, c):
    pass
