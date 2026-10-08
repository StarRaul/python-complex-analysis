import ComplexPygame as C
import Color
import math
import random

from AC_lab_10_folder.ComplexPygame import fromRhoTheta


# Tema 10 ex. 1
def InsulaLuiVonKoch():
    theta = math.pi / 6
    ro = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(ro, theta)
    Lambda = 1 / 3.0

    def transforma(li):  # VonKoch
        z1 = li[0]
        rez = [z1]
        for z2 in li[1:]:
            delta = z2 - z1
            # Segmentul z1_z2 este inlocuit cu
            # z1_zA, zA_zB, zB_zC si zC_z2, unde
            # zA=z1 + Lambda* (z2 - z1)
            # zB=z1 + w * (z2 - z1))
            # zC=z1 + (1-Lambda) * (z2 - z1).
            rez.append(z1 + Lambda * delta)
            rez.append(z1 + w * delta)
            rez.append(z2 - Lambda * delta)
            rez.append(z2)
            z1 = z2
        return rez

    def traseaza(li):
        for k in range(1, len(li)):
            C.drawLine(li[k - 1], li[k], Color.Index(k // 500))
        return

    C.setXminXmaxYminYmax(-1, 1, -1, 1)
    N = 6
    alfa = 2 * math.pi / N
    fig = [C.fromRhoTheta(0.7, k * alfa) for k in range(N + 1)]


    for _ in range(6):
        fig = transforma(fig)

    omega = C.fromRhoTheta(0.99, math.pi / 360)

    for k in range(10000):
        for z in fig:
            C.setPixel(z, Color.Index(200 +  k))
        fig = [ z * omega for z in fig]
        if C.mustClose(): return
##################################################################
# Tema 10 ex. 8
def Pitagora():
    class PatratAB:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.c = b - 1j * (a - b)
            self.d = a + 1j * (b - a)

        def show(self, color):
            C.fillNgon([self.a, self.b, self.c, self.d], color)
            C.drawNgon([self.a, self.b, self.c, self.d], Color.Green)

    def transforma(li):
        # li este o lista de patrate
        rez = []
        for P in li:
            Lambda = (1 + random.random()) / 3
            zE = P.d + (P.c - P.d) * 0.6 + 1j * (P.c - P.d) * 0.6
            rez.append(PatratAB(P.d, zE))
            rez.append(PatratAB(zE, P.c))

        return rez

    C.setXminXmaxYminYmax(-10, 20, -10, 20)
    C.fillScreen()
    P0 = PatratAB(3.5 + 1j, 6.5 + 1j)
    lista = [P0]
    for k in range(10):
        for P in lista:
            P.show(Color.Index(50 * k))
        lista = transforma(lista)
        C.wait(100)
        if C.mustClose():
            return
    C.setText("A", P0.a - 0.2 - 0.1j)
    C.setText("B", P0.b + 0.2 - 0.1j)
    C.setText("C", P0.c + 0.2)
    C.setText("D", P0.d - 0.2)
    C.setText("E", (P0.d + P0.c) / 2)

########################################


if __name__ == '__main__':
    C.initPygame()
    #C.run(InsulaLuiVonKoch)
    C.run(Pitagora)
