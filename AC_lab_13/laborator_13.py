import ComplexPygame as C
import Color
import random, math


####################################################
def JuliaRandom():
    c = 0.45 + 0.2j
    rhoMax = 1.0e20

    def f(z):
        # f(z)=(z*z*z+c)/(z*z*z-c)
        u = z * z * z
        if u == c:
            return rhoMax
        else:
            return (u + c) / (u - c)

    def zar():
        return random.uniform(-0.5, 0.5)

    C.setXminXmaxYminYmax(-2.7, 3.5, -3.1, 3.1)
    C.fillScreen()
    prec = 0.01
    nrIter = 100
    for coloana in C.screenColumns():
        for zeta in coloana:
            z1 = zeta + prec * complex(zar(), zar())
            z2 = zeta + prec * complex(zar(), zar())
            for k in range(nrIter):
                z1 = f(z1)
                z2 = f(z2)
                if C.rho(z1) + C.rho(z2) >= rhoMax:
                    break

            col = Color.White
            if C.rho(z1) >= rhoMax and C.rho(z2) >= rhoMax \
                    or C.rho(z1 - z2) < prec:
                col = Color.Red
            C.setPixel(zeta, col)
        if C.mustClose():
            return


####################################################
def JuliaGreen():
    c = complex(0.45, 0.2)
    rhoMax = 1.0e20

    def f(z):
        # f(z)=(z*z*z+c)/(z*z*z-c)
        u = z * z * z
        if u == c:
            return rhoMax
        else:
            return (u + c) / (u - c)

    C.setXminXmaxYminYmax(-2.7, 3.5, -3.1, 3.1)
    nrIter = 1000
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                z = f(z)
                if C.rho(z) >= rhoMax: break
            C.setPixel(zeta, Color.Index(sum(C.getHK(z))))
        if C.mustClose():
            return


####################################################
def JuliaPlina():
    c = complex(-0.4538, 0.55946)

    def f(z):
        return z * z + c

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    nrIter = 1001
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if C.rho(z) > 4: break
                z = f(z)
            C.setPixel(zeta, Color.Index(775 + k))
        if C.mustClose():
            return


####################################################
def JuliaNewton():
    eps0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 3.0)
    eps1 = C.fromRhoTheta(1.0, 2.0 * math.pi / 3.0)
    eps2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 3.0)
    omega = 0.54 + 0.5j

    def f(z):
        if z in [eps0, eps1, eps2]:
            return z
        w0 = omega / (z - eps0)
        w1 = omega / (z - eps1)
        w2 = omega / (z - eps2)
        return z - 1 / (w0 + w1 + w2)

    C.setXminXmaxYminYmax(-1000.5, 1000.5, -1000.5, 1000.5)
    prec = 0.001
    nrIter = 10000
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                z = f(z)
                if C.rho(z - eps0) < prec \
                        or C.rho(z - eps1) < prec \
                        or C.rho(z - eps2) < prec:
                    break
            C.setPixel(zeta, Color.Index(635 + 5 * k // 2))
        if C.mustClose():
            return


####################################################
def JuliaRetro():  # f(z) = z * z + c
    c = -0.4538 + 0.55946j

    def Sqrt(z):
        a = z.real
        b = z.imag
        if b == 0.0:
            if a >= 0.0:
                return complex(math.sqrt(a), 0.0)
            else:
                return complex(0.0, math.sqrt(-a))
        else:
            w = math.sqrt(a * a + b * b)
            if b >= 0.0:
                return complex(math.sqrt((w + a) / 2.0),
                               math.sqrt((w - a) / 2.0))
            else:
                return complex(-math.sqrt((w + a) / 2.0),
                               math.sqrt((w - a) / 2.0))

    # def Sqrt(z):
    #    return C.fromRhoTheta(math.sqrt(C.rho(z), C.theta(z)/2)
    #
    # def Sqrt(z):
    #     return pow(z, 0.5)

    def trans_total(li):
        rez = []
        for z in li:
            rez.append(Sqrt(z - c))
            rez.append(-Sqrt(z - c))
        return rez

    def trans_random(li):
        rez = []
        for z in li:
            C.setPixel(z, Color.Black)
            if random.random() < 0.5:
                rez.append(Sqrt(z - c))
            else:
                rez.append(-Sqrt(z - c))
        return rez

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    delta = Sqrt(1 - 4 * c)
    fig = [(1 + delta) / 2, (1 - delta) / 2]
    for k in range(15):
        fig = trans_total(fig)
    for k in range(1000):
        fig = trans_random(fig)
        if k % 10 == 0 and C.mustClose():
            return


####################################################

if __name__ == '__main__':
    C.initPygame()
    C.run(JuliaRandom)
    # C.run(JuliaGreen)
    # C.run(JuliaPlina)
    # C.run(JuliaNewton)
    # C.run(JuliaRetro)
