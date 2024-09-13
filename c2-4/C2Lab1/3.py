def medie_arit(a, b):
    return (a + b) / 2

def impartire(a, b):
    return int(a / b)

def pow(a, b):
    return a ** b

a = int(input())
b = int(input())
print("Media numerelor este: " + str(medie_arit(a, b)) + "\n"
      + "Impartirea numerelor este: " + str(impartire(a , b)) + "\n"
        + "A la puterea b: " + str(pow(a, b)) + "\n")