from unicodedata import numeric


def read_number():
    nr = input("(nr cu cel mult 9 cifre) nr = ")
    assert nr.isdigit() == True and len(nr) <= 9, "Valoarea nu reprezinta un numar intreg si trebuie sa aiba maxim 9 cifre"
    return nr

def calculeaza_min(nr: int):
    nr = str(nr)
    nr = sorted(nr)
    nr1 = ""
    for i in nr:
        if i == '0':
            nr1 += i
        if i != '0' and nr1[0] == '0':
            nr1 = i + nr1
        elif i != '0':
            nr1 = nr1 + i

    return nr1


nr = read_number()
print(f"Pentru n = {nr}, cel mai mic este {calculeaza_min(nr)}.")
