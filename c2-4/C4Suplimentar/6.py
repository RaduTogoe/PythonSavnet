def prime(a: int, b: int):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a == 1

def palindrom(a: int):
    return str(a) == str(a)[::-1]

a = int(input("Left: "))
b = int(input("Right: "))

for i in range (a, b - 1):
    for j in range (i + 1, b):
        if palindrom(i) and palindrom(j) and prime(i, j):
            print(i, j)



