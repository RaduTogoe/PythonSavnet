def arie_triunghi(baza, inaltime):
    return (baza * inaltime) / 2


a = int(input("Introduce baza triunghiului:"))
b = int(input("Introduce inaltimea triunghiului:"))

rez = arie_triunghi(a, b)
print("Aria este:", rez)
if rez == int(rez):
    print("Rezultatul este int")
else:
    print("Rezultatul este float")
