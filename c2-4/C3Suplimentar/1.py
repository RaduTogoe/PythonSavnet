def meniu():
    print("1. Fiecare numar la puterea y\n2. Suma tuturor numerelor din lista\n3. Inmultirea fiecarui numar cu y \n4. Iesire")

def putere(alese):
    y = int(input("Introduceti numarul: "))
    puteri = [int(i) ** y for i in alese]
    print(puteri)

def suma(alese):
    sum = 0
    sum += [int(i) for i in alese]

def inmultire(alese):
    y = int(input("Introduceti numarul: "))
    rez = [int(i) * y for i in alese]
    print(rez)

def aplicatie(alese):
        meniu()
        opt = int(input("Alegeti optiunea: "))
        if opt == 1:
            putere(alese)
        elif opt == 2:
            suma(alese)
        elif opt == 3:
            inmultire(alese)
        else:
            return
        aplicatie(alese)

print("Introduceti un sir de numere separate prin virgula:")
s = input()
s = s.split(",")
alese = [i for i in s if i.isnumeric() if int(i) >= 0 and int(i) <= 100]
print(f"Numerele alese sunt: {alese}")
aplicatie(alese)

