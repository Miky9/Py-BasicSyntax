#!/usr/bin/env python3

# while podmínka:
#     blok_příkazů
# else:
#     blok_příkazů

cislo = 1
while (cislo <= 10):
    print(cislo, end=" ")
    cislo = cislo + 1 #zvýšíme číslo o jednu - jinak by cyklus nikdy neskončil
input("\nNext...\n")


print("Program vypíše všechna sudá čísla.")
maximum = int(input("Zadejte maximální číslo: "))
cislo = 0
while (cislo <= maximum):
    if (cislo % 2 == 0): #číslo je sudé
        print(cislo, end=" ")
    cislo = cislo + 1
input("\nNext...\n")


# pass - daná část kodu nic nedělá
# break - vyskočí z cyklu
# continue - pokračuje s další iterací cyklu
# return - návratová hodnota (u funkce)


print("Dotěrná aplikace")
pokracovat = True
while pokracovat:
    slovo = input("\nNapište Python pro ukončení: ")
    if (slovo == "Python" or slovo == "python"):
        print("\nSlovo zadáno!")
        pokracovat = False
    else:
        pass # nic se nestane
input("Next...\n")


print("Hledač sudých čísel")
for num in range(2, 10):
    if num % 2 == 0:
        print ("Found an even number", num)
        continue
    print ("Found a number", num)
input("Next...\n")


print("Přeskočí písmeno h")
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
input("Next...\n")


print("Přeskočí číslo 5")
var = 10                    # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")
input("Next...\n")

