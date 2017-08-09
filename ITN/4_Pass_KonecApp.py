print("Dotěrná aplikace")
pokracovat = True
while pokracovat:
    slovo = input("\nNapište Python pro ukončení: ")
    if slovo == "Python" or slovo == "python":
        print("\nSlovo zadáno!")
        pokracovat = False
    else:
        pass # nic se nestane
input("\nAplikaci ukončíte stisknutím libovolné klávesy...")
