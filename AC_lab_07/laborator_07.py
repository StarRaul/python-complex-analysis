import ComplexPygame as C
import Color
import math


def FormulaLuiCauchy():
    unuPe2iPi = 1.0 / (2j * math.pi)
    a = 0
    b = 2 * math.pi

    def gamma(t):
        return C.fromRhoTheta(ro, t)

    def f(z):
        return z * z * z + 1 / (z - 10)
        #return z * z * z + 1 / (z - 1)

    def arataMod(h, k, z):
        kol = int(100 * abs(z))
        C.setPixelHK(h, k, Color.Index(kol))

    def arataArg(h, k, z):
        kol = int(512 * (1 + C.theta(z) / math.pi))
        C.setPixelHK(h, k, Color.Index(kol))

    def fCauchy(zstar):
        # calculam suma Riemann-Stieltjes
        # pentru g(z)=f(z)/(z-zstar)

        suma = 0
        zvechi = gamma(a)
        tk = a
        while tk <= b:
            tk += 0.01
            zk = gamma(tk)
            suma += f(zk) * (zk - zvechi) / (zk - zstar)
            zvechi = zk
        return unuPe2iPi * suma

    ro = 2.0
    rplus = ro + 0.1
    C.setXminXmaxYminYmax(-rplus, rplus, -rplus, rplus)
    ScreenColor = Color.Index(0)
    C.fillScreen(ScreenColor)
    C.setAxis()
    dim2 = C.dim // 2

    for h in range(dim2):
        for k in range(dim2):
            z = C.getZ(2 * h, 2 * k)
            if C.rho(z) >= ro:
                continue
            fExact = f(z)
            fAprox = fCauchy(z)

            arataArg(h, k, fExact)
            arataMod(h, k + dim2, fExact)

            arataArg(h + dim2, k, fAprox)
            arataMod(h + dim2, k + dim2, fAprox)
        if C.mustClose():
            return
    C.setAxis()


###################################################################
if __name__ == '__main__':
    C.initPygame()
    C.run(FormulaLuiCauchy)
