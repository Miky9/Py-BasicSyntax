#!/usr/bin/env python3

# inicializace proměnných
retezec = input("Zadejte slovo: ")
posun = int(input("Zadejte posun: "))
print("Původní zpráva:", retezec)
zprava = ""

# cyklus projíždějící jednotlivé znaky
for znak in retezec:
    i = ord(znak)
    i = i + posun
    # kontrola přetečení
    if (i > ord("z")):
        i = i - 26
    znak = chr(i)
    zprava = zprava + znak
# výpis
print("Zašifrovaná zpráva:", zprava)
input()