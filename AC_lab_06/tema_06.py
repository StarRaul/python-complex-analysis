import ComplexPygame as C
import Color
import math

from AC_lab_06_folder.ComplexPygame import fillNgon


def Exemplu():
    C.setXminXmaxYminYmax(-3, 3, 0, 6)
    zA, zB, zC = 1.5 + 5j, -2 + 1j, 2 + 1j
    a = C.rho(zC - zB)
    omegaA = (zC - zA) / (zB - zA)
    uA = abs(C.theta(omegaA))
    C.drawNgon([zA, zB, zC], Color.Navy)
    C.setText("A", zA)
    C.setText("B", zB - 0.1)
    C.setText("C", zC + 0.1)
    C.setTextIJ(f"lungimea BC = {a:.3f} metri", 10, 30)
    C.setTextIJ(f"unghiul A = {uA:.3f} radiani", 10, 50)

###########################################################################
def BazaUnghiLatura():
    def bazaUnghiLatura(zB, zC, uB, c, peStg=True):  # returneaza varful zA
        if not peStg:
            uB = -uB
        a = C.rho(zC - zB)
        omegaB = C.fromRhoTheta(c / a, uB)
        return zB + omegaB * (zC - zB)

    C.setXminXmaxYminYmax(-5, 5, -5, 5)
    C.fillScreen()
    zB = -3 - 1j
    zC = 1.5
    uB = math.pi / 7
    c = 7.5
    C.drawLine(zB, zC, Color.Red)
    zA = bazaUnghiLatura(zB, zC, uB, c)
    C.drawLine(zB, zA, Color.Green)
    C.drawLine(zC, zA, Color.Green)
    zA = bazaUnghiLatura(zB, zC, uB, c, False)
    C.drawLine(zB, zA, Color.Magenta)
    C.drawLine(zC, zA, Color.Magenta)
    C.setAxis()

###########################################################################

def PentagoaneExterioare():
    def bazaApex(zB, zC, uA, peStg=True):
        """
        calculeaza apexul zA al triunghiului isoscel zB zA zC
        """
        omegaA = C.fromRhoTheta(1, uA)
        if not peStg:
            omegaA = omegaA.conjugate()
        return (zC - omegaA * zB) / (1 - omegaA)

    def transformaPoligon(p, col):  # pentagonul p trece in rez
        N = len(p)
        rez = [None] * N
        for k in range(N - 1):
            rez[k] = bazaApex(p[k], p[k + 1], math.pi / 3, False)
            C.fillNgon([p[k], p[k + 1], rez[k]], col)
            C.drawNgon([p[k], p[k + 1], rez[k]], Color.Navy)
        rez[N - 1] = rez[0]
        return rez

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen()
    N = 5
    delta = 2 * math.pi / N
    q = 0
    a = -1.5j
    pp = [q + C.fromRhoTheta(1, k * delta) * (a - q) for k in range(N + 1)]
    for k in range(3):
        pp = transformaPoligon(pp, Color.Index(100 + 20 * k))
    return
###########################################################################

def Desen():
    def unPatrat(a,b, color):
        #d = a + 1j * (b - a)
        #c = b - 1j * (a - b)
        d = a + (b - a) * 1j
        c = d + b - a
        C.fillNgon([a, b, c, d], color)
        return (a + c) / 2
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    a = 3 + 1j
    b = 5 + 3j
    l = 3 + 3j
    m = 5 + 4j
    n = 6 + 6j
    o = l + n - m
    c1 = unPatrat(m, l, Color.Black)
    c2 = unPatrat(l, o, Color.Blue)
    c3 = unPatrat(o, n, Color.Yellow)
    c4 = unPatrat(n, m, Color.Magenta)
    C.fillNgon([c1, c2, c3, c4], Color.Red)
    C.refreshScreen()


def BazaUnghiLatura():
    def bazaUnghiLatura(zB, zC, uB, uC, peStg=True): # returneaza varful zA
        if not peStg:
            uB = -uB
        a = C.rho(zC - zB)
        omegaB = C.fromRhoTheta(math.sin(uC)/math.sin(uC),uB)
        return zB + omegaB * (zC - zB)
    for t in range(1,100):
        C.setXminXmaxYminYmax(-15, 15, -15, 15)
        C.fillScreen()
        zB = -3-4j
        zC = 3-3j
        uB = math.acos(1/t)
        c = t
        C.drawLine(zB, zC, Color.Red)
        zA = bazaUnghiLatura(zB, zC, uB, c)
        C.drawLine(zB, zA, Color.Green)
        C.drawLine(zC, zA, Color.Green)
        zA = bazaUnghiLatura(zB, zC, uB, c, False)
        C.setAxis()


if __name__ == '__main__':
    C.initPygame()
    #C.run(Exemplu)
    # C.run(BazaUnghiLatura)
    # C.run(PentagoaneExterioare)
    #C.run(Desen)
    C.run(BazaUnghiLatura)

