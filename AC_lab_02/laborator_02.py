import ComplexPygame as C
import Color
import math
from random import *


def Sablon2():
    def unCercQRN(q=0j, r=1.0, N=1000):
        delta = 2 * math.pi / N
        return [q + C.fromRhoTheta(r, k * delta) for k in range(N)]

    # animatia:
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen(Color.Navy)
    fig = unCercQRN(5j, 4)
    omega = C.fromRhoTheta(1, math.pi / 1200)
    for k in range(10 ** 10):
        fig = [z * omega for z in fig]
        C.setNgon(fig, Color.Index(k // 10))
        C.drawNgon(fig, Color.Index(k//10))
        # C.fillNgon(fig, Color.Index(k // 10))
        if C.mustClose():
            break

    C.setAxis(Color.White)

###################################################################


def DiscuriColorate():
    C.setXminXmaxYminYmax(-1, 1, -1, 1)
    r0 = 0.5
    nrCercuri = randint(5, 12)
    delta = 2 * math.pi / nrCercuri
    centre = [C.fromRhoTheta(r0, k * delta) for k in range(nrCercuri)]
    for z in C.screenAffixes():
        niv = 700  # randint(675, 725)
        for z0 in centre:
            if C.rho(z - z0) <= r0:
                niv += 100
        C.setPixel(z, Color.Index(niv + int(300 * C.rho(z))))
    C.refreshScreen()


##########################################################
def Pixeli():
    xq = 4
    yq = 3
    r = 5
    q = xq + yq * 1j
    C.fillScreen(Color.Navy)
    C.setXminXmaxYminYmax(xq - 2 * r, xq + 2 * r, yq - 2 * r, yq + 2 * r)
    C.setAxis(Color.White)
    for col in C.screenColumns():
        for z in col:
            H, K = C.getHK(z)
            esteSus = (z.imag > 0)
            esteLaDreapta = (z.real > 0)
            esteInDisc = (C.rho(z - q) < r)
            if esteSus:
                col = Color.Skyblue if esteLaDreapta else Color.Deepskyblue
            else:
                col = Color.Darkturquoise if esteLaDreapta else Color.Lightseagreen
            if esteInDisc:
                col = Color.Index(100 + K // 2) if esteSus else Color.Index(600 + K)
            C.setPixel(z, col)
        if C.mustClose():
            return
    C.drawLine(q + r, q - r, Color.Magenta)
    C.drawLine(q + r * 1j, q - r * 1j, Color.Yellow)
    C.setAxis(Color.Midnightblue)


##########################################################

def CurbeLissajous():
    C.fillScreen(Color.Navy)
    C.setXminXmaxYminYmax(-1.3, 1.3, -1.3, 1.3)
    omega1 = 0.001
    omega2 = 1.5005 * omega1
    fi = 0.1
    for t in range(10 ** 10):
        x = math.sin(omega1 * t)
        y = math.sin(omega2 * t + fi)
        C.setPixelXY(x, y, Color.Index(t // 5000))
        if t % 10000 == 0 and C.mustClose():
            break
    print(f"GATA")


#############################################################


def SistemDinamic():
    def PunctAleator():
        hz = randint(0, C.dim)
        kz = randint(0, C.dim)
        return C.getZ(hz, kz), Color.Index((hz + kz) // 2 + randint(1, 100))

    def UnPas(puncte):
        # nonlocal a, b, c, d, h
        for k in range(len(puncte)):
            zVechi, cVechi = puncte[k]
            xv = zVechi.real
            yv = zVechi.imag
            xn = xv + h * math.sin(a * xv + b * yv)
            yn = yv + h * math.sin(c * xv + d * yv)
            zNou = complex(xn, yn)
            if abs(zNou) < raza and abs(zNou - zVechi) > 1.0e-4:
                puncte[k] = (zNou, cVechi)
            else:
                puncte[k] = PunctAleator()

            C.setPixel(*puncte[k])
        return

    # animatia:
    a = -10.0
    b = 1.0
    c = -1.0
    d = 10.0
    h = 0.005
    raza = 2.0
    C.fillScreen(Color.Navy)
    C.setXminXmaxYminYmax(-raza / 2, raza / 2, -raza / 2, raza / 2);
    nrPuncte = 10000
    tab = [PunctAleator() for k in range(nrPuncte)]
    while not C.mustClose():
        C.fillScreen(Color.Navy)
        UnPas(tab)
    return


###################################################################


if __name__ == '__main__':
    C.initPygame()
    C.run(Sablon2)
    C.run(DiscuriColorate)
    C.run(Pixeli)
    C.run(CurbeLissajous)
    C.run(SistemDinamic)
