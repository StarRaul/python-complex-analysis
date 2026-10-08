import ComplexPygame as C
import Color
import math

def Puteri():
    r = 2
    C.setXminXmaxYminYmax(-r, r, -r, r)
    C.fillScreen(Color.Gray)
    alfa = math.pi / 9
    q1 = C.fromRhoTheta(0.95, alfa)
    q2 = C.fromRhoTheta(1, alfa)
    q3 = C.fromRhoTheta(1.05, alfa)
    p1 = p2 = p3 = 1
    for k in range(50):
        pp1, pp2, pp3 = p1, p2, p3
        p1 *= q1
        p2 *= q2
        p3 *= q3
        C.drawLine(p1, pp1, Color.Greenyellow)
        C.drawLine(p2, pp2, Color.Red)
        C.drawLine(p3, pp3, Color.Blue)
        C.drawLine(0, p3, Color.White)
        C.wait(100)
        if C.mustClose():
            return
    q = C.fromRhoTheta(1, 1)
    p = 1
    for k in range(1000000):
        p *= q
        C.setPixel(p, Color.Navy)
        if k % 10 == 0 and C.mustClose():
            return





def SeriaGeometrica():
    C.setXminXmaxYminYmax(-1, 4, -1, 4)
    C.fillScreen(Color.Lightgray)
    C.setAxis()
    omega = C.fromRhoTheta(0.9, math.pi / 9.2)
    suma = 1 / (1 - omega)
    p = 1
    s = 0
    n = 100
    for k in range(n):
        s += p
        p *= omega
        C.drawLine(s, suma, Color.Index(10 * k))
        C.setPixel(s, Color.Red)
        C.wait(100)
        if C.mustClose():
            return

def SpiralaLuiArhimede():
    def Z(t):
        return t * (math.cos(t) + 1j * math.sin(t))

    def Zprim(t):
        return math.cos(t) + 1j * math.sin(t) + t * (-math.sin(t) + 1j * math.cos(t))

    C.setXminXmaxYminYmax(-50, 50, -50, 50)
    C.setAxis()
    N = 2000
    delta = 2 * math.pi / N
    ntheta = 5 * N // 6
    nfinal = 6 * N
    for n in range(nfinal):
        t = delta * n
        z = Z(t)
        C.setPixel(z, Color.Blue)
        if n % N == ntheta:
            C.drawLine(z, z + Zprim(t), Color.Red)
        if C.mustClose():
            return
if __name__ == '__main__':
    C.initPygame()
    C.run(Puteri)
    # C.run(SeriaGeometrica)
    # C.run(SpiralaLuiArhimede)
