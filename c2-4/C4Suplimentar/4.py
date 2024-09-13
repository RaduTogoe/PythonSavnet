def lideri(l : list):
    liderii = []
    for i in range (0, len(l)):
        ok = 1
        for j in range (i + 1, len(l)):
            if l[i] < l[j]:
                ok = 0
                break
        if ok == 1:
            liderii.append(l[i])
    return liderii

l = [16, 17, 4, 3, 5, 2]
print(lideri(l))