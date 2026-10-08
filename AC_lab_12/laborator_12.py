import ComplexPygame as C
import Color
import math


####################################################
def Newton2():
    zStar1 = 1
    zStar2 = -1

    def f(z):  # f(z)=0.5*(z+1/z)
        if z == 0:
            return 1.0e100
        else:
            return 0.5 * (z + 1 / z)


    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            z = zeta
            for _ in range(nrIter):
                if C.rho(z - zStar1) < 0.1:
                    col = Color.Red
                    break
                if C.rho(z - zStar2) < 0.1:
                    col = Color.Blue
                    break
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose():
            return
    C.setAxis()
    C.refreshScreen()


####################################################


def Newton2ETA():
    zStar1 = 1
    zStar2 = -1

    def f(z):  # f(z)=0.5*(z+1/z)
        if z == 0:
            return 1.0e100
        else:
            return 0.5 * (z + 1 / z)

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if C.rho(z - zStar1) < 0.1 or C.rho(z - zStar2) < 0.1:
                    break
                z = f(z)
            C.setPixel(zeta, Color.Index(k * 50))
        if C.mustClose(): return
    C.refreshScreen()


####################################################

def Newton3():
    eps0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 3.0)
    eps1 = C.fromRhoTheta(1.0, 2.0 * math.pi / 3.0)
    eps2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 3.0)

    def f(z):
        if z == 0:
            return 1.0e100
        else:
            return (2 * z * z * z + 1) / (3 * z * z)

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            z = zeta
            for _ in range(nrIter):
                if C.rho(z - eps0) < 0.1:
                    col = Color.Darkblue
                    break
                if C.rho(z - eps1) < 0.1:
                    col = Color.Yellow
                    break
                if C.rho(z - eps2) < 0.1:
                    col = Color.Fuchsia
                    break
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose(): return
    C.setAxis(Color.White)
    C.refreshScreen()


####################################################

def Newton3ETA():
    eps0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 3.0)
    eps1 = C.fromRhoTheta(1.0, 2.0 * math.pi / 3.0)
    eps2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 3.0)

    def f(z):
        if z != 0:
            return (2 * z * z * z + 1) / (3 * z * z)
        else:
            return 1.0e100

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    C.fillScreen()
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if C.rho(z - eps0) < 0.1 or C.rho(z - eps1) < 0.1 or C.rho(z - eps2) < 0.1:
                    break
                z = f(z)
            C.setPixel(zeta, Color.Index(3 * k))
        if C.mustClose(): return
    C.refreshScreen()


####################################################

def Newton3TETA():
    eps0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 3.0)
    eps1 = C.fromRhoTheta(1.0, 2.0 * math.pi / 3.0)
    eps2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 3.0)

    def f(z):
        if z != 0:
            return (2 * z * z * z + 1) / (3 * z * z)
        else:
            return 1.0e100

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    C.fillScreen()
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            kol = 0
            z = zeta
            for k in range(nrIter):
                if C.rho(z - eps0) < 0.1:
                    kol = 100
                    break
                if C.rho(z - eps1) < 0.1:
                    kol = 200
                    break
                if C.rho(z - eps2) < 0.1:
                    kol = 300
                    break
                z = f(z)
            C.setPixel(zeta, Color.Index(10 * k + kol))
        if C.mustClose(): return
    C.refreshScreen()


####################################################

def Newton3GEN():
    eps0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 3.0)
    eps1 = C.fromRhoTheta(1.0, 2.0 * math.pi / 3.0)
    eps2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 3.0)

    def f(z):
        exp = 2.1  # +2.1 * i
        if z != eps0 and z != eps1 and z != eps2:
            w0 = exp / (z - eps0)
            w1 = exp / (z - eps1)
            w2 = exp / (z - eps2)
            return z - 1 / (w0 + w1 + w2)
        else:
            return 1.0e100

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    C.fillScreen()
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if C.rho(z - eps0) < 0.01 or C.rho(z - eps1) < 0.01 or C.rho(z - eps2) < 0.01:
                    break
                z = f(z)
            C.setPixel(zeta, Color.Index(775 + 4 * k))
        if C.mustClose(): return
    C.refreshScreen()


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


####################################################

def Newton6():
    omega0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 5.0)
    omega1 = C.fromRhoTheta(2.0, 2.0 * math.pi / 5.0)
    omega2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 5.0)
    omega3 = C.fromRhoTheta(2.0, 2.0 * math.pi / 5.0)
    omega4 = C.fromRhoTheta(1.0, 2.0 * math.pi / 5.0)
    omega = [omega0, omega1, omega2, omega3, omega4]

    def f(z):
        exp = C.fromRhoTheta(10.0, 0 * math.pi / 3)
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
                kol = 0
                for omg in omega:
                    kol += 100
                    if C.rho(z - omg) < 0.01:
                        amAjuns = True
                        break
                if amAjuns:
                    break
                z = f(z)
            C.setPixel(zeta, Color.Index(10 * k + kol))
        if C.mustClose(): return
    C.refreshScreen()


####################################################

def Newtonk():
    a0 = complex(0.3, 1.5)
    a1 = complex(1.1, 0.6)
    a2 = complex(-0.1, 0.6)
    a3 = complex(0.1, -1.6)
    a4 = complex(-1.1, -0.6)
    k0 = C.fromRhoTheta(2.3, 0.1)
    k1 = C.fromRhoTheta(1.2, 0.1)
    k2 = C.fromRhoTheta(1.3, 0.2)
    k3 = C.fromRhoTheta(1.0, 0.1)
    k4 = C.fromRhoTheta(2.1, 0.05)

    alist = [a0, a1, a2, a3, a4]
    klist = [k0, k1, k2, k3, k4]

    def f(z):
        if z in alist:
            return z
        else:
            w = [klist[h] / (z - alist[h]) for h in range(5)]
            return z - 1 / sum(w)

    C.setXminXmaxYminYmax(-3, 3, -3, 3)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for _ in range(nrIter):
                amAjuns = False
                kol = 0
                for ak in alist:
                    kol += 100
                    if C.rho(z - ak) < 0.01:
                        amAjuns = True
                        break
                if amAjuns:
                    break
                z = f(z)
            C.setPixel(zeta, Color.Index(kol))
        if C.mustClose():
            return
    C.refreshScreen()


####################################################

if __name__ == '__main__':
    C.initPygame()
    C.run(Newton2)
    # C.run(Newton2ETA)
    # C.run(Newton3)
    # C.run(Newton3ETA)
    # C.run(Newton3TETA)
    # C.run(Newton3GEN)
    # C.run(Newton5)
    # C.run(Newton6)
    # C.run(Newtonk)
