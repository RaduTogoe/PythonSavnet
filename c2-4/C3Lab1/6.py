def first_letter_occurence(s):
    ch = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == ch:
            count += 1
    return count

s = input("Introduceti un cuvant (fara majuscule): ")
print(f"{s[0]} apare de {first_letter_occurence(s)} ori")