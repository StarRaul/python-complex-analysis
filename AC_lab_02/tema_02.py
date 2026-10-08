import ComplexPygame as C
import Color
import math, cmath, sys

def SpiralaLogaritmica():
    r = 1.1
    C.setXminXmaxYminYmax(-r, r, -r, r)
    C.fillScreen(Color.Azure)
    C.setAxis()
    a = -0.1
    b = 1
    lamb_da = a + b * 1j
    tmax = 50
    delta_t = 0.001
    t = 0
    while t < tmax:
        rho = math.exp(a * t)
        x = rho * math.cos(b * t)
        y = rho * math.sin(b * t)
        C.setPixelXY(x, y, Color.Red)
        if C.mustClose():
            break
        t += delta_t
    t = 0
    while t < tmax:
        z = C.fromRhoTheta(math.exp(a * t), b * t)
        C.setPixel(z, Color.Blue)
        if C.mustClose():
            break
        t += delta_t
    t = 0
    while t < tmax:
        z = cmath.exp(lamb_da * t)
        C.setPixel(z, Color.Black)
        if C.mustClose():
            break
        t += delta_t

    print("GATA!")


if __name__ == '__main__':
    C.initPygame()
    C.run(SpiralaLogaritmica)
