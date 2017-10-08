#!/usr/bin/env python3

# for proměnná in iterovatelný_objekt:
#     blok_příkazů
# else:
#     blok_příkazů


print("Program zjistí zda dané slovo obsahuje samohlásky.")
slovo = input("Zadejte slovo: ")
samohlasky = False
for znak in slovo:
    if znak in "aáeéěiíoóuúůyý":
        samohlasky = True
        break
if samohlasky:
    print(slovo, "obsahuje samohlásky.")
else:
    print(slovo, "neobsahuje samohlásky.")
input("Next...\n")


print("Program zjistí z čeho se skládá slovo.")
slovo = input("Zadejte slovo: ")
samohlasky = 0
souhlasky = 0
ostatni = 0
cisla = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúůyý":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňprřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisla = cisla + 1
    else:
        ostatni = ostatni + 1
print(slovo, "má: ")
print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisla)
print("ostatních znaků...", ostatni)
input("Next...\n")


# range(n) - vrátí čísla od nuly do n-1
#
# range(m, n) - vrátí čísla od m do n-1
#
# range(m, n, i) - vrátí čísla od m a každé další i-té číslo do n-1

print("Range 2,15,2")
for cislo in range(2, 15, 2):
    print(cislo, end=" ")
input("\nNext...\n")


print("Program vygeneruje čísla v zadaném intervalu")
spodnimez = int(input("Zadejte spodní mez intervalu: "))
hornimez = int(input("Zadejte horní mez intervalu: "))
hornimez = hornimez + 1
nasobek = 1
try:
    nasobek = int(input("Násobek čísla (1=default): "))
    if not nasobek:
        raise ValueError('empty string')
except ValueError as e:
    # print(e)
    pass
for cislo in range(spodnimez, hornimez, nasobek):
    print(cislo, end=" ")
input("\nNext...\n")




