import ComplexPygame as C
import Color
import math

from AC_lab_04_folder.ComplexPygame import setPixel


def Darts():
    R = 6
    C.setXminXmaxYminYmax(-R, R, -R, R)
    N = 5
    for z in C.screenAffixes():
        nTheta = int(N * (1 + C.theta(z) / math.pi))
        nRho= int(C.rho(z))
        col = Color.Whitesmoke
        if (nTheta + nRho) % 2 == 0: col = Color.Black
        C.setPixel(z, col)

    C.refreshScreen()
    return

def Bisectoare():
    C.setXminXmaxYminYmax(0, 10, 0, 10)
    a=5+8j
    b=2+2j
    c=3+9j
    C.drawNgon([a,b,c],Color.Red)
    for z in C.screenAffixes():
        col=Color.White
        niv=0
        if abs(C.theta((z-a)/(b-a)))>abs(C.theta((z-a)/(c-a))):
            col=Color.Black
            niv+=1
        setPixel(z,col)
    C.drawNgon([a,b,c],Color.Blue)

if __name__ == '__main__':
    C.initPygame()
    #C.run(Darts)
    C.run(Bisectoare)

