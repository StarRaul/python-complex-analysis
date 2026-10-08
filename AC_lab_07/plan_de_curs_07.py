import ComplexPygame as C
import Color
import math
def TransBar():
    class Triunghi:
        def __init__(self, a, b, c):
            self.zA, self.zB, self.zC = a, b, c
        def show(self):
            C.drawLine(self.zA, self.zB, Color.Red)
            C.drawLine(self.zB, self.zC, Color.Green)
            C.drawLine(self.zC, self.zA, Color.Blue)
        def aria(self):
            return ((self.zB - self.zA) * (self.zC - self.zA).conjugate()).imag / 2

    def T(S, D, z):
        # Sursa, Destinatie, zetul curent
        sigmaBC = Triunghi(z, S.zB, S.zC).aria()
        sigmaCA = Triunghi(z, S.zC, S.zA).aria()
        sigmaAB = Triunghi(z, S.zA, S.zB).aria()
        return (sigmaBC * D.zA + sigmaCA * D.zB + sigmaAB * D.zC) / (sigmaBC + sigmaCA + sigmaAB)

    C.setXminXmaxYminYmax(0, 10, 0, 10)
    # triunghiul Sursa:
    q0 = 2 + 2j
    r0 = 1
    a, b, c = (q0 + C.fromRhoTheta(r0, (4 * k + 3) * math.pi / 6) for k in range(3))
    S = Triunghi(a, b, c)
    # figura sursa:
    N = 100
    delta = 2 * math.pi / N
    fig = [q0 + C.fromRhoTheta(r0 / 2, k * delta) for k in range(N)]
    C.pygame.display.set_caption("Click and drag with mouse!")
    zA, zB, zC = 2 + 9j, 3 + 3j, 9 + 2j
    while True:
        C.fillScreen()
        S.show()
        C.fillNgon(fig, Color.Cyan)
        C.drawNgon(fig, Color.Black)
        # triunghiul destinatie
        D = Triunghi(zA, zB, zC)
        # figura transformata:
        figTrans = [T(S, D, z) for z in fig]
        D.show()
        C.fillNgon(figTrans, Color.Cyan)
        C.drawNgon(figTrans, Color.Black)

        for event in C.pygame.event.get():
            if event.type == C.pygame.QUIT:
                C.mustExit = True
                return
            if event.type == C.pygame.MOUSEMOTION:
                if C.pygame.mouse.get_pressed()[0]:
                    h, k = event.pos
                    zA = C.getZ(h, C.dim - k)
                break  # end for
        C.refreshScreen()

if __name__ == '__main__':
    C.initPygame()
    C.run(TransBar)
