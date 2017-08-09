print("Program vypíše všechna sudá čísla.")
maximum = int(input("Zadejte maximální číslo: "))
cislo = 0
while cislo <= maximum:
    if cislo % 2 == 0: #číslo je sudé
        print(cislo)
    cislo = cislo + 1
input("\nProgram ukončíte stisknutím libovolné klávesy...")
