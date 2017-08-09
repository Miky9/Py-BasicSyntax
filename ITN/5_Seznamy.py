seznam_1 = []
seznam_2 = [1, 2, 3]
seznam_3 = ["a", "b", "c"]
seznam_4 = ["a", 1, "b", 2]
seznam_5 = list() #prázdný seznam
seznam_6 = list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
seznam_7 = list(range(3, 7)) #[3, 4, 5, 6]

seznam_8 = list(range(1, 10, 2)) #[1, 3, 5, 7, 9]

print("rozsah seznamu je: " + str(seznam_6[0]) + " - " + str(seznam_6[-1]))

print("\n" + str(seznam_6))

print("\n" + str(seznam_6[0:5]))

print("\n" + str(seznam_6[1:7:2])) #vybere m a každý i-tý prvek do n-1

print("\n" + str(seznam_6[2:9:2]))

print("\n" + str(seznam_6[::2]))

#Velikost seznamu
seznam = [1, 2, 3, "a", "b"]
print ("\nvelikost seznamu: " + str(len(seznam)) + "\n")

# Procházení seznamu

# 1) For in
for prvek in seznam:
    print(prvek, sep=' ', end=' ', flush=True) #nebo můžeme udělat něco jiného

print("\n")

# 2) Pomocí funkce range()
for index in range(len(seznam)):
    seznam[index] = seznam[index] + 1 #všechna čísla v seznamu zvětšíme o 1

# Pozor! Pokud chceme dělat to samé co v ukázce, musí být seznam pouze z čísel!
#
# Funkce len() nám vrátí počet prvků a tento počet si převedeme na iterátor,
# který nám vrací indexy od prvního prvku (0) do posledního prvku (velikost seznamu - 1). Poté k prvkům přistupujeme přes indexy.


# 3) Pomocí funkce enumerate()
# Funkce enumerate() vrací index prvku i jeho hodnotu. Za for následuje proměnná i,
# do které se ukládá index prvku a libovolná proměnná, do které se ukládá hodnota prvku.

for i, prvek in enumerate(seznam):
    print(i, prvek) #vytiskneme index prvku a jeho hodnotu


input()
