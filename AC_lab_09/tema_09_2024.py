import ComplexPygame as C
import Color
import math

#def Functie():

def PseudoSpiralaLuiArhimede():
    nrPuncte = 1000
    alfa = math.pi/2
    omega = C.fromRhoTheta(1, alfa / nrPuncte)

    def traseazaArc(q, delta):
        for k in range(nrPuncte):
            delta *= omega
            C.setPixel(q + delta, Color.Red)
        versor = delta / C.rho(delta)
        q -= versor
        delta += versor
        C.drawLine(q, q + delta, Color.Black)
        return q, delta

    lat = 20
    C.setXminXmaxYminYmax(-lat, lat, -lat, lat)
    q = 0
    delta = 1j
    for k in range(20):
        q, delta = traseazaArc(q, delta)
    C.refreshScreen()

def SpiralaluiPadovan():
    C.fillScreen(Color.Mediumaquamarine)
    def triunghi(triunghi,col):
        a,b,c=triunghi
        aprim=b
        bprim=b+(c-a)/fi
        cprim=b+(c-b)/fi
        return [aprim,bprim,cprim]
    fi=1.324
    C.setXminXmaxYminYmax(-2,8,-3,7)
    a=-1
    b=math.sqrt(3)*1j
    c=1
    C.fillNgon([a,b,c],Color.Blueviolet)
    for k in range(10):
        triunghi = triunghi(triunghi, Color.Index(345))

def grafic(): # metoda injumatatatirii intervalelor
    def functie():
        x=1
        return x^3-x-1 # ???
    a=1
    b=2
    print(a,b)






##############################################################

if __name__ == '__main__':
    C.initPygame()
    C.run(PseudoSpiralaLuiArhimede)
    #C.run(SpiralaluiPadovan)


