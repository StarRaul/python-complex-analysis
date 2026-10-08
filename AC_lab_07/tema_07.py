import ComplexPygame as C
import Color
import math
def unCercQR(q, r, N):
    alfa = 2 * math.pi / N
    return [q + C.fromRhoTheta(r, k * alfa) for k in range(N)]
def Mediatoare():
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    zA = 2 + 2.5j
    zB = 8 + 2.5j
    zC = 3.5 + 9j
    alfa=abs(zB-zC)
    beta=abs(zC-zA)
    gamma=abs(zA-zB)
    zO =(alfa*zA+beta*zB+gamma*zC)/(alfa+beta+gamma)
    for z in C.screenAffixes():
        za = C.rho(z - zA)
        zb = C.rho(z - zB)
        zc = C.rho(z - zC)
        k = 0
        if za < zb: k += 1
        if zb < zc: k += 2
        if zc < za: k += 4
        C.setPixel(z, Color.Index(600 + 50 * k))
    C.drawNgon([zA, zB, zC], Color.Red)
    C.drawLine(zA,zO,Color.Azure)
    C.drawLine(zB,zO,Color.Azure)
    C.drawLine(zC,zO,Color.Azure)
    C.drawNgon(unCercQR(5+5j, 4, 1000), Color.White)

###################################################################



def LocGeomI():

    def cercInscris(zA, zB, zC):
        # returneaza zI si r pentru cercul inscris
        a = C.rho(zB - zC)
        b = C.rho(zC - zA)
        c = C.rho(zA - zB)
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - c) * (p - b) * (p - a))
        zI = (a * zA + b * zB + c * zC) / (a + b + c)
        r = S / p
        return zI, r

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    q = 0
    R = 7
    nrPuncte = 720
    delta = 2 * math.pi / nrPuncte
    nB = nrPuncte // 2 + nrPuncte // 15
    nC = nrPuncte - nrPuncte // 15
    zB = C.fromRhoTheta(R, nB * delta)
    zC = C.fromRhoTheta(R, nC * delta)
    locGeo=[]
    for i in range(nrPuncte):
        zA=C.rho(zB-zC)
        zB=C.rho(zC-zA)
        zC=C.rho(zA-zB)
        zI, r = cercInscris(zA, zB, zC)
        locGeo.append(zI)
    for n in range(10 * nrPuncte):
        C.fillScreen(Color.White)
        C.setNgon(unCercQR(q, R, nrPuncte), Color.Navy)
        zA = C.fromRhoTheta(R, n * delta)
        C.drawNgon([zA, zB, zC], Color.Navy)
        zI, r = cercInscris(zA, zB, zC)
        C.setNgon(unCercQR(zI, r, 300), Color.Green)
        C.drawNgon([zA, zI, zB, zI, zC, zI], Color.Green)
#        for z in locGeo:
#           C.
        if C.mustClose():
            return


###################################################################

def LocGeomH():

    def ortocentru(zA, zB, zC):
        # returneaza afixul zH al ortocentrului
        zH = 0 #de corectat!
        return zH

    C.setXminXmaxYminYmax(-10, 10, -12, 8)
    q = 0
    R = 6
    nrPuncte = 720
    delta = 2 * math.pi / nrPuncte
    nB = nrPuncte // 2 + nrPuncte // 15
    nC = nrPuncte - nrPuncte // 15
    zB = C.fromRhoTheta(R, nB * delta)
    zC = C.fromRhoTheta(R, nC * delta)
    for n in range(10 * nrPuncte):
        if n % nrPuncte == nB or n % nrPuncte == nC:
            continue
        C.fillScreen(Color.White)
        C.setNgon(unCercQR(q, R, nrPuncte), Color.Navy)
        zA = C.fromRhoTheta(R, n * delta)
        C.drawNgon([zA, zB, zC], Color.Navy)
        zH = ortocentru(zA, zB, zC)
        C.drawNgon([zA, zH, zB, zH, zC, zH], Color.Green)
        if C.mustClose():
            return
##########################################################
if __name__ == '__main__':
    C.initPygame()
    #C.run(Mediatoare)
    C.run(LocGeomI)
    #C.run(LocGeomH)

