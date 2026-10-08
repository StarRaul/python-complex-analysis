import ComplexPygame as C
import Color
import math
import sys


def Sablon():
    def FiguraInitiala(r):
        # un cerc care trece prin origine
        nrPuncte = 5000
        delta = 2 * math.pi / nrPuncte
        return [r + C.fromRhoTheta(r, h * delta) for h in range(nrPuncte)]

    # animatia:
    C.fillScreen(Color.Navy)
    lat = 1
    C.setXminXmaxYminYmax(-lat, lat, -lat, lat)
    fig = FiguraInitiala(lat / 3)
    omega = C.fromRhoTheta(1, math.pi / 24)
    for t in range(sys.maxsize):
        # C.fillScreen(Color.Navy)
        col = Color.Index(t)
        for k in range(len(fig)):
            C.setPixel(fig[k], col)
            fig[k] *= omega
        if C.mustClose():
            break
    C.setAxis(Color.White)


if __name__ == '__main__':
    C.initPygame()
    C.run(Sablon)
