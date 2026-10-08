import math

def VerficareDeltaMinus(p, q):
    delta = q * q + 4.0 * p ** 3 / 27.0
    assert delta < 0, "Nu suntem in cazul Delta < 0"
    theta = math.acos(3 * q * math.sqrt(-3 / p) / (2 * p))
    rho = math.sqrt(-p / 3)
    print(f"Ecuatia z**3{p:+}z{q:+}=0")
    print(f"are solutiile:")
    for k in range(3):
        zk = 2*rho*math.cos((theta + 2 * k * math.pi) / 3)
        print(f"z{k}={zk: .3g}")


if __name__ == '__main__':
    VerficareDeltaMinus(-7, 6)
# Rezultat:
# Ecuatia z**3-7z+6=0
# are solutiile:
# z0= 2
# z1=-3
# z2= 1