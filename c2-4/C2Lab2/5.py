def palindrom(s):
    return s == s[::-1]

s = input("Introduceti un cuvant: ")
print("Palindrom: ", palindrom(s))
