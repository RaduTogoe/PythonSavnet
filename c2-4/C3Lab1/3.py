def automat():
    print("1. Cappuccino ... 4 lei")
    print("2. Espresso ...3.5 lei")
    optiune = int(input("Ce optiune alegeti? [1,2]: "))
    if optiune not in [1, 2]:
        print("Optiunea nu este valida\n\n")
        automat()
        return
    else:
        bacnota = int(input("Introduceti o bacnota [5,10]: "))
        if bacnota not in [5, 10]:
            print("Va rugam introduceti o bacnota de 5 sau 10 lei!\n\n")
            automat()
            return
        else:
            if optiune == 1:
                print(f"Veti primi restul de {bacnota - 4} lei.")
            else:
                print(f"Veti primi restul de {bacnota - 3.5} lei.")
    print("Produsul se livreaza...")

automat()
