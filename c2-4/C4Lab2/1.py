from unicodedata import numeric
def citeste_nr_part():
    nr = input("Cati participanti avem la sondaj? ")
    try:
        nr = int(nr)
        if nr < 0:
            raise Exception("Numar invalid")
        return nr
    except Exception as e:
        print("Numar invalid")
        return citeste_nr_part()
    return nr


def citeste_participant(nr):
    varsta = input(f"Introduceti varsta participantului {nr}:")
    try:
        varsta = int(varsta)
        if varsta <= 0:
            raise Exception("Varsta invalida")
    except Exception as e:
        print("Varsta invalida")
        return citeste_participant(nr)
    return varsta

def calculeaza_medie(varste):
    return sum([varsta for varsta in varste]) / nr

varste = []
nr = citeste_nr_part()
for i in range(nr):
    varste.append(citeste_participant(i + 1))

print(calculeaza_medie(varste))