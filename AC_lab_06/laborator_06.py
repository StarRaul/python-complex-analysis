import ComplexPygame as C
import Color
import math

###################################################################
def IntegralaComplexa():
    def gamma(t):
        return 2-2.5j + C.fromRhoTheta(3, 2 * t) + C.fromRhoTheta(1.7, 5 * t)

    def f(z):
        #return 5/z**2
        #return 1 / z
        return complex(z.imag,z.real)

    R = 12
    C.setXminXmaxYminYmax(-R, R, -R, R)
    C.fillScreen(Color.Navy)
    C.setAxis(Color.White)
    a = 0
    b = 2 * math.pi
    # calculam suma Riemann-Stieltjes
    N = 10000
    delta = (b - a) / N
    suma = 0
    zvechi = gamma(a)
    tk=a
    for k in range(N):
        tk+=delta
        zk = gamma(tk)
        suma += f(zk) * (zk - zvechi)
        print(suma)
        col = Color.Index( k // 10)
        C.drawLine(0, suma, col)
        C.setPixel(zk, col)
        zvechi = zk
        if C.mustClose():
            return

###################################################################

def LeibnizNewton():
    def f(z):
        return 3 * z * z - 10

    def F(z):
        return z * z * z - 10 * z

    def arataMod(h, k, z):
        kol = int(10 * abs(z))
        C.setPixelHK(h, k, Color.Index(kol))

    def arataArg(h, k, z):
        kol = int(512 * (1 + C.theta(z) / math.pi))
        C.setPixelHK(h, k, Color.Index(kol))

    def intPQf(p, q, f):
        # calculam suma Riemann-Stieltjes
        # pentru f pe segmentul PQ
        N = 1000
        delta = (q - p) / N
        suma = 0
        z = p
        for _ in range(N):
            z += delta
            suma += f(z)
        return suma * delta

    R = 5
    C.setXminXmaxYminYmax(-R, R, -R, R)
    C.setAxis()
    dim2 = C.dim // 2
    z0 = 20j
    Fz0 = F(z0)
    for h in range(dim2):
        for k in range(dim2):
            z = C.getZ(2 * h, 2 * k)
            fExact = F(z)
            fAprox = Fz0 + intPQf(z0, z, f)

            #fExact in stanga:
            arataArg(h, k, fExact)
            arataMod(h, k + dim2, fExact)

            #fAprox in dreapta:
            arataArg(h + dim2, k, fAprox)
            arataMod(h + dim2, k + dim2, fAprox)
        if C.mustClose():
            return
    C.setAxis()

#####################################################################
if __name__ == '__main__':
    C.initPygame()

    C.run(IntegralaComplexa)
    #C.run(LeibnizNewton)

