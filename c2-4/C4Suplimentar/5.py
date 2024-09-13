nr = input()
assert len(nr) <= 9 and int(nr) > 0 and nr.isdigit(), "Input-ul trebuie sa fie un numar natural de 9 cifre"

if len(nr) % 2 == 0:
    st = nr[0:len(nr) // 2]
    dr = nr[len(nr) // 2: len(nr)]
else:
    st = nr[0:len(nr) // 2]
    dr = nr[len(nr) // 2 + 1: len(nr)]

st = int(st)
dr = int(dr)
print(f"Pentru n = {nr} rezultatul este {st + dr} ({st} + {dr})")