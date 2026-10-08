import ComplexPygame as C
import Color
import math

def Romburi26gon():
    def deseneazaRomb(p, kol):
        C.fillNgon(p, Color.Index(kol))
        C.drawNgon(p, Color.Navy)

    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    C.fillScreen(Color.Mediumaquamarine)
    R = 9
    N = 13
    # plecam de la 2N-gon-ul exterior
    omega = math.pi / N
    A = [C.fromRhoTheta(R, k * omega) for k in range(2 * N + 1)]

    for nr in range(6):
        for nn in range(0, 2 * N, 2):
            aux = A[nn] - A[nn + 1] + A[nn + 2]
            deseneazaRomb([A[nn], A[nn + 1], A[nn + 2], aux], 200 + 25 * nr)
            A[nn + 1] = aux
        # rotim lista
        del A[0]
        A.append(A[0])
        if C.mustClose():
            return
        C.wait(100)

########################################################


def GoldenRatio2024():
    fi = (1 + math.sqrt(5.0)) / 2
    omegaCDprimPeAD = -1j / fi

    def traseazaSiTransforma(sector):
        a = sector[0]
        d = sector[- 1]
        c = sector[-2]
        b = a + c - d
        dprim = c + (d - c) / fi
        C.fillNgon([a, b, c, d], Color.Aqua)
        C.fillNgon(sector, Color.Red)
        C.drawNgon([a, b, c, d], Color.White)
        return [dprim + omegaCDprimPeAD * (z - d) for z in sector]

    C.setXminXmaxYminYmax(-0.5, 2, -0.75, 1.75)
    C.fillScreen(Color.Mediumaquamarine)
    a = 0
    b = 1j
    c = 1 + 1j
    d = 1
    C.setText("A", a - 0.1j)
    C.setText("B", b + 0.01j)
    C.setText("C", c + 0.01j)
    C.setText("D", d - 0.1j)
    nrPuncte = 1000
    alfa = -math.pi / (2 * nrPuncte)
    sector = [d + C.fromRhoTheta(1, n * alfa) * (a - d) for n in range(nrPuncte)]
    sector.append(d)
    for k in range(10):
        sector = traseazaSiTransforma(sector)
        C.refreshScreen()
        C.wait(100)

def Desen():

    def transform(patrat, col):
        C.fillNgon(patrat, col)
        a, b, c, d = patrat
        ap = c
        bp = c + (c - b) / fi
        dp = c + (d - c) / fi
        cp = bp + dp - ap
        return [ap, bp, cp, dp]

    fi = (1 + math.sqrt(5) / 2)
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    patrat = [1 + 2j, 1 + 6j, 5 + 6j, 5 + 2j]

    for k in range(10):
        patrat = transform(patrat, Color.Index(200 * k))

##############################################################

if __name__ == '__main__':
    C.initPygame()
    # C.run(Romburi26gon)
    #C.run(GoldenRatio2024)
    C.run(Desen)
