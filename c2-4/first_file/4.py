n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))

print("")

for i in l:
    if i % 2 == 0:
        print(i)
