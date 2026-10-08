import ComplexPygame as C
import Color

def Nisshoki():
    C.setXminXmaxYminYmax(-3, 3, -3, 3)
    r = 3.0 / 5.0
    for z in C.screenAffixes():
        col = Color.Cyan
        if abs(z.real) < 1.5 and abs(z.imag) < 1.5:
            col=Color.White
        if abs(z) < r:
            col = Color.Crimson
        C.setPixel(z, col)
    # C.setAxis()
    C.refreshScreen()


def MasterCard():
    centru1=-2
    centru2=2
    raza=3
    C.setXminXmaxYminYmax(-10, 10, -10, 10)
    #r = 3.0 / 5.0
    for z in C.screenAffixes():
        niv=0
        if abs(z-centru1) < raza:
            niv+=1
        if abs(z-centru2) < raza:
            niv+=2
        if niv==0:
            C.setPixel(z, Color.White)
        elif niv==1:
            C.setPixel(z, Color.Red)
        elif niv==2:
            C.setPixel(z, Color.Yellow)
        else:
            C.setPixel(z, Color.Orange)
        if z.imag>4 or z.imag<-4:
            C.setPixel(z, Color.Cyan)
    C.refreshScreen()

#pb 3 si 4
if __name__ == '__main__':
    C.initPygame()
    #C.run(Nisshoki)
    C.run(MasterCard)

