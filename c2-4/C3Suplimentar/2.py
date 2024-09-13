numere = []
castigatoare = [4, 12, 31, 17, 22, 25]
premii = {2 : 50, 3 : 500, 4: 500, 5: 1000, 6: 5000}
def citeste_numar():
    nr = int(input("Introduceti un nr intre 1 si 49: "))
    if nr not in range(1, 50):
        print("Numar invalid. Incercati din nou.")
        return citeste_numar()
    if nr in numere:
        print("Numar invalid. Incercati din nou.")
        return citeste_numar()
    return nr

def alegere_numere():
    for i in range(6):
        numere.append(citeste_numar())

def calculeaza_castig():
    r = []
    for i in numere:
        if i in castigatoare:
            r.append(i)
    print(f"Numerele ghicite sunt: {r}")
    print(f"Ati castigat {premii[len(r)]} lei")

alegere_numere()
calculeaza_castig()

