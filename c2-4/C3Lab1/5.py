l = ["Masa", 5, "Scaun", 4.5, [5,6,7], 8]
for i in l:
    t = str(type(i))
    t = t.split('\'')[1]

    print(f"Tipul obiectului {i} este {t}")