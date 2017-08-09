# Naprogramujte jednoduchou variantu hry Kámen, nůžky, papír pro jednoho hráče a počítač. Hra musí splňovat následující požadavky+
#
# Volba počítače je dána při startu hry
# Při startu budou vypsána základní pravidla hry
# Hráč bude vyzván k zadání své volby
# Hra porovná volbu hráče s volbu počítače dle známých pravidel (kámen tupí nůžky, nůžky stříhají papír a papír obalí kámen)
# Hra oznámí vítěze

import random
import sys

Z = ''
print("zadej K / N / P\nK=kamen\nN=nuzky\nP=papir\n")
Z = input("Zadejte volbu: ")

if 'K' in Z:
    Z = 1
elif 'N' in Z:
    Z = 2
elif 'P' in Z:
    Z = 3
else:
    print('chyba!')
    sys.exit()


# print (zadani)


# print (random.randrange(1, 4))

R = random.randrange(1, 4)
# R = random.choise(['K', 'N', 'P'])


# volby = {                  #list/slovník
#     'K': 'kamen',
#     'N': 'nuzky',
#     'P': 'papir',
# }

if R == 1:
    RR = 'K'
elif R == 2:
    RR = 'N'
elif R == 3:
    RR = 'P'

v = 'vyhral jsi!'+' pocitac udelal '+RR
p = 'prohral jsi!'+' pocitac udelal '+RR
rem = 'remiza'+' pocitac udelal taky '+RR

if Z == R:
    print(rem)
elif (Z == 3) and (R == 1):
    print(v)
elif (Z == 2) and (R == 3):
    print(v)
elif (Z == 1) and (R == 2):
    print(v)
else:
    print(p)