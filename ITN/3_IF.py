#!/usr/bin/env python3

cislo = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (cislo > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit!")
    odmocnina = cislo ** (1/2)
    print("Odmocnina z čísla", cislo, "je", odmocnina)
else:
    print("Odmocnina ze záporného čísla neexistuje!")
print("Děkuji za zadání")
input("Next...\n")


# 1.verze - špatně, příkazy jdou po sobě
cislo = 0 # do čísla si přiřadíme na začátku 0
if (cislo == 0): # pokud je číslo 0, dáme do něj jedničku
    cislo = 1
if (cislo == 1): # pokud je číslo 1, dáme do něj nulu
    cislo = 0
print(cislo)
input("Next...\n")

# 2.verze - správně, provede se jen jedna část příkazu
cislo = 0 # do čísla si přiřadíme na začátku 0
if (cislo == 0): # pokud je číslo 0, dáme do něj jedničku
    cislo = 1
else: # pokud je číslo 1, dáme do něj nulu
    cislo = 0
print(cislo)
input("Next...\n")


# Logické operátory and, or, not

cislo = int(input("Zadejte číslo v rozmezí 10-20: "))
if ((cislo >= 10) and (cislo <= 20)):
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně")
input("Next...\n")


cislo = int(input("Zadejte číslo v rozmezí 10-20 nebo 30-40: "))
if (((cislo >= 10) and (cislo  <= 20)) or ((cislo  >=30) and (cislo  <= 40))):
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně")
input("Next...\n")


cislo = int(input("Zadejte číslo v rozmezí 10-20 nebo 30-40: "))
if ((10 <= cislo <= 20) or (30 <= cislo <= 40)):
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně")
input("Next...\n")


if "0" not in "agent 007":
    z = "neni"
else:
    z = "je tam"
print (z)
input("Next...\n")
