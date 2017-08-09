print("Program vypíše všechna sudá čísla.")
maximum = int(input("Zadejte maximální číslo: "))
cislo = 0
while (cislo <= maximum):
    if (cislo % 2 == 0): # nula je sudé číslo
        print(cislo)
    cislo = cislo + 1
input("\nProgram ukončíte stisknutím libovolné klávesy...")


# http://www.fi.muni.cz/IB111/sbirka/index.html

# print(2 + 3)               # scitani
# print(2 * 5)               # nasobeni
# print(10.0 / 3)            # desetinne deleni
# print((5 - 3) * (7 - 4))   # uzavorkovani
# print()
#
# x = 2          # do promenne x prirad cislo 2
# y = 5          # do promenne y prirad cislo 5
# print(x + y)   # spocitej a vypis soucet hodnot promennych x a y
# print()
#
#
# # 5krat vypis retezec 'Hello!'
# for i in range(5):
#     print('Hello!')
# print()
#
#
# # definice funkce pro vypis obvodu ctverce,
# # jehoz delka strany je 'side'
# def print_square_perimeter(side):
#     perimeter = 4 * side
#     print(perimeter)
#
# # volani funkce pro delky strany 50 a 100
# print_square_perimeter(50)
# print_square_perimeter(100)
# print()
#
#
# # z knihovny math importujeme funkci sqrt (odmocnina) a konstantu pi
# from math import sqrt, pi
#
# print(sqrt(4))
# print(pi)
# print()
#
#
# # assignment
# my_variable = 3 + 4
# print(my_variable)
#
# my_variable = my_variable + 5
# print(my_variable)
# print()