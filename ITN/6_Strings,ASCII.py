#!/usr/bin/env python3

# Speciální znaky
# \n - nový řádek
# \t - tabulátor
# Tabulátor zarovnává slova tak, aby každé slovo po tabulátoru začínalo na pozici, která je násobkem 8 (první znak řetězce se počítá od nuly)

# \a - zvonek
# \\ - zpětné lomítko
# r"\n" - holý řetězec (bere každý znak v řetězci zvlášť)
# 'ass "1" ass' - lze bez úprav

# Řetězce jsou iterovatelný objekt! Skládají se totiž z jednotlivých znaků.
# Proto když při vytváření seznamu použijeme nějaký řetězec, uloží se nám do něj jednotlivé znaky.

# Replikace
# retezec = "Bum! "
# print(retezec * 7)


# Převod znaku na číslo a zpět (ASCII) https://cs.wikipedia.org/wiki/ASCII
# ord("a") #97
# chr(97) #'a'


# Vylepšený program:
print("Program zjistí z čeho se skládá slovo.")
slovo = input("Zadejte slovo: ")
samohlasky = 0
souhlasky = 0
cisel = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúů":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňprřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif ord(znak) in range(48, 58):
        cisel = cisel + 1
    else:
        pass
print(slovo, "má: ")
print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisel)
print("ostatních znaků...", len(slovo) - samohlasky - souhlasky - cisel)
input("\nAplikaci ukončíte stisknutím libovolné klávesy...")


# Porovnávání
# >>> "a" < "b"
# True
# >>> "b" < "a"
# False
# >>> "c" == "c"
# True
# >>> "ab" >= "a"
# True
# >>> "e" <= "df"
# False
# >>> "java" == "javascript"
# False
# >>> "c-sharp" != "java"
# True


# Řezání
# [:] - vybere celý řetězec
# [::-1] - převrátí řetězec
# >>> retezec = "lokomotiva"
# >>> retezec[0]
# 'l'
# >>> retezec[1:4]
# 'oko'
# >>> retezec[::2]
# lkmtv


# Metody řetězců

# count("podretezec") - Vrátí počet podřetězců v jiném řetězci. Lze zadat i výřez
# >>> retezec = "abeceda"
# >>> retezec.count("a")
# 2
# >>> retezec.count("e", 1, 4) # to samé jako retezec[1:4].count("e")
# 1

# endswith("podretezec") - Vrátí booleovskou hodnotu (True/False) jestli řetězec končí zadaným řetězcem. Lze zadat i výřez.
# >>> retezec = "abeceda"
# >>> retezec.endswith("a")
# True

# find("podretezec") - Vrátí index nejlevější pozice řetězce v jiném řetězci. Pokud není nalezen, vrátí -1 . Lze zadat i výřez.
# >>> retezec = "abeceda"
# >>> retezec.find("a")
# 0
# >>> retezec.find("f")
# -1



