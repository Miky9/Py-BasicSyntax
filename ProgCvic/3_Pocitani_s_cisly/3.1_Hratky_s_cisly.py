# Program načte přirozené číslo n a vypíše výsledek výpočtu nad tímto číslem.
# Náměty na výpočty:
# 1. součet prvních n přirozených čísel,
# 2. faktoriál čísla n, tj. součin prvních n čísel,
# 3. celou část odmocniny z čísla n, tj. největší celé x takové, že x x^2<=n,
# 4. ciferný součet čísla n,
# 5. počet jedniček obsažených v čísle n,
# 6. číslo n zapsané pozpátku,
# 7. informace o tom, zda n je platné rodné číslo.

#!/usr/bin/env python3

import math

# F:
def numLen(num):
  return len(str(abs(num)))

def palindrome(num):
    return str(num) == str(num)[::-1]

print("Vypocty s n\n")
cislo_n = int(input("Zadejte cislo n: "))

cislo = 1
faktorial = 1
soucet = 0

while (cislo <= cislo_n):
    print(cislo)
    soucet = soucet + cislo
    faktorial = faktorial * cislo
    cislo = cislo + 1

odmocnina = math.sqrt(cislo_n)
cifsoucet = sum(int(digit) for digit in str(cislo_n))

delkacisla = numLen (cislo_n)

soucet_1 = str(cislo_n).count('1')

palindrom = palindrome(cislo_n)

print ("\nZadane cislo bylo: " + str(cislo_n) + " " + "\nSoucet prvnich n prirozenych cisel: " + str(soucet) +
       "\nFaktorial cisla n: " + str(faktorial) + "\nOdmocnina cisla n: " + str(math.floor(odmocnina)) +
       "\nCiferny soucet cisla n: " + str(cifsoucet) + "\nSoucet jednicek v cisle n: " + str(soucet_1) +
       "\nCislo n pozpatku: " + str(cislo_n)[::-1] + "\nJedna se o palindrom: " + str(palindrom))

input ()


print("Overeni rodneho cisla\n")
# cislo_rc = int(input("Zadejte rc: "))
cislo_rc = 7401040020

print (str(cislo_rc)+ "\n")

delka_rc = numLen (cislo_rc)

if delka_rc == 10:
    platnost = True
else:
    platnost = False

string_rc = str(cislo_rc)

digits = [int(x) for x in string_rc]

print ((digits[::2]))
y = (sum(digits[::2]))
print (str(y))

print (digits[1::2])
y2 = (sum(digits[1::2]))
print (str(y2))

y3 = (y-y2)
print (str(y3))

if y3 % 11 == 0:
    platnost = True
else:
    platnost = False

# cifsoucet_rc = sum(int(digit) for digit in str(cislo_n))

print ("\nCislo splnuje format rodneho cisla: " + str(platnost))

input ()
