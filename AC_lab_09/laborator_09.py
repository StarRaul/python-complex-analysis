import ComplexPygame as C
import Color
import math

def Reziduuri():
    a, b = 0, 2 * math.pi
    p1 = 3 + 1j
    p2 = -1 + 3j

    def g(z):
        return z * z

    def f(z):
        if (z - p1) * (z - p2) == 0:
            return 0
        else:
            return g(z) / ((z - p1) * (z - p2))

    # def cercQr(q, r):
    #     return lambda t: q + C.fromRhoTheta(r, t)

    def cercQR(q, r):
        def gamma(t):
            return q + C.fromRhoTheta(r, t)

        return gamma

    def arataModulul(F):
        for z in C.screenAffixes():
            k = int(10 * C.rho(F(z)))
            C.setPixel(z, Color.Index(k))

    def arataIntegrala(F, Gamma):
        nrPasi = 5000
        dt = (b - a) / nrPasi
        # calculam suma Riemann-Stieltjes
        suma = 0
        z0 = Gamma(a)
        for k in range(1, nrPasi):
            z1 = Gamma(a + k * dt)
            suma += F(z1) * (z1 - z0)
            col = Color.Index(300 + k // 10)
            C.drawLine(0, suma, col)
            C.setPixel(z1, col)
            z0 = z1
            C.refreshScreen()
        return suma

    lat = 30
    C.setXminXmaxYminYmax(-lat, lat, -lat, lat)
    arataModulul(f)
    C.setAxis()
    q0 = 1 + 1j
    r0 = 5
    intRS = arataIntegrala(f, cercQR(q0, r0))
    sumaReziduuri = 0
    if C.rho(p1 - q0) < r0:
        sumaReziduuri += g(p1) / (p1 - p2)
    if C.rho(p2 - q0) < r0:
        sumaReziduuri += g(p2) / (p2 - p1)

    intTR = 2j * math.pi * sumaReziduuri
    C.setTextIJ(f"intRS = {intRS}", 10, 20, Color.White)
    C.setTextIJ(f"intTR = {intTR}", 10, 40, Color.White)

###################################################################
if __name__ == '__main__':
    C.initPygame()
    C.run(Reziduuri)

