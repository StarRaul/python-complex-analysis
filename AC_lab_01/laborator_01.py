from MyComplex import Complex
import math
import cmath


def Exp(z):
    s = 0
    t = 1
    for n in range(1, 100):
        s += t
        t *= z / n
    return s


def testExp():
    z = 0.5
    print(f"\nz are tipul {type(z)} iar Exp(z)  {type(Exp(z))}")
    print(f"z={z} Exp(z)={Exp(z)}")
    print(f"z={z} exp(z)={math.exp(z)}")
    print(f"z={z} exp(z)={cmath.exp(z)}")

    z = 0.5 + 2j
    print(f"\nz are tipul {type(z)} iar Exp(z)  {type(Exp(z))}")
    print(f"z={z} Exp(z)={Exp(z)}")
    # print(f"z={z} exp(z)={math.exp(z)}")
    # TypeError: can't convert complex to float
    print(f"z={z} exp(z)={cmath.exp(z)}")

    zz = Complex(z.real, z.imag)
    print(f"\nzz are tipul {type(zz)} iar Exp(z)  {type(Exp(zz))}")
    print(f"zz={zz} Exp(zz)={Exp(zz)}")
    print(f"z={z}    exp(z)={cmath.exp(z)}")


def Sin(z):
    s = 0
    t = z
    for n in range(2, 100, 2):
        s += t
        t *= - z * z / (n * (n + 1))
    return s
    pass


def testSin():
    z = 0.5

    print(f"\nz are tipul {type(z)} iar Sin(z)  {type(Sin(z))}")
    print(f"z={z} Sin(z)={Sin(z)}")
    print(f"z={z} sin(z)={math.sin(z)}")
    print(f"z={z} sin(z)={cmath.sin(z)}")

    z = 0.5 + 2j

    print(f"\nz are tipul {type(z)} iar Sin(z)  {type(Sin(z))}")
    print(f"z={z} Sin(z)={Sin(z)}")
    print(f"z={z} sin(z)={cmath.sin(z)}")

    w = Complex(z.real, z.imag)
    print(f"\nw are tipul {type(w)} iar Sin(w)  {type(Sin(w))}")
    print(f"w={w} Sin(w)={Sin(w)}")
    print(f"z={z} sin(z)={cmath.sin(z)}")

    print("\nverificam formula")
    print("sin(z)=sin(x)cosh(y)+i cos(x)sinh(y)")
    w = Complex(1, 1)
    xx = math.sin(w.x) * math.cosh(w.y)
    yy = math.cos(w.x) * math.sinh(w.y)
    print(f"w={w} Sin(w)={Complex(xx, yy)}")
    print(f"w={w} Sin(w)={Sin(w)}")


if __name__ == '__main__':
    testExp()
    testSin()

def cos(z):
    s,t=0,1
    for k in range(1,100,2):
        s+=t
        t *= (-z)*z/k*(k+1)
    return s
def testCos():
    z = math.pi/3
    print(cos(z))
print(testCos())
print(cmath.sqrt(21-20j))
print(2000%22)

def SeriaBinomiala(z,alfa):
    if(abs(z)>=1):
        return 0
    s=0
    t=1
    for k in range(1,1000):
        s+=t
        t*=z*(alfa-k)/(k+1)
    return s
def BinSqrt(u):
    z=u-1
    if(abs(z)>=1):
        return 0
    return SeriaBinomiala(z,0.5)
w=0.1+0.2j
print(cmath.sqrt(w))
print(BinSqrt(w))