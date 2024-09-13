def citeste_numere():
    nr = int(input())
    l = []
    while nr != 0:
        l.append(nr)
        nr = int(input())
    return l

def palindroame(l : list):
    l1 =  [i for i in l if str(i) == "".join(reversed(str(i)))]
    return l1

l = citeste_numere()
print(f"lista initiala: {l}")
print(f"lista finala: {palindroame(l)}")
