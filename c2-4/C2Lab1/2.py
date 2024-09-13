def verifica_parola(nr):
    PAROLA = 7710
    if nr > PAROLA:
        return True
    else:
        return False


a = int(input())
if verifica_parola(a) == True:
    print("Parola corecta")
else:
    print("Parola gresita")