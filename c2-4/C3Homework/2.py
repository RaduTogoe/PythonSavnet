def numara_vocale(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

s = input("Introduceti un cuvant:")
print(f"Vocale in cuvantul dvs: {numara_vocale(s)}")