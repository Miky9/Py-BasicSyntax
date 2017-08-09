print("Program zjistí z čeho se skládá slovo.")
slovo = input("Zadejte slovo: ")
samohlasky = 0
souhlasky = 0
ostatni = 0
cisel = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúůyý":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňprřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisel = cisel + 1
    else:
        ostatni = ostatni + 1
print(slovo, "má: ")
print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisel)
print("ostatních znaků...", ostatni)
input("\nAplikaci ukončíte stisknutím libovolné klávesy...")