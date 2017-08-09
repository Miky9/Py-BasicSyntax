# Cílem tohoto cvičení je naprogramovat jednoduchou hru hráče proti počítači. Úkolem počítače je vybrat si číslo z rozsahu od 1 do 15.
# Následně počítač vypíše do konzole příkazového řádku následující výzvu
# "Pojďme si zahrát hru. Myslím si číslo od 1 do 15. Uhodneš, na které číslo myslím?"
# Hráč poté opakovaně zadává pomocí klávesnice svůj tip a počítač odpovídá následujícím způsobem
# Je-li zadané číslo větší, než to, které si počítač vybral, bude odpověď znít - "Netrefil(a) jsi se. Zkus to znovu s menším číslem"
# Je-li zadané číslo menší než to, které si počítač vybral, bude odpověď znít - "Netrefil(a) jsi se. Zkus to znovu s větším číslem"
# Zadal-li hráč číslo, které jsi vybral počítač, bude odpověď znít - "Gratuluji, vyhrál(a) jsi!"
# Hra končí poté, co hráč uhodne číslo, které si počítač myslel.
# Nápověda - pro práci s náhodnými čísly nabízí Python modul random. Návod na použití tohoto modulu naleznete on-line na
# nebo off-line v interpretu Pythonu pomocí posloupnosti příkazů
import random

R = random.randrange(1, 16)
Z = 0
P = 0

print("Pojďme si zahrát hru. Myslím si číslo od 1 do 15. Uhodneš, na které číslo myslím?")

V = "Netrefil(a) jsi se. Zkus to znovu s menším číslem"
M = "Netrefil(a) jsi se. Zkus to znovu s větším číslem"
W = "Gratuluji, vyhrál(a) jsi!"

while Z != R:
    Z = int(input("Zadejte číslo: "))
    P += 1
    if Z > R:
        print(V)
    elif Z < R:
        print(M)

print(W)
print('pocet pokusu byl '+str(P))