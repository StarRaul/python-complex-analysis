import ComplexPygame as C
import Color
import math

#https://en.wikipedia.org/wiki/Koch_snowflake
def VonKoch():
    theta = math.pi / 6
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)
    Lambda = 1 / 3.0

    def transforma(li):  # VonKoch
        z1 = li[0]
        rez = [z1]
        for z2 in li[1:]:
            delta = z2 - z1
            # Segmentul z1_z2 este inlocuit cu
            # z1_zA, zA_zB, zB_zC si zC_z2, unde
            # zA=z1 + Lambda* (z2 - z1)
            # zB=z1 + w * (z2 - z1))
            # zC=z1 + (1-Lambda) * (z2 - z1).
            rez.append(z1 + Lambda * delta)
            rez.append(z1 + w * delta)
            rez.append(z2 - Lambda * delta)
            rez.append(z2)
            z1 = z2
        return rez

    def traseaza(li):
        C.fillScreen()
        for k in range(1, len(li)):
            C.drawLine(li[k - 1], li[k], Color.Black)
        C.refreshScreen()
        C.wait(50)

    C.setXminXmaxYminYmax(-1.1, 1.1, -0.5, 1.5)
    # segmentul initial
    fig = [-1, 1]
    for k in range(6):
        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose():
            return


#########################################################
def VonKoch4():
    theta = math.pi / 4
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)
    Lambda = 1 / 2

    def transforma(li):  # VonKoch
        rez = [li[0]]
        for k in range(1, len(li)):
            z1 = li[k - 1]
            z2 = li[k]
            delta = z2 - z1
            # Segmentul z1_z2 este inlocuit cu
            # z1_zA, zA_zB, zB_zC si zC_z2, unde
            # zA=z1 + Lambda* (z2 - z1)
            # zB=z1 + w * (z2 - z1))
            # zC=z1 + (1-Lambda) * (z2 - z1).
            rez.append(z1 + Lambda * delta)
            rez.append(z1 + w * delta)
            rez.append(z2 - Lambda * delta)
            rez.append(z2)
        return rez

    def traseaza(li):

        C.fillScreen()
        for k in range(1, len(li)):
            C.drawLine(li[k - 1], li[k], Color.Index(k // 500))
        # C.wait(50)

    C.setXminXmaxYminYmax(-0.1, 1.1, -0.1, 1.1)
    # patratul initial
    fig = [0, 1, 1 + 1j, 1j, 0]
    for k in range(9):
        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose():
            return


###############################################################

#https://en.wikipedia.org/wiki/L%C3%A9vy_C_curve
def Crab():
    i = complex(0, 1)
    theta = math.pi / 4.0
    rho = 0.5 / math.cos(theta)
    w = C.fromRhoTheta(rho, theta)

    def transforma(li):  # Crab
        rez = [li[0]]
        for k in range(1, len(li)):
            z1 = li[k - 1]
            z2 = li[k]
            # Segmentul z1_z2 este inlocuit cu z1_zA si zA_z2
            # unde zA=z1+w*(z2-z1).
            rez.append(z1 + w * (z2 - z1))
            rez.append(z2)
        return rez

    def traseaza(li):
        C.fillScreen()
        C.setAxis()
        for k in range(1, len(li)):
            C.drawLine(li[k - 1], li[k], Color.Index(k // 30))
            # C.refreshScreen()
        # C.wait(50)

    C.setXminXmaxYminYmax(-1, 2, -1.5, 1.5)
    # segmentul initial
    fig = [0, 1]
    for k in range(19):
        fig = transforma(fig)
        traseaza(fig)
        print(k)
        if C.mustClose():
            return


##############################################################

#https://en.wikipedia.org/wiki/Dragon_curve
def Dragon():
    i = complex(0, 1)
    theta = math.pi / 4.0
    rho = 0.5 / math.cos(theta)
    w1 = C.fromRhoTheta(rho, theta)
    w2 = C.fromRhoTheta(rho, -theta)

    def transforma(li):  # Dragon
        rez = [li[0]]
        sign = 1
        for k in range(1, len(li)):
            z1 = li[k - 1]
            z2 = li[k]
            # Segmentul z1_z2 este inlocuit cu z1_zA si zA_z2
            # unde zA=z1+w*(z2-z1) cu w avand in mod
            # alternativ valoarea w1 sau w2.
            sign *= -1
            w = w2 if sign > 0 else w1
            rez.append(z1 + w * (z2 - z1))
            rez.append(z2)
        return rez

    def traseaza(li):
        C.fillScreen()
        C.setAxis()
        for k in range(1, len(li)):
            C.drawLine(li[k - 1], li[k], Color.Index(k // 30))
        C.refreshScreen()
        C.wait(50)

    C.setXminXmaxYminYmax(-0.5, 1.5, -1, 1)
    # segmentul initial
    fig = [0, 1]
    for k in range(19):

        fig = transforma(fig)
        traseaza(fig)
        if C.mustClose():
            return


if __name__ == '__main__':
    C.initPygame()
    C.run(VonKoch)
    C.run(VonKoch4)
    C.run(Crab)
    C.run(Dragon)
