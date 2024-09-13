pcs = {}
i = 1

for i in range(1, 4):
    user = input(f"Introduceti utilizatorul PC-ului {i}: ")
    parola = input(f"Introduceti parola PC-ului {i}: ")
    pcs[user] = parola

for pc in pcs:
    print(f"{pc} -> {pcs[pc]}")