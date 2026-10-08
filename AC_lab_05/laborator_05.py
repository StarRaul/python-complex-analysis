import ComplexPygame as C
import Color


def RidicareaLaCub():
    C.setXminXmaxYminYmax(-20, 10, -10, 20)
    C.fillScreen(Color.Lightgray)
    a = 1
    b = 2
    N = 1000
    delta = (b - a) / N
    for h in range(N):
        x = a + h * delta
        for k in range(N):
            y = a + k * delta
            z = complex(x, y)
            C.setPixel(z, Color.Black)
            C.setPixel(z ** 3, Color.Red)
    C.setAxis()


def RidicareaLaPatrat():
    C.setXminXmaxYminYmax(-5, 5, -5, 5)
    C.fillScreen(Color.Black)
    C.setAxis(Color.White)
    a = 3
    nra = 10
    deltaa = 2 * a / nra
    b = 3
    nrb = 1000
    deltab = 2 * b / nrb

    for h in range(nra):
        x = -a + (h + 0.5) * deltaa
        col = Color.Index(25 * h)
        for k in range(nrb):
            y = -b + k * deltab
            z = complex(x, y)
            C.setPixel(z, col)
            C.setPixel(z * z, col)
            if C.mustClose():
                return
        C.wait(500)
    for h in range(nra):
        y = -a + (h + 0.5) * deltaa
        col = Color.Index(400 + 25 * h)
        for k in range(nrb):
            x = -b + k * deltab
            z = complex(x, y)
            C.setPixel(z, col)
            C.setPixel(z * z, col)
            if C.mustClose():
                return
        C.wait(500)


if __name__ == '__main__':
    C.initPygame()
    C.run(RidicareaLaCub)
    # C.run(RidicareaLaPatrat)
