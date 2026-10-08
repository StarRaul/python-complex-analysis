import ComplexPygame as C
import Color
import math

Directii = [-1 - 1j, -1, -1 + 1j, 1j, 1 + 1j, 1, 1 - 1j, -1j]

class Patrat:
    # q = centrul patratului
    # r = semilatura
    def __init__(self, q, r):
        self.q, self.r = q, r

    def show(self, col):
        C.fillNgon([self.q + self.r * u for u in Directii[::2]], col)

##############################################################################
def SierpinskiMotiveIterate():
    def transforma(li):
        # pentru fiecare patrat P, baza,
        # aplicam motivul de 8 ori
        return [Patrat(P.q + 2 * u * P.r / 3, P.r / 3) for P in li for u in Directii]

    def traseaza(li, col):
        C.fillScreen()
        for p in li:
            p.show(col)
            if C.mustClose():
                return

    C.setXminXmaxYminYmax(-1, 1, -1, 1)
    q0 = 0
    r0 = 1
    fig = [Patrat(q0, r0)]
    nrEtape = 5
    for _ in range(nrEtape):
        fig = transforma(fig)
    traseaza(fig, Color.Navy)

##########################################################################
def SierpinskiRecursiv():
    def deseneazaRec(P, niv):
        if C.mustClose():
            return
        if niv <= 0:
            P.show(Color.Darkcyan)
            return
        for u in Directii:
            deseneazaRec(Patrat(P.q + 2 * u * P.r / 3, P.r / 3), niv - 1)

    C.setXminXmaxYminYmax(-1, 1, -1, 1)
    C.fillScreen()
    q0 = 0
    r0 = 1
    niv = 5
    deseneazaRec(Patrat(q0, r0), niv)

######################################################################


def LSistemSierpinskiPeano():
    def arataPatrat(z0, delta):
        # diagonala z0z2 == delta
        z2 = z0 + delta
        z1 = z0 + delta * (1 + 1j) / 2
        z3 = z0 + delta * (1 - 1j) / 2  # z3 = z0 + z2 - z1
        C.fillNgon([z0, z1, z2, z3], Color.Indigo)

    # P = salt pe diagonala unui patrat Pastrat
    # E = salt peste patratul Eliminat
    # + = rotatie +90
    # - = rotatie -90

    def generare(text):
        rez = ''
        for s in text:
            if s == 'P':
                rez += 'P+P-P-P-E+P+P+P-P'
            elif s == 'E':
                rez += 'EEE'
            else:
                rez += s
        return rez

    def interpretare(z0, delta, text):
        C.fillScreen()
        for s in text:
            # if C.mustClose():return
            if s == 'P':
                arataPatrat(z0, delta)
                # C.drawLine(z0, z0 + delta, Color.Black)
                z0 += delta
            elif s == 'E':
                # C.drawLine(z0, z0 + delta, Color.Red)
                z0 += delta
            elif s == '+':
                delta *= 1j
            elif s == '-':
                delta *= -1j
            else:
                continue

    C.setXminXmaxYminYmax(0, 1, 0, 1)
    C.fillScreen()
    z0 = 0
    delta = 1 + 1j
    text = 'P'
    nrEtape = 5
    for k in range(nrEtape):
        text = generare(text)
        print(f"k={k} text={text}")
    interpretare(z0, delta / 3 ** nrEtape, text)

######################################################################
def SierpinskiTernar():
    # desenam patratul lui Sierpinski
    # prin scriere ternara x=0.cccccccccc
    C.setXminXmaxYminYmax(0, 1, 0, 1)
    C.fillScreen()
    for z in C.screenAffixes():
        x, y = z.real, z.imag
        nivMax = 5
        color = Color.Midnightblue
        for _ in range(nivMax):
            x *= 3
            y *= 3
            cx = int(x)  # cifra lui x de pe locul curent
            cy = int(y)  # cifra lui y de pe locul curent
            if cx == 1 and cy == 1:
                color = Color.White
                break
            x -= cx
            y -= cy
        C.setPixel(z, color)

################################################################


def Newton3():
    eps0 = C.fromRhoTheta(1.0, 0.0 * math.pi / 3.0)
    eps1 = C.fromRhoTheta(1.0, 2.0 * math.pi / 3.0)
    eps2 = C.fromRhoTheta(1.0, 4.0 * math.pi / 3.0)

    def f(z):
        return (2 * z * z * z + 1) / (3 * z * z) if z != 0 else 10e10

    c0 = 0
    r = 2
    C.setXminXmaxYminYmax(c0.real - r, c0.real + r, c0.imag - r, c0.imag + r)
    nrIter = 300
    for coloana in C.screenColumns():
        for zeta in coloana:
            col = Color.Black
            z = zeta
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
                z = f(z)
            C.setPixel(zeta, col)
        if C.mustClose(): return
    C.drawLine(c0 - r, c0 + r, Color.White)
    C.drawLine(c0 - r * 1j, c0 + r * 1j, Color.White)

##################################################################
def NewtonGeneral():
    # p(z)=(z-a1)**m1*(z-a2)**m2*...*(z-ak)**mk
    radacini = [C.fromRhoTheta(1, 2 * k * math.pi / 5) for k in range(5)]
    multipli = [2 + 1j for k in range(5)]

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

##########################################################
if __name__ == '__main__':
    C.initPygame()
    C.run(SierpinskiMotiveIterate)
    C.run(SierpinskiRecursiv)
    C.run(LSistemSierpinskiPeano)
    C.run(SierpinskiTernar)
    C.run(Newton3)
    C.run(NewtonGeneral)
