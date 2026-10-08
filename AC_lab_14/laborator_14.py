import ComplexPygame as C
import math
import cmath
import Color


def JuliaMandelbrot():
    dim2 = C.dim // 2
    nrIterMan = 100
    nrIterJulia = 100

    def traseazaMan():
        for hi in range(dim2):
            for kj in range(dim2):
                c = C.getZ(2 * hi, 2 * kj)
                z = 0
                for n in range(nrIterMan + 1):
                    z = z * z + c
                    if C.rho(z) > 2:
                        break
                col = Color.Darkblue
                if n < nrIterMan: col = Color.Darkcyan
                C.setPixelHK(dim2 + hi, dim2 + kj, col)

            if C.mustClose(): return

    def traseazaAxe():
        hi0, kj0 = C.getHK(0)
        hi0 //= 2
        kj0 //= 2
        col = Color.White
        for hi in range(dim2):
            C.setPixelHK(dim2 + hi, dim2 + kj0, col)
        for kj in range(dim2):
            C.setPixelHK(dim2 + hi0, dim2 + kj, col)

    def punePunct(c):
        hic, kjc = C.getHK(c)
        C.setPixelHK(dim2 + hic // 2, dim2 + kjc // 2, Color.Yellow)

    def traseazaJulia(c):
        for hi in range(dim2):
            for kj in range(dim2):
                z = C.getZ(2 * hi, 2 * kj)
                for n in range(nrIterJulia):
                    z = z * z + c
                    if C.rho(z) > 2:
                        break
                C.setPixelHK(hi, kj, Color.Index(10 * n))

    C.setXminXmaxYminYmax(-2, 2, -2, 2)
    C.fillScreen()
    traseazaMan()
    traseazaAxe()
    nrPuncte = 100
    q = -0.35
    r = 0.8
    delta = 2 * math.pi / nrPuncte
    for n in range(nrPuncte):
        c = q + C.fromRhoTheta(r, n * delta)
        punePunct(c)
        traseazaJulia(c)
        if C.mustClose(): return


########################################################
def Mandelbrot():
    x0 = 0.27314055
    y0 = -0.486
    r0 = 2.0 / 10 ** 3
    nrIter = 1001
    C.setXminXmaxYminYmax(x0 - r0, x0 + r0, y0 - r0, y0 + r0)
    C.fillScreen()
    for coloana in C.screenColumns():
        for c in coloana:
            z = 0
            col = Color.Black
            for k in range(nrIter):
                z = z * z + c
                if abs(z) > 2:
                    col = Color.Index(700 + k)
                    break
            C.setPixel(c, col)
        if C.mustClose():
            return


########################################################
def MandelbrotReal():
    def f(x, c):
        return x * x + c

    a = 2
    C.setXminXmaxYminYmax(-a, a, -a, a)
    C.fillScreen()
    C.setAxis()
    PenColor = Color.Black
    C.drawLineXY(-a, -a, a, a, PenColor)

    c = -1.812
    # GRAFICUL y=f(x,c)
    xv = -a
    yv = f(xv, c)
    for k in range(C.dim):
        x, _ = C.getXY(k, 0)
        y = f(x, c)
        C.drawLineXY(xv, yv, x, y, PenColor)
        xv = x
        yv = y

    # SIRUL x_n
    xv = 0
    xp = f(xv, c)

    for k in range(10 ** 5):

        col = Color.Index(k)
        C.drawLineXY(xv, xp, xp, xp, col)
        xv = xp
        xp = f(xv, c)
        C.drawLineXY(xv, xv, xv, xp, col)
        if C.mustClose() or xp < -2 or xp > 2:
            break


########################################################
def Feigenbaum():
    def f(x, c):
        return x * x + c

    a = 2
    nrGradatii = 16
    delta = 2 * a / nrGradatii
    C.setXminXmaxYminYmax(-a, a, -a, a / 4)
    C.setAxis()
    for k in range(C.dim, 0, -1):
        _, c = C.getXY(0, k)
        x = 0
        for n in range(11650):
            x = f(x, c)
            if abs(x) > 2:
                break
            if n < 10000:
                continue
            h, _ = C.getHK(x)
            C.setPixelHK(h, k, Color.Index(n))
        if C.mustClose():
            break

    for n in range(nrGradatii):
        c = -a + n * delta
        C.drawLineXY(a - 0.5, c, a, c, Color.Red)
        C.setText("c = {0:.2f}".format(c), complex(a - 0.25, c))

    C.refreshScreen()
    C.saveScreenPNG("feigenbaum")


########################################################
########################################################
########################################################


if __name__ == '__main__':
    C.initPygame()
    C.run(JuliaMandelbrot)
    C.run(Mandelbrot)
    C.run(MandelbrotReal)
    C.run(Feigenbaum)
