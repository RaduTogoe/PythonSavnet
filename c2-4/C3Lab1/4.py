def verificare_parola():
    parola = int(input("Introduceti parola: "))
    if parola == 7677:
        print("Acces permis.")
    else:
        print("Parola gresita. Mai incercati.")
        verificare_parola()
        return

verificare_parola()