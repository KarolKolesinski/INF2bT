#zadanie 68 - strona 128
def jednolity(napis):
    for i in range(len(napis)-1):
        if napis[i] != napis[i+1]:
            return False
    return True

lista_napisow = []
with open("ZbiorCKE\\zadanie68\\dane_napisy.txt") as plik:
    for linia in plik:
        lista_napisow.append(linia.split())
print(lista_napisow)
licznik = 0
for napisy in lista_napisow:
    if napisy[0] == napisy[1]:
        if jednolity(napisy[0]):
            licznik += 1
print(licznik)

licznik1 = 0
for napisy in lista_napisow:
    if sorted(napisy[0]) == sorted(napisy[1]):
        licznik1 += 1
print(licznik1)