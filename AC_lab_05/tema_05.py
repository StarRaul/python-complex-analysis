import ComplexPygame as C
import Color

def Mijloace():
    n = 10
    r = 1/5
    C.fillScreen(Color.Black)
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    a = 1 + 1j
    b = 9 + 2j
    c = 5 + 9j
    col=Color.Turquoise
    C.drawNgon([a,b,c],col)
    ap = a + r*(b-a)
    bp = b + r*(c-b)
    cp = c + r*(a-c)

    for i in range(n):
        C.drawNgon([ap, bp, cp], col)
        ap, bp, cp = ap + r * (bp - ap), bp + r * (cp - bp), cp + r * (ap - cp)



def triunghiexterior():
    n = 10
    r = 5/4
    C.fillScreen(Color.Black)
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    a = 1 + 1j
    b = 9 + 2j
    c = 5 + 9j
    col=Color.Turquoise
    C.drawNgon([a,b,c],col)
    ap = a + r*(b-a)
    bp = b + r*(c-b)
    cp = c + r*(a-c)
    for i in range(n):
        C.drawNgon([ap, bp, cp], col)
        ap, bp, cp = ap + r * (bp - ap), bp + r * (cp - bp), cp + r * (ap - cp)



def patratmare():
    def patratmic(a,b,c,d):
        j=1/5
        n=10
        for i in range(n):
            C.drawNgon([a,b,c,d],Color.Navy)
            aa=a+i*(b-a)
            bb=b+i*(c-b)
            cc=c+i*(d-c)
            dd=d+i*(a-d)
            a,b,c,d=aa,bb,cc,dd
        C.refreshScreen()
    C.setXminXmaxYminYmax(-10,10,-10,10)
    m=-9+9j
    n=-9-9j
    p=9-9j
    q=9+9j
    #patratmic(m,(m+n)/2,(m+p)/2,(m+q)/2
    #patratmic(n,(m+n)/2,(n+p)/2,(n+q)/2
    #...



if __name__ == '__main__':
    C.initPygame()
    #C.run(Mijloace)
    C.run(triunghiexterior)
    #C.run(patratmare)
