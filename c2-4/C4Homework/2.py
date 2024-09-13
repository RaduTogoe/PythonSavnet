nr = input("Cati carti doriti sa adaugati in biblioteca? ")
lista_carti = []
for i in range(int(nr)):
    print(f"======== Cartea {i + 1} =========")
    nume = input("Numele cartii: ")
    autor = input("Numele autorului: ")
    an = input("Anul publicarii: ")
    c = {"nume" : nume, "autor": autor, "an": an}
    lista_carti.append(c)
print(lista_carti)