import ComplexPygame as C
import Color
def JuliaBazine():
    c = complex(-0.21, -0.7)

    def f(z):
        return z * z + c

    C.setXminXmaxYminYmax(-1.5, 1.5, -1.5, 1.5)
    nrIter = 1001
    rhoMax = 1.0e5
    for coloana in C.screenColumns():
        for zeta in coloana:
            z = zeta
            for k in range(nrIter):
                if C.rho(z) > rhoMax: break
                z = f(z)
            col = Color.White
            if C.rho(z) < rhoMax:
                col = Color.Index(10 * sum(C.getHK(z)) + 200)
            C.setPixel(zeta, col)
        if C.mustClose():
            return



####################################################


if __name__ == '__main__':
    C.initPygame()
    C.run(JuliaBazine)
