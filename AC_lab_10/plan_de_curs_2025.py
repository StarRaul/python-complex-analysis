import ComplexPygame as C
import Color
import math

def VonKoch():
    theta = math.pi / 6
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)
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
        C.fillScreen()
        for k in range(1, len(li)):
            C.drawLine(li[k - 1], li[k], Color.Black)
        C.refreshScreen()
        C.wait(50)

    C.setXminXmaxYminYmax(-1.1, 1.1, -0.5, 1.5)
    # segmentul initial
    fig = [-1, 1]
    nrEtape=6
    for _ in range(nrEtape):
        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose():  return

#########################################################

def VonKochTriunghiuri():
    theta = math.pi / 6
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)
    Lambda = 1 / 3.0

    class Triunghi:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def show(self, col):
            C.drawLine(self.a, self.b, col)
            C.drawLine(self.c, self.b, col)

        def fill(self, col):
            C.fillNgon([self.a, self.b, self.c], col)
            C.drawNgon([self.a, self.b, self.c], col)

    def transforma(li):  # VonKoch
        rez = []
        for t in li:
            z1, zB, z2 = t.a, t.b, t.c
            zA = z1 + Lambda * (z2 - z1)
            zC = z1 + (1 - Lambda) * (z2 - z1)
            rez.append(Triunghi(z1, zA, zB))
            rez.append(Triunghi(zB, zC, z2))
        return rez

    def traseaza(li, col):
        # C.fillScreen()
        for t in li:
            t.fill(col)
            t.show(Color.Black)

    C.setXminXmaxYminYmax(-2, 2, -1, 3)
    # triunghiul initial
    z1 = -1.9
    z2 = +1.9
    zB = z1 + w * (z2 - z1)
    fig = [Triunghi(z1, zB, z2)]
    kmax = 12
    for k in range(kmax):
        traseaza(fig, Color.Index(50 * k + 100))
        fig = transforma(fig)
        if C.mustClose():
            return
        C.wait(50)

################################################################



def Lindenmayer():
    alfa = math.pi / 3
    omegaS = C.fromRhoTheta(1, alfa)
    omegaD = C.fromRhoTheta(1, -alfa)

    def generare(text):
        rez = ''
        for s in text:
            if s == 'F':
                rez += 'FSFDDFSF'
            elif s == 'S':
                rez += 'S'
            elif s == 'D':
                rez += 'D'
            else:
                break
        return rez

    def interpretare(z0, delta, text):
        for s in text:
            if s == 'F':
                C.drawLine(z0, z0 + delta, Color.Black)
                z0 += delta
            elif s == 'S':
                delta *= omegaS
            elif s == 'D':
                delta *= omegaD
            else:
                return

    C.setXminXmaxYminYmax(-1.1, 1.1, -0.5, 1.5)
    z0 = -1
    delta = 2
    text = 'F'
    nrEtape = 6
    for k in range(nrEtape):
        C.fillScreen()
        print(f"k={k}")
        print(text)
        interpretare(z0, delta, text)
        C.refreshScreen()
        text = generare(text)
        delta /= 3
        C.wait(100)

######################################################################

def VonKochRecursiv():
    theta = math.pi / 6
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)
    Lambda = 1 / 3.0

    def aplicaMotiv(z1, z2, nivel):
        if nivel <= 0:
            # trasam numai curba finala
            C.drawLine(z1, z2, Color.Navy)
            return

        zA = z1 + Lambda * (z2 - z1)
        zB = z1 + w * (z2 - z1)
        zC = z1 + (1 - Lambda) * (z2 - z1)
        nivel -= 1
        aplicaMotiv(z1, zA, nivel)
        aplicaMotiv(zA, zB, nivel)
        aplicaMotiv(zB, zC, nivel)
        aplicaMotiv(zC, z2, nivel)

    C.setXminXmaxYminYmax(-1.1, 1.1, -0.5, 1.5)
    z1 = -1
    z2 = 1
    nrEtape = 6
    aplicaMotiv(z1, z2, nrEtape)
    C.refreshScreen()

#############################################################
def VonKochRecursivList():
    theta = math.pi / 6
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)
    Lambda = 1 / 3.0
    li = []

    def aplicaMotiv(z1, z2, nivel):
        # nu trimitem lista prin referinta
        # pentru ca nu o schimbam ci numai o completam,
        # o singura data, pe nivelul 0
        if nivel <= 0:
            li.append(z2)
            return

        zA = z1 + Lambda * (z2 - z1)
        zB = z1 + w * (z2 - z1)
        zC = z1 + (1 - Lambda) * (z2 - z1)
        nivel -= 1
        aplicaMotiv(z1, zA, nivel )
        aplicaMotiv(zA, zB, nivel )
        aplicaMotiv(zB, zC, nivel )
        aplicaMotiv(zC, z2, nivel )

    def traseaza(li):

        C.fillScreen()
        for k in range(1, len(li)):
            C.drawLine(li[k - 1], li[k], Color.Navy)
        #  C.wait(0.5)

    C.setXminXmaxYminYmax(-1.1, 1.1, -0.5, 1.5)
    z1 = -1
    z2 = 1
    li.append(z1)
    nrEtape = 6
    aplicaMotiv(z1, z2, nrEtape)
    traseaza(li)
    C.refreshScreen()



##########################################################################

if __name__ == '__main__':
    C.initPygame()
    C.run(VonKoch)
    C.run(VonKochTriunghiuri)
    C.run(Lindenmayer)
    C.run(VonKochRecursiv)
    C.run(VonKochRecursivList)
