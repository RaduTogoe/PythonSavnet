numere = ['abc',123,'1',1]
d = {"int" : 0, "float" : 0, "str" : 0}

for i in numere:
    print(type(i))
    d[str(type(i)).split("\'")[1]] += 1

print(d)