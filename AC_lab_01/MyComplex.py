import math
class Complex:

    def __init__(self, x=0, y=0):
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        self.x = x
        self.y = y

    @property
    def rho(self):
        # furnizeaza modulul rho = |x+yi| pentru
        # z = x+yi = rho(cos(theta) + i sin(theta))
        return math.hypot(self.x, self.y)

    @property
    def theta(self):
        # furnizeaza argumentul theta pentru
        # z = x+yi = rho(cos(theta) + i sin(theta))
        return math.atan2(self.x, self.y)

    @property
    def conj(self):
        # furnizeaza conjugatul
        return Complex(self.x, -self.y)

    def __repr__(self):
        # reprezinta pe z ca string: "Complex(x,y)"
        return f"Complex({self.x}, {self.y})"

    def __str__(self):
        # reprezinta pe z ca string: "x+yi"
        return f"({self.x}{self.y:+}i)"

    def __neg__(self):
        # expresia -z este tradusa z.__neg__()
        return Complex(-self.x, -self.y)

    def __pos__(self):
        # expresia +z este tradusa z.__pos__()
        return Complex(self.x, self.y)

    def __add__(self, other):
        # aduna self + other; z+w se traduce z.__add__(w)
        if isinstance(other, (int, float)):
            return Complex(self.x + other, self.y)
        if isinstance(other, Complex):
            return Complex(self.x + other.x, self.y + other.y)
        raise TypeError(f"Operatie nedefinita: {type(self)} + {type(other)}")

    def __radd__(self, other):
        # aduna other + self;  5+z se traduce z.__radd__(5)
        if isinstance(other, (int, float)):
            return Complex(self.x + other, self.y)
        raise TypeError(f"Operatie nedefinita: {type(other)} + {type(self)}")

    def __sub__(self, other):
        # scade self - other; z-w se traduce z.__sub__(w)
        if isinstance(other, (int, float)):
            return Complex(self.x - other, self.y)
        if isinstance(other, Complex):
            return Complex(self.x - other.x, self.y - other.y)
        raise TypeError(f"Operatie nedefinita: {type(self)} - {type(other)}")

    def __rsub__(self, other):
        # scade other - self; 5-z se traduce z.__rsub__(5)
        if isinstance(other, (int, float)):
            return Complex(other - self.x, -self.y)
        raise TypeError(f"Operatie nedefinita: {type(other)} - {type(self)}")

    def __mul__(self, other):
        # returneaza self*other; z*w se traduce z.__mul__(w)
        if isinstance(other, (int, float)):
            return Complex(self.x * other, self.y * other)
        if isinstance(other, Complex):
            return Complex(self.x * other.x - self.y * other.y,
                           self.x * other.y + self.y * other.x)
        raise TypeError(f"Operatie nedefinita: {type(self)} * {type(other)}")

    def __rmul__(self, other):
        # returneaza other*self;  5*z se traduce z.__rmul__(5)
        if isinstance(other, (int, float)):
            return Complex(self.x * other, self.y * other)
        raise TypeError(f"Operatie nedefinita: {type(other)} * {type(self)}")

    def __truediv__(self, other):
        # returneaza self/other; z/w se traduce z.__truediv__(w)
        if isinstance(other, (int, float)):
            if other != 0:
                return Complex(self.x / other, self.y / other)
            else:
                raise ZeroDivisionError(f"Impartire la zero: {type(self)} / 0")
        if isinstance(other, Complex):
            ro2 = other.rho ** 2
            if ro2 != 0.0:
                return (self * other.conj) / ro2
            else:
                raise ZeroDivisionError(f"Impartire la zero: {type(self)} / 0")
        raise TypeError(f"Operatie nedefinita: {type(self)} / {type(other)}")

    def __rtruediv__(self, other):
        # returneaza other/self;  5/z devine z.__rtruediv__(5)
        if isinstance(other, (int, float)):
            if self != 0:
                return (self.conj * other) / (self.rho ** 2)
            else:
                raise ZeroDivisionError(f"Impartire la zero: {type(other)} / 0")

    def __eq__(self, other):
        # testeaza daca self == other
        try:
            delta = self - other
        except TypeError:
            raise TypeError(f"Operatie nedefinita: {type(self)} == {type(other)}")
        else:
            return delta.rho < 1.0e-20

    def __ne__(self, other):
        # testeaza daca self != other
        try:
            delta = self - other
        except TypeError:
            raise TypeError(f"Operatie nedefinita: {type(self)} != {type(other)}")
        else:
            return delta.rho >= 1.0e-20

    def __pow__(self, n):
        # calculeaza z**n cu formula lui Moivre
        if isinstance(n, (int, float)):
            rlan = self.rho ** n
            ntheta = self.theta * n
            xx = round(rlan * math.cos(ntheta), 10)
            yy = round(rlan * math.sin(ntheta), 10)
            return Complex(xx, yy)
        raise TypeError(f"Operatie nedefinita: {type(self)}**{type(n)}")

    @classmethod
    def fromRhoTheta(cls, rho, theta):
        return Complex(rho * math.cos(theta), rho * math.sin(theta))
