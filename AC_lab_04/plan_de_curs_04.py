import ComplexPygame as C
import Color
import math
def zEsteInStanga(a, b, z):
    # return C.theta((z - a) / (b - a)) >= 0
    # return ((z - a) / (b - a)).imag >= 0
    return ((z - a) * (b - a).conjugate()).imag >= 0
def Semiplane():
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen()
    N = 32
    dt = 2 * math.pi / N
    p = [C.fromRhoTheta(3,k * dt) for k in range(N + 1)]
    for coloana in C.screenColumns():
        for z in coloana:
            niv = 0
            for k in range(N):
                if zEsteInStanga(p[k], p[k + 1], z):
                    niv += 1
            C.setPixel(z, Color.Index(12 * niv))
        if C.mustClose():
            return
def DomeniuConvex():
    def zEsteInInteriorConvex(p, z):
        # p este o lista circulara
        nrLaturi = len(p) - 1
        pozitiaInitiala=zEsteInStanga(p[0], p[1], z)
        for k in range(1, nrLaturi):
            if pozitiaInitiala != zEsteInStanga(p[k], p[k + 1], z):
                return False
        return True

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen()
    N = 100
    dt = 2 * math.pi / N
    p = [complex(8 * math.cos(k * dt), 6 * math.sin(k * dt)) for k in range(N + 1)]
    C.fillNgon(p, Color.Turquoise)
    C.refreshScreen()
    for coloana in C.screenColumns():
        for z in coloana:
            col = Color.Yellow if zEsteInInteriorConvex(p, z) else Color.Lightgray
            C.setPixel(z, col)
        if C.mustClose():
            return
def DomeniuJordan():
    # p este o lista circulara
    def zEsteInInteriorJordan(p, z):
        s = 0
        for k in range(1, len(p)):
            if z != p[k - 1]:
                s += C.theta((p[k] - z) / (p[k - 1] - z))
        return abs(s) > 0.1

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen()
    N = 100
    dt = 2 * math.pi / N
    p = []
    for k in range(N + 1):
        t = k * dt
        r = 5 + 4 * math.sin(5 * t)
        p.append(C.fromRhoTheta(r, t))
    C.fillNgon(p, Color.Turquoise)
    C.refreshScreen()
    for coloana in C.screenColumns():
        for z in coloana:
            col = Color.Yellow if zEsteInInteriorJordan(p, z) else Color.Lightgray
            C.setPixel(z,col)
        if C.mustClose():
            return

def TriunghiInCerc():
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    r=5
    a=r
    b=C.fromRhoTheta(r,2*math.pi/3)
    c=C.fromRhoTheta(r,6*math.pi/5)
    C.drawNgon([a,b,c],Color.Violet)
    for z in C.screenAffixes():
        niv=0
        if zEsteInStanga(a,b,z): niv+=1
        if zEsteInStanga(b,c,z): niv+=2
        if zEsteInStanga(c,a,z): niv+=4
        C.setPixel(z, Color.Index(a * niv))
        if abs(z)<r:niv+=8
        C.setPixel(z,Color.Index(200*niv))

if __name__ == '__main__':
    C.initPygame()
    #C.run(Semiplane)
    #C.run(DomeniuConvex)
    #C.run(DomeniuJordan)
    C.run(TriunghiInCerc)