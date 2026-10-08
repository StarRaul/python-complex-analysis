import ComplexPygame as C
import Color


def MandelbrotExplorer():
    x0 = -0.5
    y0 = 0.0
    r0 = 2.0
    nrIter = 101

    def oDerulareCompleta():
        C.fillScreen()
        for coloana in C.screenColumns():
            for c in coloana:
                z = 0
                for k in range(nrIter):
                    z = z * z + c
                    if abs(z) > 2:
                        break
                C.setPixel(c, Color.Index(k))
            if unClick():
                return False
        return True

    def unClick():
        nonlocal x0, y0, r0, nrIter
        C.refreshScreen()
        rez = False
        for event in C.pygame.event.get():
            if event.type == C.pygame.QUIT:
                C.mustExit = True
                return True  # parasim unClick()
            if event.type == C.pygame.KEYDOWN:
                if event.key == C.pygame.K_SPACE:
                    C.mustPainting = False
                    rez = True
                elif event.key == C.pygame.K_n:
                    nrIter *= 2
                    rez = True
                elif event.key == C.pygame.K_m:
                    nrIter //= 2
                    rez = True
                elif event.key == C.pygame.K_b:
                    r0 *= 5
                    rez = True
            if event.type == C.pygame.MOUSEBUTTONDOWN:
                ii, jj = event.pos
                x0, y0 = C.getXY(ii, C.dim - jj)
                r0 *= 0.1
                rez = True
        return rez

    # bucla derularilor
    while True:
        C.setXminXmaxYminYmax(x0 - r0, x0 + r0, y0 - r0, y0 + r0)
        C.pygame.display.set_caption("x0={0}, y0={1}, r0={2:.2e},"
                                     " nrIter={3}".format(x0, y0, r0, nrIter))
        saDerulatPanaLaCapat = oDerulareCompleta()
        if C.mustExit or not C.mustPainting:
            break  # parasim bucla derularilor
        if saDerulatPanaLaCapat:
            C.saveScreenPNG("mandelbrot")
            C.pygame.display.set_caption("Click! x0={0}, y0={1}, r0={2:.2e},"
                                         "nrIter={3}".format(x0, y0, r0, nrIter))
            while not unClick():  # asteptam un click
                pass
            if C.mustExit or not C.mustPainting:
                break  # parasim bucla derularilor
        # reluam derularea
    return


if __name__ == '__main__':
    C.initPygame()
    C.run(MandelbrotExplorer)
