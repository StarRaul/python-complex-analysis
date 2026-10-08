import ComplexPygame as C
import Color
import math

def Newton4():

    eps0 = C.fromRhoTheta(1.0, math.pi / 4)
    eps1 = C.fromRhoTheta(1.0, (math.pi + 2 * math.pi) / 4)
    eps2 = C.fromRhoTheta(1.0, (math.pi + 4 * math.pi) / 4)
    eps3 = C.fromRhoTheta(1.0, (math.pi + 6 * math.pi) / 4)

    def f(z):
        return (3*(z**4) - 1) / (4 * (z ** 3)) if z != 0 else 10e10 #(z * z * z * z + 1) / (3 * z * z)

    c0 = 0
    r = 2
    C.setXminXmaxYminYmax(c0.real - r, c0.real + r, c0.imag - r, c0.imag + r)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            if zeta !=0:
                z =  1 / zeta
            for _ in range(nrIter):
                if abs(z - eps0) < 0.1:
                    col = Color.Darkblue
                    break
                if abs(z - eps1) < 0.1:
                    col = Color.Yellow
                    break
                if abs(z - eps2) < 0.1:
                    col = Color.Fuchsia
                    break
                if abs(z - eps3) < 0.1:
                    col = Color.Green
                    break
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose(): return
    C.drawLine(c0 - r, c0 + r, Color.White)
    C.drawLine(c0 - r * 1j, c0 + r * 1j, Color.White)


####################################################

# de editat
def Newton44():
    eps0 = C.fromRhoTheta(1.0, math.pi / 4)
    eps1 = C.fromRhoTheta(1.0, (math.pi + 2 * math.pi) / 4)
    eps2 = C.fromRhoTheta(1.0, (math.pi + 4 * math.pi) / 4)
    eps3 = C.fromRhoTheta(1.0, (math.pi + 6 * math.pi) / 4)

    def f(z):
        return (3*(z**4) - 1) / (4 * (z ** 3)) if z != 0 else 10e10

    c0 = 0
    r = 2
    C.setXminXmaxYminYmax(c0.real - r, c0.real + r, c0.imag - r, c0.imag + r)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            if zeta !=0:
                z =  1 / zeta
            for _ in range(nrIter):
                if abs(z - eps0) < 0.1:
                    col = Color.Darkblue
                    break
                if abs(z - eps1) < 0.1:
                    col = Color.Yellow
                    break
                if abs(z - eps2) < 0.1:
                    col = Color.Fuchsia
                    break
                if abs(z - eps3) < 0.1:
                    col = Color.Green
                    break
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose(): return
    C.drawLine(c0 - r, c0 + r, Color.White)
    C.drawLine(c0 - r * 1j, c0 + r * 1j, Color.White)

####################################################

def NewtonWiki():
    # p(z)=(z-a1)**m1*(z-a2)**m2*...*(z-ak)**mk
    r2=math.sqrt(2)
    radacini = [+1,-1,1j,-1j,r2*(1+1j),r2*(1-1j),r2*(-1+1j),r2*(-1-1j)]
    multipli = [1,1,1,1,1,1,1,1]

    def f(z):
        if z in radacini:
            return z
        pprimpp = sum([mk / (z - ak) for mk, ak in zip(multipli, radacini)])
        return z - 1 / pprimpp if pprimpp != 0 else 10e10

    c0 = 0
    r = 0.8
    C.setXminXmaxYminYmax(c0.real - r, c0.real + r, c0.imag - r, c0.imag + r)
    nrIter = 300
    C.fillScreen(Color.Darkcyan)
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                amAjuns = False
                kol = 800
                for ak in radacini:
                    kol += 150
                    if abs(z - ak) < 0.01:
                        amAjuns = True
                        break
                if amAjuns: break
                z = f(z)
            C.setPixel(zeta, Color.Index(2 * k + kol))
        if C.mustClose(): return
    # C.drawLine(c0 - r, c0 + r, Color.White)
    # C.drawLine(c0 - r * 1j, c0 + r * 1j, Color.White)

####################################################


def Newton5():
    omega = [C.fromRhoTheta(1.0, 2 * k * math.pi / 5.0) for k in range(5)]

    def f(z):
        exp = C.fromRhoTheta(2.0, math.pi / 3)
        if z in omega:
            return 1.0e100
        w = [exp / (z - omg) for omg in omega]
        return z - 1 / sum(w)

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    C.fillScreen()
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                amAjuns = False
                for omg in omega:
                    if C.rho(z - omg) < 0.01:
                        amAjuns = True
                        break
                if amAjuns:
                    break
                z = f(z)
            C.setPixel(zeta, Color.Index(k))
        if C.mustClose(): return
    C.refreshScreen()


if __name__ == '__main__':
    C.initPygame()
    #C.run(Newton4)
    #C.run(Newton44)
    #C.run(NewtonWiki)
    C.run(Newton5)

