
class Mesiac:
    def __init__(self, nazov, pocet_dni, poradie):
        self.nazov = nazov
        self.pocet_dni = pocet_dni
        self.poradie = poradie

    def __str__(self):
        return self.nazov

mesiace = [
    Mesiac('Januar', 31, 1),
    Mesiac('Februar', 28, 2),
    Mesiac('Marec', 31, 3),
    Mesiac('April', 30, 4),
    Mesiac('Maj', 31, 5),
    Mesiac('Jun', 30, 6),
    Mesiac('Jul', 31, 7),
    Mesiac('August', 31, 8),
    Mesiac('September', 30, 9),
    Mesiac('Oktober', 31, 10),
    Mesiac('November', 30, 11),
    Mesiac('December', 31, 12)
]

den_v_tyzdni = 7

for mesiac in mesiace:
    print(mesiac.nazov)
    print('  P   U   S   S   P   S   N')

    print('    ' * (den_v_tyzdni - 1), end='')
    pocet = den_v_tyzdni - 1

    for i in range(mesiac.pocet_dni):
        if pocet != 0 and pocet % 7 == 0:
            print()

        print('{:3}'.format(i + 1), end=' ')
        pocet += 1

    den_v_tyzdni = (mesiac.pocet_dni + den_v_tyzdni - 1) % 7 + 1

    print()
    print()
