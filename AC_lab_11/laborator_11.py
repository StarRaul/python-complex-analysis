import ComplexPygame as C
import Color
import math




def CurbaLuiLebesgue():
    c0 = (1 + 1j) / 2
    c1 = (1 + 1j) / 4
    c2 = (1 + 3j) / 4
    c3 = (3 + 3j) / 4
    c4 = (3 + 1j) / 4

    def s1(z):
        return c1 + 0.5 * (z - c0)
    def s2(z):
        return c2 + 0.5 * (z - c0)
    def s3(z):
        return c3 + 0.5 * (z - c0)
    def s4(z):
        return c4 + 0.5 * (z - c0)

    def transforma(li):
        rez = []
        for z in li:    rez.append(s2(z))
        for z in li:    rez.append(s3(z))
        for z in li:    rez.append(s1(z))
        for z in li:    rez.append(s4(z))
        return rez

    def traseaza(li):
        C.fillScreen()
        #  trasam chenarul
        C.drawNgon([0, 1, 1 + 1j, 1j], Color.Index(500))
        #  desenam curba curenta
        for n in range(1, len(li)):
            C.drawLine(li[n - 1], li[n], Color.Index(n // 5))

    C.setXminXmaxYminYmax(-0.1, 1.1, -0.1, 1.1)
    fig = [c0]
    nrEtape=4
    for k in range(nrEtape):
        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose(): return
        C.wait(100)


####################################################

def CurbaLuiHilbert():
    c0 = (1 + 1j) / 2
    c1 = (1 + 1j) / 4
    c2 = (1 + 3j) / 4
    c3 = (3 + 3j) / 4
    c4 = (3 + 1j) / 4

    def s1(z):
        return c1 + 0.5j * (z - c0).conjugate()

    def s2(z):
        return c2 + 0.5 * (z - c0)

    def s3(z):
        return c3 + 0.5 * (z - c0)

    def s4(z):
        return c4 - 0.5j * (z - c0).conjugate()

    def transforma(li):

        rez = []
        for z in li:
            rez.append(s1(z))
        for z in li:
            rez.append(s2(z))
        for z in li:
            rez.append(s3(z))
        for z in li:
            rez.append(s4(z))
        return rez

    def traseaza(li):
        C.fillScreen()
        #  trasam chenarul
        C.drawNgon([0, 1, 1 + 1j, 1j], Color.Index(500))
        #  desenam curba curenta
        for n in range(1, len(li)):
            C.drawLine(li[n - 1], li[n], Color.Index(n // 50))

    C.setXminXmaxYminYmax(-0.1, 1.1, -0.1, 1.1)
    fig = [c0]
    nrEtape=5
    for k in range(nrEtape):
        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose(): return
        C.wait(100)

#
if __name__ == '__main__':
    C.initPygame()
    C.run(CurbaLuiLebesgue)
    C.run(CurbaLuiHilbert)

