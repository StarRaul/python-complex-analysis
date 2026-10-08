import ComplexPygame as C
import Color, math, sys

def PrimulDesen():
    C.setXminXmaxYminYmax(-20,20,-20,20)
    C.fillScreen(Color.Aqua)
    for k in range(sys.maxsize):
        t=0.0001*k
        r=10+8*math.cos(25.12345*t)
        x=r*math.sin(t)
        y=r*math.cos(t)
        C.setPixelXY(x,y,Color.Index(k//50000))
        if k%10000==0 and C.mustClose(): break
    print("GATA!")

def hypotrochoid():
    C.setXminXmaxYminYmax(-15,15,-15,15)
    C.fillScreen(Color.Deepskyblue)
    for k in range(sys.maxsize):
        t=0.0001*k
        a=10.5
        b=4.35
        h=3.5
        x=(a-b)*math.cos(t)+h*math.cos(((a-b)/b)*t)
        y=(a-b)*math.sin(t)-h*math.sin(((a-b)/b)*t)
        #r=x*x+y*y
        r=(a-b)*(a-b)+h*h+2*(a-b)*h*math.cos(a*t/b)
        C.setPixelXY(x,y,Color.Index(k//50000))
        if k%10000==0 and C.mustClose(): break
    print("GATA!")

def archimede():
    C.setXminXmaxYminYmax(-60,60,-60,60)
    C.fillScreen(Color.Goldenrod)
    for k in range(sys.maxsize):
        t=0.0001*k
        x=t*math.cos(t)
        y=t*math.sin(t)
        C.setPixelXY(x,y,Color.Index(k//50000))
        C.drawLine(x,y,Color.Index(k//50000))
        if k%10000==0 and C.mustClose(): break
    print("GATA!")

def SpiralaLuiArhimede():
    def z(t):
        return C.fromRhoTheta(t,t)
    C.setXminXmaxYminYmax(-50,50,-50,50)
    C.fillScreen(Color.Cadetblue)
    for k in range(10000000):
        t=0.001*k
        t1=t+0.1
        C.fillNgon([z(t),z(t+2*math.pi),z(t1+2*math.pi),z(t1)],Color.Index(k//50000))
        #C.drawLine(z(t),z(t-2*math.pi),Color.Index(k//1000))
        #C.setPixel(z(t),Color.Index(k//500))
        if C.mustClose(): break


if __name__ == '__main__':
    C.initPygame()
    #C.run(PrimulDesen)
    #C.run(hypotrochoid)
    #C.run(archimede)
    C.run(SpiralaLuiArhimede)
