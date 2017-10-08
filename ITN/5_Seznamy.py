#!/usr/bin/env python3

seznam_1 = []
seznam_2 = [1, 2, 3]
seznam_3 = ["a", "b", "c"]
seznam_4 = ["a", 1, "b", 2]
seznam_5 = list() #prázdný seznam
seznam_6 = list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
seznam_7 = list(range(3, 7)) #[3, 4, 5, 6]
seznam_8 = list(range(1, 10, 2)) #[1, 3, 5, 7, 9]

print("Rozsah seznam_6 \"list(range(10)\" je: " + str(seznam_6[0]) + " - " + str(seznam_6[-1]))
print("seznam_6 = list(range(10)): " + str(seznam_6))
print("seznam_6[0:5]: " + str(seznam_6[0:5]))
print("seznam_6[1:7:2]: " + str(seznam_6[1:7:2])) #vybere m a každý i-tý prvek do n-1
print("seznam_6[2:9:2]: " + str(seznam_6[2:9:2]))
print("seznam_6[::2]: " + str(seznam_6[::2]))

#Velikost seznamu
seznam = [1, 2, 3, "a", "b"]
seznam2 = [1, 2, 3, 4, 5, 8]
print ("velikost seznamu [1, 2, 3, \"a\", \"b\"]: " + str(len(seznam)) + "\n")

# Procházení seznamu
# 1) For in
print("Procházení seznamu [1, 2, 3, \"a\", \"b\"]")
for prvek in seznam:
    print(prvek, sep=' ', end=' ', flush=True) #nebo můžeme udělat něco jiného
print("\n")

# 2) Pomocí funkce range()
print("Procházení seznamu [1, 2, 3, 4, 5, 8]")
for index in range(len(seznam2)):
    print(seznam2[index], end=" ")
    seznam2[index] = seznam2[index] + 1 #všechna čísla v seznamu zvětšíme o 1
print("\n")


# Pozor! Pokud chceme dělat to samé co v ukázce, musí být seznam pouze z čísel!
#
# Funkce len() nám vrátí počet prvků a tento počet si převedeme na iterátor,
# který nám vrací indexy od prvního prvku (0) do posledního prvku (velikost seznamu - 1). Poté k prvkům přistupujeme přes indexy.


# 3) Pomocí funkce enumerate()
# Funkce enumerate() vrací index prvku i jeho hodnotu. Za for následuje proměnná i,
# do které se ukládá index prvku a libovolná proměnná, do které se ukládá hodnota prvku.

for i, prvek in enumerate(seznam):
    print(i, prvek) #vytiskneme index prvku a jeho hodnotu
input("Next...\n")


# Metody

# append - připojí prvek na konec seznamu
# pop - vrátí a odstraní poslední prvek ze seznamu


# Funkce

# len() - Vrátí počet prvků iterovatelného objektu
# min() - Vrátí z iterovatelného objektu prvek s nejmenší hodnotou
# max() - Vrátí z iterovatelného objektu prvek s největší hodnotou
# sum() - Vrátí součet prvků v iterovatelném objektu
# sorted() - Seřadí prvky v iterovatelném objektu A-Z
# Lze také použít metodu seznamu sort, která seznam rovnou seřadí, jelikož funkce sorted() vrací pouze jeho seřazenou kopii a seznam zůstavá nezměněný.
#
# all() - Vrátí booleovskou hodnotu True, jestliže se všechny prvky v iterovatelném objektu vyhodnotí na True, jinak vrátí False
# any()
#
# del - Pomocí del lze jednotlivé prvky ze seznamu mazat za pomoci řezu

seznamX = [1, 3, 2, 0, 5]
del seznam[1] #seznamX = [1, 2, 0, 5]
del seznam[1:3] #seznamX = [1, 5]
input("Next...\n")
