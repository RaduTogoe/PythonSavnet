numere = []

def citeste_numere():
    try:
        nr = input("Numar: ")
        if nr == 'x':
            return
        nr = float(nr)
        numere.append(nr)
    except Exception:
        print("Numar invalid")
    citeste_numere()

def afisare_meniu():
    print("Meniu:\n1. Media numerelor\n2. Suma numerelor\n3. Puterea numerelor din lista de numere\n4. Iesire\n")

def run():
    afisare_meniu()
    rezultat = ""
    nr = input("Introduceti optiunea dvs: ")
    if nr in meniu:
        if nr == "1":
            rezultat = medie(numere)
        elif nr == "2":
            rezultat = suma(numere)
        elif nr == "3":
            rezultat = putere(numere)
        else:
            return
    print(f"Rezultat: {rezultat}")

def suma(lista: list):
    return sum([i for i in lista])

def medie(lista: list):
    return sum([i for i in lista]) / len(lista)

def putere(lista: list):
    return [i ** 2 for i in lista]

meniu = {
    "1": medie,
    "2": suma,
    "3": putere
}
print("Introduceti numere. Cand sunteti gata, introduceti x.")
citeste_numere()
run()
print(numere)
