import ComplexPygame as C
import Color
import math


def SerieDePuteri():
    # comparam vizual functiile
    # ExpReIm() si ExpSerie()

    def ExpSerie(z):
        s = 0
        p = 1
        for n in range(1, 100):
            s += p
            p *= z / n
        return s

    def ExpReIm(z):
        return C.fromRhoTheta(math.exp(z.real), z.imag)

    def arataMod(h, k, z):
        #kol = int(100 * abs(z))
        kol = int(100 * z.real)
        C.setPixelHK(h, k, Color.Index(kol))

    def arataArg(h, k, z):
        kol = int(512 * (1 + C.theta(z) / math.pi))
        C.setPixelHK(h, k, Color.Index(kol))

    lat = 2 * math.pi
    C.setXminXmaxYminYmax(-lat, lat, -lat, lat)
    C.setAxis()
    dim2 = C.dim // 2

    for h in range(dim2):
        for k in range(dim2):
            z = C.getZ(2 * h, 2 * k)
            vExact = ExpReIm(z)
            vAprox = ExpSerie(z)

            arataArg(h, k, vExact)
            arataMod(h, k + dim2, vExact)

            arataArg(h + dim2, k, vAprox)
            arataMod(h + dim2, k + dim2, vAprox)
        if C.mustClose():
            return
    C.setAxis()

###################################################################

def FunctiiRationale():
    Nmax = 100
    eps = 1.0e-100

    def initPol(P):
        # presupunem len(P)<Nmax
        rez = [0] * Nmax
        for k in range(len(P)):
            rez[k] = P[k]
        return rez

    def evalPol(P, z):
        suma = 0
        zn = 1
        for n in range(Nmax):
            suma += P[n] * zn
            zn *= z
        return suma

    def dezvoltaFractie(P, Q):
        # presupunem Q[0]!=0
        P = P.copy()
        Rez = [0] * Nmax
        for n in range(Nmax):
            Rez[n] = alfa = P[0] / Q[0]
            for k in range(Nmax):
                P[k - 1] = P[k] - alfa * Q[k]
        return Rez

    def arataMod(h, k, z):
        kol = int(100 * abs(z)) % 1000
        C.setPixelHK(h, k, Color.Index(kol))

    def arataArg(h, k, z):
        kol = int(512 * (1 + C.theta(z) / math.pi))
        C.setPixelHK(h, k, Color.Index(kol))

    lat = 1
    C.setXminXmaxYminYmax(-lat, lat, -lat, lat)
    C.setAxis()
    P = initPol([1, 0, 4])
    Q = initPol([1, 0, 1j, 1 + 1j])
    F = dezvoltaFractie(P, Q)
    for k in range(Nmax):
        print(F[k])

    dim2 = C.dim // 2
    for h in range(dim2):
        for k in range(dim2):
            z = C.getZ(2 * h, 2 * k)
            Qz = evalPol(Q, z)
            if abs(Qz) < eps:
                Qz = eps
            fExact = evalPol(P, z) / Qz
            fAprox = evalPol(F, z)
            arataArg(h, k, fExact)
            arataMod(h, k + dim2, fExact)
            arataArg(h + dim2, k, fAprox)
            arataMod(h + dim2, k + dim2, fAprox)
        if C.mustClose():
            return
    C.setAxis()

###################################################################

def SerieTaylor():
    Nmax = 100

    def alfa(n):
        return 1 / (n * n + 1j)
        # return  C.fromRhoTheta(1,n*math.pi/2)
        # return 1

    def val(a, z):
        suma = a[0]
        p = 1
        for n in range(1, Nmax):
            p *= z / n
            suma += a[n] * p
        return suma

    def arataMod(h, k, z):
        kol = int(100 * abs(z))
        C.setPixelHK(h, k, Color.Index(kol))

    def arataArg(h, k, z):
        kol = int(512 * (1 + C.theta(z) / math.pi))
        C.setPixelHK(h, k, Color.Index(kol))

    lat = 10
    C.setXminXmaxYminYmax(-lat, lat, -lat, lat)
    C.setAxis()
    z0 = 25+1j
    an = [alfa(n) for n in range(Nmax)]
    bn  = [val([alfa(n + k) for n in range(Nmax)], z0) for k in range(Nmax)]

    dim2 = C.dim // 2
    for h in range(dim2):
        for k in range(dim2):
            z = C.getZ(2 * h, 2 * k)
            fExact = val(an, z)
            fAprox = val(bn, z - z0)
            arataArg(h, k, fExact)
            arataMod(h, k + dim2, fExact)
            arataArg(h + dim2, k, fAprox)
            arataMod(h + dim2, k + dim2, fAprox)
        if C.mustClose():
            return
    C.setAxis()

###################################################################

if __name__ == '__main__':
    C.initPygame()
    #C.run(SerieDePuteri)
    #C.run(FunctiiRationale)
    C.run(SerieTaylor)
   