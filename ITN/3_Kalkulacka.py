#!/usr/bin/env python3

# print("Kalkulačka1\n")
# první_číslo = int(input("Zadejte první číslo: "))
# druhé_číslo = int(input("Zadejte druhé číslo: "))
# print("Jejich součet je:", první_číslo + druhé_číslo)
# print("Jejich rozdíl je:", první_číslo - druhé_číslo)
# print("Jejich součin je:", první_číslo * druhé_číslo)
# print("Jejich podíl je:", první_číslo / druhé_číslo)
# input("\nStiskněte libovolnou klávesu...")


# print("Kalkulačka2\n")
# prvni_cislo = int(input("Zadejte první číslo: "))
# druhe_cislo = int(input("Zadejte druhé číslo: "))
# print("1 - sčítání")
# print("2 - odčítání")
# print("3 - násobení")
# print("4 - dělení")
# cislo_operace = int(input("Zadejte číslo operace: "))
# if cislo_operace == 1:
#     print("Jejich součet je:", prvni_cislo + druhe_cislo)
# elif cislo_operace == 2:
#     print("Jejich rozdíl je:", prvni_cislo - druhe_cislo)
# elif cislo_operace == 3:
#     print("Jejich součin je:", prvni_cislo * druhe_cislo)
# elif cislo_operace == 4:
#     print("Jejich podíl je:", prvni_cislo / druhe_cislo)
# else:
#     print("Neplatná volba!")
# input("\nStiskněte libovolnou klávesu...")


print("Kalkulačka3\n")
pokracovat = True
while pokracovat:
    prvni_cislo = int(input("Zadejte první číslo: "))
    druhe_cislo = int(input("Zadejte druhé číslo: "))
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    print("5 - umocňování")
    cislo_operace = int(input("Zadejte číslo operace: "))
    if cislo_operace == 1:
        print("Jejich součet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Jejich rozdíl je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Jejich součin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        print("Jejich podíl je:", prvni_cislo / druhe_cislo)
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná volba!")
    nezadano = True
    while nezadano:
        odpoved = input("\nPřejete si zadat další příklad? y / n: ")
        if odpoved == "y" or odpoved == "Y":
            nezadano = False
        elif odpoved == "n" or odpoved == "N":
            nezadano = False
            pokracovat = False
        else:
            pass
input("\nStiskněte libovolnou klávesu...")