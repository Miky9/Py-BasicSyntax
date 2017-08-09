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
input("")
