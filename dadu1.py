# program dua dadu oleh NIM 030

import random
for x in range(1, 11):  # simualsi 10 kali lemparan
    lempar_1 = random.randint(1, 6)
    lempar_2 = random.randint(1, 6)
    total = lempar_1 + lempar_2
    print(total)
    if total == 7:
        print('Lemparan Angka 7')
    if total == 11:
        print('Lemparan Angka 11')
    if lempar_1 == lempar_2:
        print('Lemparan Angka DOUBLE')
