import ComplexPygame as C
import Color
import math


def FermatTorricelli():
    def unCercQR(q, r):
        N = 100
        delta = 2 * math.pi / N
        return [q + C.fromRhoTheta(r, k * delta) for k in range(N)]
    def unCercQA(q, a):
        N = 100
        delta = 2 * math.pi / N
        return [q + C.fromRhoTheta(1, k * delta) *(a-q) for k in range(N)]

    def sumaDistantelor(a, b, c, z):
        return C.rho(z - a) + C.rho(z - b) + C.rho(z - c)

    C.setXminXmaxYminYmax(-11, 11, -10, 12)
    a = 1 + 7j
    b = 4
    c = -6
    zmin = a
    smin = sumaDistantelor(a, b, c, zmin)
    for z in C.screenAffixes():
        s = sumaDistantelor(a, b, c, z)
        if s < smin:
            zmin = z
            smin = s
        s=int(s)
        # trasam curbele de nivel |z-a|+|z-b|+|z-c|=const
        if s % 2 == 1:
            C.setPixel(z, Color.Index(800 + 10 * s))
    C.fillNgon(unCercQR(zmin,0.3),Color.Red)
    omega = C.fromRhoTheta(1, math.pi / 3)
    aprim = b + omega * (c - b)
    bprim = c + omega * (a - c)
    cprim = a + omega * (b - a)
    C.drawNgon([a, b, cprim], Color.Red)
    qcprim = (cprim + b + a) / 3
    C.drawNgon(unCercQA(qcprim, cprim), Color.Red)
    C.drawNgon([a, bprim, c], Color.Red)
    qbprim = (bprim + a + c) / 3
    C.drawNgon(unCercQA(qbprim, bprim), Color.Red)
    C.drawNgon([aprim, b, c], Color.Red)
    qaprim=(aprim+b+c)/3
    C.drawNgon(unCercQA(qaprim,aprim),Color.Red)
    C.drawLine(a, aprim, Color.Blue)
    C.drawLine(b, bprim, Color.Blue)
    C.drawLine(c, cprim, Color.Blue)


if __name__ == '__main__':
    C.initPygame()
    C.run(FermatTorricelli)