import ComplexPygame as C
import Color
import math



def TransformariGeometrice():
    def Translatie(z, a, aprim):  # translatia a -> aprim
        return aprim - a + z

    def Rotatie(z, z0, omega):  # rotatie
        return z0 + omega * (z - z0)

    def Transforma(fig, T, p, q):
        for k in range(len(fig)):
            fig[k] = T(fig[k], p, q)

    C.setXminXmaxYminYmax(-5, 10, -5, 10)
    fig = [1 + 1j, 2 + 0.5j, 3 + 0.5j, 5 + 1j, 4 + 1.5j, 3 + 1.5j, 1 + 1j]
    C.fillScreen(Color.Navy)
    C.setAxis(Color.White)

    a = 0
    aprim = (1 + 2j) / 100
    n = 1000
    k0 = 200
    C.drawNgon(fig, Color.Index(k0))
    kmax = k0 + 6 * n
    z0 = (1 + 1j) / 2

    omega = C.fromRhoTheta(1, math.pi / n)
    for k in range(kmax):
        C.fillScreen(Color.Navy)
        C.setAxis(Color.White)

        Transforma(fig, Translatie, a, aprim)
        #Transforma(fig, Rotatie, z0, omega)
        C.fillNgon(fig, Color.Index(k // 10))
        if C.mustClose():
            return


######################################################
def AstroidaAnimata():

    def traseazaCercQA(q0, a0):  # cercul cu centrul q0 cu primul punct a0
        n = 200
        delta = 2 * math.pi / n
        for k in range(n):
            C.setPixel(q0 + C.fromRhoTheta(1, k * delta) * (a0 - q0), Color.Index(100 + 2 * k))

    r = 1
    R = 4 * r
    a = R + 1
    C.setXminXmaxYminYmax(-a, a, -a, a)
    N = 2000
    dt = 2 * math.pi / N
    cerculMare = [C.fromRhoTheta(R, k * dt) for k in range(N)]
    astroida = [R * complex(math.cos(k * dt)**3, math.sin(k * dt)**3) for k in range(N)]
    for k in range(100000):
        C.fillScreen(Color.Black)
        C.setAxis(Color.White)
        C.drawNgon(cerculMare, Color.White)
        C.drawNgon(astroida, Color.Red)
        theta = k*dt
        q = C.fromRhoTheta(3 * r, theta)
        zC = C.fromRhoTheta(R, theta)  # punctul de contact
        omega = C.fromRhoTheta(1, -4 * theta)  # rotorul
        zA = q + omega * (zC - q)
        traseazaCercQA(q, zA)
        C.drawLine(q, zA, Color.Red)
        if C.mustClose():
            return


######################################################

def RadacinileUnitatii():
    C.setXminXmaxYminYmax(-2, 2, -2, 2)
    C.setAxis()
    n = 9
    fi = 2 * math.pi / n
    for k in range(n):
        u = C.fromRhoTheta(1, k * fi)
        v = C.fromRhoTheta(1, (k + 1) * fi)
        w = C.fromRhoTheta(1, (k + 2) * fi)
        C.drawLine(0, u, Color.Darkslateblue)
        C.drawLine(u, v, Color.Darkmagenta)
        C.drawLine(u, w, Color.Red)

########################################################
def Caleidoscop():
    # simetria fata de dreapta PQ
    def simPQ(z, p, q):
        return p + (q - p) / (q - p).conjugate() * (z - p).conjugate()

    # testare daca z este in stanga laturii a->b:
    def esteInStanga(z, a, b):
        return C.theta((z - a) / (b - a)) >= 0

    # testare daca z este in triunghiul abc
    def esteInTriunghi(z, a, b, c):
        return esteInStanga(z, a, b) == esteInStanga(z, b, c) == esteInStanga(z, c, a)

    # C.getHK restrictionat la [0,dim) x [0,dim)
    def myGetHK(z):
        h, k = C.getHK(z)
        h = max(0, h)
        h = min(h, C.dim - 1)
        k = max(0, k)
        k = min(k, C.dim - 1)
        return h, k

    def cartareReflexii(a, b, c, nmax):
        zSursa = [[C.getZ(h, k) for h in range(C.dim)] for k in range(C.dim)]
        # zSursa[h][k] va fi zetul sursa al reflexiilor
        # care ajung in (h,k)
        for n in range(nmax):
            for h in range(C.dim):
                for k in range(C.dim):
                    z = C.getZ(h, k)
                    if esteInStanga(z, a, c):
                        hsim, ksim = myGetHK(simPQ(z, a, c))
                        zSursa[h][k] = zSursa[hsim][ksim]
                        continue
                    if esteInStanga(z, c, b):
                        hsim, ksim = myGetHK(simPQ(z, c, b))
                        zSursa[h][k] = zSursa[hsim][ksim]
                        continue
                    if esteInStanga(z, b, a):
                        hsim, ksim = myGetHK(simPQ(z, b, a))
                        zSursa[h][k] = zSursa[hsim][ksim]
                        continue
            # formam noul triunghi abc
            a, b, c = simPQ(a, b, c), simPQ(b, c, a), simPQ(c, a, b)

        # decupam triunghiul abc  final
        rez = []  # lista de tupluri (zsursa,h,k)
        for h in range(C.dim):
            for k in range(C.dim):
                if esteInTriunghi(C.getZ(h, k), a, b, c):
                    rez.append((zSursa[h][k], h, k))
        return rez

    # animatia
    C.fillScreen(Color.Navy)
    C.refreshScreen()
    C.setXminXmaxYminYmax(-4, 4, -3, 5)
    omega = math.pi / 6
    ro = 0.5
    a0 = C.fromRhoTheta(ro, 1 * omega)
    b0 = C.fromRhoTheta(ro, 5 * omega)
    c0 = C.fromRhoTheta(ro, 9 * omega)
    caleidoscop = cartareReflexii(a0, b0, c0, 3)
    #img = C.pygame.image.load("bile_colorate.bmp")
    img = C.pygame.image.load("sticle.bmp")
    img.convert()
    colorImgHK = [[img.get_at((h, k)) for h in range(C.dim)] for k in range(C.dim)]
    delta = math.pi / 120
    for t in range(1000000):
        rotor = C.fromRhoTheta(1, t * delta)
        # plimbam  caleidoscopul prin img
        for px in caleidoscop:
            pxz, pxh, pxk = px
            zh, zk = C.getHK(rotor * pxz)
            C.setPixelHK(pxh, pxk, colorImgHK[zh][zk])
        #C.drawNgon([a0,b0,c0],Color.White)
        if C.mustClose():
            return



if __name__ == '__main__':
    C.initPygame()
    # C.run(TransformariGeometrice)
    # C.run(RadacinileUnitatii)
    # C.run(AstroidaAnimata)
    C.run(Caleidoscop)
