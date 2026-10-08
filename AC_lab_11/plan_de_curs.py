import ComplexPygame as C
import Color
import math


def Z_order():
    k = 6  # atentie: 0 < k < 15
    nrPuncte = 1 << (2 * k)
    lat = 1 << k
    C.setXminXmaxYminYmax(-1, lat, lat, -1)
    zvechi = 0
    for n in range(nrPuncte):
        x = 0
        y = 0
        nn = n
        for h in range(k):
            x |= (nn & 1) << h
            nn >>= 1
            y |= (nn & 1) << h
            nn >>= 1
        znou = complex(x, y)
        C.drawLine(znou, zvechi, Color.Index(n // 10))
        zvechi = znou
        if C.mustClose(): return


###############################################################
def HilbertPatrateIterate():
    class Patrat:
        def __init__(self, a, b, c, d):
            self.a, self.b, self.c, self.d = a, b, c, d

        def show(self, col):
            C.fillNgon([self.a, self.b, self.c, self.d], col)

        def centru(self):
            return (self.a + self.b + self.c + self.d) / 4

    def transforma(li):
        rez = []
        for P in li:
            mab, mbc, mcd, mda = (P.a + P.b) / 2, (P.b + P.c) / 2, (P.c + P.d) / 2, (P.d + P.a) / 2
            c0 = P.centru()
            rez.append(Patrat(P.a, mda, c0, mab))
            rez.append(Patrat(mab, P.b, mbc, c0))
            rez.append(Patrat(c0, mbc, P.c, mcd))
            rez.append(Patrat(mcd, c0, mda, P.d))
        return rez

    def traseaza(li):
        for k in range(len(li)):
            li[k].show(Color.Index(200 + k // 5))
            if C.mustClose(): return


    def liniaza(li):
        for k in range(1, len(li)):
            col = Color.Index(k // 5)
            C.drawLine(li[k - 1].centru(), li[k].centru(), col)
            if C.mustClose(): return

    C.setXminXmaxYminYmax(0, 10, 0, 10)
    C.fillScreen(Color.Navy)
    fig = [Patrat(1 + 1j, 1 + 9j, 9 + 9j, 9 + 1j)]
    # fig = [Patrat(0.5 + 1j, 1 + 9j, 7 + 8j, 9.5 + 1j)]
    nrEtape=5
    for k in range(nrEtape):
        fig = transforma(fig)
    traseaza(fig)
    liniaza(fig)


########################################################################
def LSistemHilbert():
    # S -- ocolire pe stanga
    # D -- ocolire pe dreapta
    # F -- salt in fata
    # + -- rotatie de +90
    # - -- rotatie de -90
    def generare(text):
        rez = ''
        for s in text:
            if s == 'S':
                rez += '+DF-SFS-FD+'
            elif s == 'D':
                rez += '-SF+DFD+FS-'
            else:
                rez += s
        return rez
    # simboluri interpretate: F + -
    def interpretare(z0, delta, text):
        C.fillScreen()
        for s in text:
            if s == 'F':
                C.drawLine(z0, z0 + delta, Color.Black)
                z0 += delta
            elif s == '+':
                delta *= 1j
            elif s == '-':
                delta *= -1j
            else:
                continue

    C.setXminXmaxYminYmax(0, 10, 0, 10)
    z0 = 1 + 1j
    delta = 8
    text = 'S'
    nrEtape = 5
    for k in range(nrEtape):
        print(f"k={k} text={text}")
        text = generare(text)
        text.replace('+-','')
    interpretare(z0, delta/2**nrEtape, text)

######################################################################
def HilbertRecursiv():
    za = 0
    zb = 0

    #   z0 = coltul curent
    #   d1 = prima deplasare
    #   d2 = a doua deplasare
    #  -d1 = a treia deplasare
    def genereaza(z0, d1, d2, niv):
        nonlocal za, zb
        if niv <= 0:
            zb = z0 + (d1 + d2) / 2  # zb = centrul patratului curent
            C.drawLine(za, zb, Color.Red)
            za = zb  # za = centrul vechi
        else:
            niv -= 1
            d1 *= 0.5
            d2 *= 0.5
            genereaza(z0, d2, d1, niv)
            genereaza(z0 + d1, d1, d2, niv)
            genereaza(z0 + d1 + d2, d1, d2, niv)
            genereaza(z0 + d1 + d2 + d2, -d2, -d1, niv)

    C.setXminXmaxYminYmax(-0.1, 1.1, -0.1, 1.1)
    z0 = 0
    d1 = 1j
    d2 = 1
    #   traseu prin patratul initial:
    #   z0 = coltul din stanga jos
    #   z0+d1 = coltul din stanga sus
    #   z0+d1+d2 = coltul din dreapta sus
    #   z0+d1+d2–d1 = z0+d2 = coltul din dreapta jos
    nrEtape = 5
    za = z0
    genereaza(z0, d1, d2, nrEtape)
    C.drawLine(za, z0 + d2, Color.Red)
    C.refreshScreen()


if __name__ == '__main__':
    C.initPygame()
    #C.run(Z_order)
    #C.run(HilbertPatrateIterate)
    C.run(LSistemHilbert)
    #C.run(HilbertRecursiv)
