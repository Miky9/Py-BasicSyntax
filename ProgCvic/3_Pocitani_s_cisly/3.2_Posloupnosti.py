# Odhalte princip následujících posloupností a poté napištete pro každou z nich
# program, který dostane na vstup číslo n a na výstup vypíšee prvních n členů
# dané posloupnosti.
# 1. 1, 2, 3, 4, 5, 6, . . .
# 2. 1, 3, 5, 7, 9, 11, . . .
# 3. 1, 5, 9, 13, 17, 21, 25, 29, . . .
# 4. 1, 2, 4, 7, 11, 16, . . .
# 5. 1, 2, 4, 8, 16, 32, . . .
# 6. 1, 2, 6, 24, 120, . . .
# 7. 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, . . .
# 8. 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, . . .
# 9. 1, 2, 4, 7, 9, 12, 18, 24, 32, 38, 42, 50, 56, 64, 71, 73, 75, 81, . . .
# 10. 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, . . .
# 11. 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, . . .


print("Posloupnosti\n\nPosloupnost cislo 1\n")
# cislo_n = int(input("Zadejte cislo n: "))
cislo_n = 6

cislo = 1
print("\nVystup: ")

while (cislo <= cislo_n):
    print(cislo, sep=' ', end=', ', flush=True)
    # soucet = soucet + cislo
    cislo = cislo + 1


cislo = 1
i = 1
print("\n\nVystup2: ")

while (i <= cislo_n):
    print(cislo, sep=' ', end=', ', flush=True)
    cislo = cislo + 2
    i = i + 1

cislo = 1
i = 1
print("\n\nVystup3: ")

while (i <= cislo_n):
    print(cislo, sep=' ', end=', ', flush=True)
    cislo = cislo + 4
    i = i + 1

cislo = 1
i = 1
print("\n\nVystup4: ")

while (i <= cislo_n):
    print(cislo, sep=' ', end=', ', flush=True)
    cislo = cislo + i
    i = i + 1

cislo = 1
i = 1
print("\n\nVystup5: ")

while (i <= cislo_n):
    print(cislo, sep=' ', end=', ', flush=True)
    cislo = cislo * 2
    i = i + 1

cislo = 1
i = 1
print("\n\nVystup6: ")

while (i <= cislo_n):
    print(cislo, sep=' ', end=', ', flush=True)
    cislo = cislo * (i+1)
    i = i + 1


cislo = 1
i = 2
print("\n\nVystup7: ")

while (i <= cislo_n):
    y = list(range(1, i))
    print((str(y))[1:-1], sep=' ', end=', ', flush=True)
    i = i + 1


r = cislo_n * 10
print("\n\nVystup8: ")  # Prvocisla

for num in range(1,r):
    if all(num%i!=0 for i in range(2,num)):
       print (str(num), sep=' ', end= ', ', flush=True)


