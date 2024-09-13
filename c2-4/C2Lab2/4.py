# a
print("/-\\".center(7, " "))
print("//_\\\\".center(7, " "))
print("".center(7, "-"))
print("\\\\_//".center(7, " "))
print("\\-//".center(7, " "))
print("\n\n\n")
# b
print("----".center(8, " "))
print("/    \\".center(8, " "))
print("/______\\")
print("\n\n\n")

#c
for i in range(4):
    s = ""
    for j in range(i * 2 + 1):
        s += "*"
    print(s.center(7, " "))