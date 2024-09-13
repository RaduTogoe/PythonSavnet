from unicodedata import numeric


def aplicatie():
    x = input("Introduce un numar sau apasa q pentru a iesi din meniu: ")
    if x == "q":
        return
    elif numeric(x):
        print(f"Puterea lui x este: {int(x) * int(x)}")
        aplicatie()


aplicatie()