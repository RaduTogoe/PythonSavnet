def underscores(l):
    l1 = []
    for i in l:
        i = i.split(" ")
        i = "_".join(i)
        print(i)

def dot(l):
    for i in l:
        i = i + "."
        print(i)

def multiply(l):
    for i in l:
        i = i.split(" ")
        i[0] = i[0] * 4
        i = " ".join(i)
        print(i)

l = ["Hello Python", "Ana are mere", "Pizza Party"]
underscores(l)
print()
dot(l)
print()
multiply(l)