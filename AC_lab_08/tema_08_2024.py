import ComplexPygame as C
import Color
import math, cmath


def PoligoaneRegulate():
    def npGonQA(q, a, n, p=1):
        # returneaza n-p-gonul cu centru q si primul varf a
        theta = p * 2.0 * math.pi / n
        return [q + C.fromRhoTheta(1, k * theta) * (a - q) for k in range(n)]

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen()
    q = 0
    a = 8
    n = 7
    for i in range(3 , 20):
        poligon=npGonQA(q,a,n)
        C.drawNgon(poligon,Color.Black)
        C.drawNgon(npGonQA(q,a,n,3),Color.Red)
        a=poligon[0]+poligon[2]-poligon[1]
        #C.drawNgon(npGonQA(q, a, n), Color.Black)
        #C.drawNgon(npGonQA(q, a, n, i), Color.Red)


#########################################################################


def HeptaPentagon():
    def npGonQA(q, a0, n, p=1):
        theta = p * 2.0 * math.pi / n
        return [q + C.fromRhoTheta(1, k * theta) * (a0 - q) for k in range(n)]

    def bazaApex(zB, zC, uA, peStg=True):
        # calculeaza apexul zA al triunghiului isoscel zB zA zC
        omegaA = C.fromRhoTheta(1, uA) if peStg else C.fromRhoTheta(1, -uA)
        zA = (zC - omegaA * zB) / (1 - omegaA)
        return zA

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen()
    q = 0
    a = 2
    nInt = 7  # poligonul interior este un heptagon
    pInt = npGonQA(q, a, nInt)
    pInt.append(pInt[0])
    #for _ in range(3):
    #    polig=npGonQA(q,a,nInt)
    #    C.drawNgon(polig,Color.Red)
    #    C.drawNgon(npGonQA(q,a,nInt,2),Color.Black)
    #    a=bazaApex(nInt,nInt,math.pi/2,True)

    nExt = 5  # la exterior construim pentagoane
    thetaExt = 2 * math.pi / nExt

    for k in range(nInt):
        qk = bazaApex(pInt[k], pInt[k + 1], thetaExt, False)
        C.drawNgon(npGonQA(qk, pInt[k], nExt), Color.Black)


def Desen():
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    C.fillNgon([0,10,0,10],Color.Blue)
    r=3/5
    for z in C.screenAffixes():
        col = Color.Blue
        if abs(z) < r:
            col = Color.Red
        C.setPixel(z, col)
    # C.setAxis()
    C.refreshScreen()


#########################################################################

if __name__ == '__main__':
    C.initPygame()
    #C.run(PoligoaneRegulate)
    #C.run(HeptaPentagon)
    C.run(Desen)

