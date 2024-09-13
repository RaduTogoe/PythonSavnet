from lib2to3.btm_utils import reduce_tree


def verifica_parola(parola):
    are_cifra = False
    are_caracter = False
    cifre = "0123456789"
    caractere = "!@%"
    if len(parola) < 7:
        print("Parola este prea scurta!")
        return False
    if parola[0].isupper() == False:
        print("Parola trebuia sa inceapa cu o majuscula")
        return False
    for i in cifre:
        if i in parola:
            are_cifra = True
            break
    for i in caractere:
        if i in parola:
            are_caracter = True
            break
    if not are_caracter:
        print("Parola trebuie sa contina una din urmatoarele caractere: %, !, @.")
        return False
    if not are_cifra:
        print("Parola trebuie sa contina cel putin o cifra")
        return False

def introduce_parola():
    parola = input("Introduceti o parola: ")
    if verifica_parola(parola) == False:
        introduce_parola()
        return
    else:
        print("Parola este in regula.")

introduce_parola()


