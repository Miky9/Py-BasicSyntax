"""
1.	Pro  zadané  číslo  vypočítejte  posloupnost  vygenerovaných  čísel
a  tuto posloupnost zobrazte graficky (podobně jako na obrá zku 3.1 A).
2.	Pro  čísla  od  1  do  n vypočítejte,  kolik  kroků  potřebujeme,  než  se  do-
staneme do jedničky. Hodnoty vykreslete grafem – pro malé  n vypadá   vý sledný graf vcelku ná hodně,
pro velké n se však objeví zajímavá struk- tura (viz obrá zek 3.1 B).
3.	Podobně  jako předchozí bod, nezobrazujte však počet kroků , ale maxi-
má lní hodnotu, na kterou v prů běhu vý počtu narazíme (např. pro začá tek v čísle 7 je touto maximá lní hodnotou 52).
4.	Pro které číslo od 1 do 100 000 potřebujeme nejvíce kroků , než dospějeme
do jedničky? Jaké  je maximá lní číslo, které  se v příslušné  posloupnosti objeví?
"""

print("Collatzuv problem\n")


def collatz(n):
    while n != 1:
        print(n, end=', ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


collatz(15)
