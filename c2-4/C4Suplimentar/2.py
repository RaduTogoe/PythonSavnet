import math


def p10(nr):
    return len(nr)


def prim(nr):
    if nr == 2:
        return True
    if nr < 2 or nr % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(nr)) + 1, 2):
        if nr % i == 0:
            return False
    return True


def divizori(nr):
    par = ""
    impar = ""
    for i in range(1, int(nr / 2) + 1):
        if nr % i == 0:
            if i % 2 == 0:
                par += str(i)
            else:
                impar += str(i)
    if nr % 2 == 0:
        par += str(nr)
    else:
        impar += str(nr)
    if par == "":
        par = "0"
    if impar == "":
        impar = "0"

    sum = int(par) + int(impar)
    print(f"""Divizori pari: {par}
Divizori impari: {impar}
Suma divizorilor este: {sum} => {'DA' if prim(sum) else 'NU'}""")


nr = input("n = ")
print(f"Cea mai mica putere a lui n este: 10^{p10(nr)}")
divizori(int(nr))
