def verifica_varsta(ziua, luna, an):
    if an <= 24:
        if an > 6:
            return False
        else:
            return True
        if luna > 9:
            return False
        else:
            return True
        if ziua > 9:
            return False
        else:
            return True
    else:
        return True


cnp = input("Introduceti primele 7 cifre din CNP:")
an = int(cnp[1] * 10 + cnp[2])
luna = int(cnp[3] * 10 + cnp[4])
ziua = int(cnp[5] * 10 + cnp[5])
major = verifica_varsta(ziua, luna, an)
if major == True:
    print("Aveti peste 18 ani.")
else:
    print("Aveti sub 18 ani.")


