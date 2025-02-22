text = """In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile. Publicul
a aflat deja acele detalii ale crimei care au iesit la iveala in ancheta politiei; dar multe au fost
suprimate cu acea ocazie, deoarece cazul acuzarii era atat de coplesitor de puternic, incat nu era
necesar sa se prezinte toate faptele. Abia acum, la sfarsitul a aproape zece ani, imi este permis sa
aprovizionez acele verigi lipsa care alcatuiesc intregul lant remarcabil. Crima era interesanta in sine, dar acel interes nu era nimic pentru mine in comparatie cu continuarea de neconceput, care
mi-a oferit cel mai mare soc si surpriza din orice eveniment din vitța mea aventuroasa. Chiar si
acum, dupa acest interval lung, mă trezesc emotionat cand ma gandesc la asta si simt din nou acel
potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea."""

def countLitera(litera):
    count = 0
    litera = litera.lower()
    for i in text.lower():
        if i == litera:
            count += 1
    return count

litera = input("Introduce o litera: ")
text1 = text.replace(",", "").replace(".", "").replace("!", "").replace("-", "")
cuvinte = text1.split(" ")
print(cuvinte)
print(countLitera(litera))

print("Cuvinte care incep cu s:")
for i in cuvinte:
    if i[0] in "sS":
        print(i)