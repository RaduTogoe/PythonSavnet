l = [5, 6, "ana"]

for i in range(0, len(l)):
    name = chr(i + 97)
    print(f"Locatia lui {name} este: {hex(id(l[i]))}")
    print(f"Tipul variabilei {name} este: {type(l[i])}")