import ComplexPygame as C
import Color
import random
import math


def Elicea():
    def miscaElicea(t, li):
        """returnam imaginea elicei"""
        q = complex(3 * math.cos(t), 2 * math.sin(t))
        omega = C.fromRhoTheta(1, 2 * t)
        return [q + omega * z for z in li]

    def formeazaElicea(r, N):
        rez = []
        alfa = 2 * math.pi / N
        for k in range(N):
            z1 = C.fromRhoTheta(r, k * alfa)
            z2 = C.fromRhoTheta(2 * r, (k + 2 / 3) * alfa)
            z3 = z2 / 30
            rez.append(z1)
            rez.append(z2)
            rez.append(z3)
        rez.append(rez[0])
        return rez

    C.setXminXmaxYminYmax(-5, 5, -5, 5)
    elice = formeazaElicea(1, 7)
    for k in range(100000):
        t = k / 1000
        #C.fillScreen()
        img = miscaElicea(t, elice)
        C.drawNgon(img, Color.Black)
        if C.mustClose():
            break
        C.fillNgon(img, Color.Index(k // 10))
        C.drawNgon(img, Color.Index(k // 10))

###############################################################

def CopacTernar():
    Lambda = 0.9
    rho = 0.6
    theta = math.pi / 7
    omega = C.fromRhoTheta(rho, theta)

    def genereaza(li):
        """li este o lista de tupluri (q,delta)"""
        rez = []
        for (q, delta) in li:
            # (q, delta) este ramura veche, formam 3 ramuri noi
            q1 = q + delta
            delta1 = Lambda * delta
            rez.append((q1, omega * delta1))
            rez.append((q1, delta1))
            rez.append((q1, omega.conjugate() * delta1))
        return rez

    def formeazaCopac(tr0, nivMax=7):
        """tr0 este tuplul (q0,delta0) initial"""
        etaj = [tr0]
        copac = [etaj]  # lista de liste
        for k in range(nivMax):
            etaj = genereaza(etaj)
            copac.append(etaj)
            C.wait(10)
            if C.mustClose():
                break
        return copac

    def mutaCopac(copac, u, sigma):
        """copac este o lista de liste de tupluri (q,delta)"""
        (q0, _) = copac[0][0]
        rez = []
        for etaj in copac:
            etajrez = []
            for (q, delta) in etaj:
                etajrez.append((u + q0 + sigma * (q - q0), delta * sigma))
            rez.append(etajrez)
        return rez

    def arataCopac(copac):
        """copac este o lista de liste de tupluri (q,delta)"""
        for k in range(len(copac)):
            for (q, delta) in copac[k]:
                C.drawLine(q, q + delta, Color.Index(350 + 40 * k))

    C.setXminXmaxYminYmax(-1, 3, -1, 3)
    C.fillScreen()
    trunchi = (0, 0.4j)
    copac = formeazaCopac(trunchi)
    arataCopac(copac)
    u = 1 + 0.5j
    sigma = 0.75
    for k in range(7):
        copac = mutaCopac(copac, u, sigma)
        arataCopac(copac)
        C.refreshScreen()
        C.wait(10)
        u *= 0.65


#########################################################################

def CopacTernarAleator():
    class Ram:
        def __init__(self, q, delta, color):
            self.q = q
            self.delta = delta
            self.color = color

        def show(self):
            C.drawLine(self.q, self.q + self.delta, self.color)

    Lambda = 0.9
    rho = 0.6
    theta = math.pi / 7

    def zar():
        return random.uniform(-0.1, 0.1)

    def genereaza(li, col):

        rez = []
        for r in li:
            # r este ramura veche, formam 3 ramuri noi
            q1 = r.q + r.delta
            omega = C.fromRhoTheta(Lambda + zar(), zar())
            delta1 = omega * r.delta
            rez.append(Ram(q1, delta1, col))
            if zar() > -0.09:
                omega = C.fromRhoTheta(rho + zar(), theta + zar())
                rez.append(Ram(q1, omega * delta1, col))
            if zar() > -0.09:
                omega = C.fromRhoTheta(rho + zar(), -theta + zar())
                rez.append(Ram(q1, omega * delta1, col))
        return rez

    def printeazaLista(li):
        for r in li:
            r.show()

    def formeazaCopac(r, etate=7):
        ultimaGeneratie = [r]
        copac = list(ultimaGeneratie)
        for k in range(etate):
            ultimaGeneratie = genereaza(ultimaGeneratie, Color.Index(350 + 50 * k))
            copac.extend(ultimaGeneratie)
            C.wait(10)
            if C.mustClose(): break
        return copac

    C.setXminXmaxYminYmax(-1, 3, -1, 3)
    C.fillScreen()

    trunchi = Ram(-0.5, 0.4j, Color.Black)
    sigma = 0.8
    u = 1 + 0.3333j
    for k in range(8):
        copac = formeazaCopac(trunchi)
        printeazaLista(copac)
        trunchi.q += u
        trunchi.delta *= sigma + zar() * 1j
        u *= sigma

        C.refreshScreen()
        C.wait(10)


############################################################


####################2024#############################
def CopacInVant():
    class Ram:
        def __init__(self, q, delta, muguri):
            self.q = q
            self.delta = delta
            self.muguri = muguri

        def show(self, color):
            C.drawLine(self.q, self.q + self.delta, color)

    lambda0 = 0.9
    rho0 = 0.6
    theta0 = math.pi / 7

    def rndRam(q, delta):  # returneaza un  ram cu muguri aleatori
        def zar():
            return random.uniform(-0.125, 0.125)

        muguri = [C.fromRhoTheta(lambda0 + zar(), zar())]  # omega
        if zar() < 0.08:
            muguri.append(C.fromRhoTheta(rho0 + zar(), theta0 + zar()))  # omegaStg
        if zar() < 0.08:
            muguri.append(C.fromRhoTheta(rho0 + zar(), -theta0 + zar()))  # omegaDrp
        return Ram(q, delta, muguri)

    def formeazaCopacEtajat(q, delta, nivMax=9):
        def genereazaEtaj(etaj):
            rez = []
            for ram in etaj:
                # ram  este pe etajul vechi, formam 1,2 sau 3 ramuri noi
                q1 = ram.q + ram.delta
                for omg in ram.muguri:
                    dt1 = omg * ram.delta
                    rez.append(rndRam(q1, dt1))
            return rez

        omg = C.fromRhoTheta(lambda0, 0)
        omgstg = C.fromRhoTheta(rho0, theta0)
        omgdrp = C.fromRhoTheta(rho0, -theta0)
        etaj = [Ram(q, delta, [omgstg, omg, omgdrp])]
        copacEtajat = [etaj]
        for _ in range(nivMax):
            etaj = genereazaEtaj(etaj)
            copacEtajat.append(etaj)
        return copacEtajat

    def rotesteCopac(copacEtajat, rotor):
        # modificam copacul rotind ramurile
        # etaj cu etaj
        etaj = copacEtajat[0]
        etaj[0].delta = rotor * delta0
        for etajNou in copacEtajat[1:]:
            k = 0
            for ram in etaj:
                q1 = ram.q + ram.delta
                for omg in ram.muguri:
                    dt1 = rotor * omg * ram.delta
                    if ram.muguri.index(omg) > 0:
                        dt1 *= rotor
                    etajNou[k].q = q1
                    etajNou[k].delta = dt1
                    k += 1
            etaj = etajNou

    def traseazaCopac(copac):
        C.fillScreen()
        for k in range(len(copac)):
            for ram in copac[k]:
                ram.show(Color.Index(400 + 25 * k))
        C.refreshScreen()

    C.setXminXmaxYminYmax(-3, 3, 0, 6)
    q0 = 0.3j
    delta0 = 0.8j
    copac = formeazaCopacEtajat(q0, delta0)
    traseazaCopac(copac)
    C.wait(1000)
    t = 0
    while t < 10000:
        rot = C.fromRhoTheta(1, math.sin(t) / 10)
        rotesteCopac(copac, rot)
        traseazaCopac(copac)
        if C.mustClose(): return
        C.wait(10)
        t += 0.05


if __name__ == '__main__':
    C.initPygame()
    #C.run(CopacTernar)
    #C.run(CopacTernarAleator)
    C.run(CopacInVant)
    #C.run(Elicea)
