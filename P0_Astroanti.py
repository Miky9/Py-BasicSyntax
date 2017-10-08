#!/usr/bin/env/Python3

# from termcolor import colored
# from clint.textui import colored
from colorama import Fore, Back, Style

# functions
# def swap (item1, item2):
#     mergedlist[i], mergedlist[j] = mergedlist[j], mergedlist[i]


print("Program for clash simulation of astroants' invasion\n")

enum = {"red", "blue", "green", "yellow"}

# color1 = input("Please select color of first astroants' group (red / blue / green / yellow): ")
# size1 = input("Please select size of first astroants' group ({0}): ".format(color1))
color1 = "red"
size1 = 3
# color2 = input("Please select color of second astroants' group (red / blue / green / yellow): ")
# size2 = input("Please select size of second astroants' group ({0}): ".format(color1))
color2 = "yellow"
size2 = 3
# numIt = input("Please select number of iterations: ")
numIt = 5

color1s = color1[0].upper()
color2s = color2[0].upper()
# color1s = Fore.{0}.format(color1.upper())
color1s = Fore.RED
color2s = Fore.YELLOW

print ('Initial state:')

print("{0} astroants: ".format(color1), end='')
seznam1 = list()
for i in range(int(size1)):
    seznam1.append(color1s + chr(i + 97).upper())
print(', '.join(seznam1), Style.RESET_ALL)

print("{0} astroants: ".format(color2), end='')
seznam2 = list()
xx = 97 + size1
for i in range(int(size2)):
    seznam2.append(color2s + chr(i + xx).upper())
print(', '.join(seznam2), Style.RESET_ALL)

print("\nBefore clash:")
# seznam1.reverse()
# print ('  '.join(seznam1), end='  ---  ')
# print ('  '.join(seznam2))
mergedList = seznam1 + seznam2
print('  '.join(mergedList))


for x in range(0, numIt):
    print(Style.RESET_ALL)
    print("Step {0}: ".format(x+1))

    if x == 0:
        i = len(seznam1) - 1
        j = len(seznam1)
        mergedList[i], mergedList[j] = mergedList[j], mergedList[i]   # switch

    elif (x % 2 == 0) & (x > 0):
        for i in range(0, (len(mergedList) ), 2):
            j = i + 1
            mergedList[i], mergedList[j] = mergedList[j], mergedList[i]

    else:
        for i in range(1, (len(mergedList)-2), 2):
            j = i + 1
            mergedList[i], mergedList[j] = mergedList[j], mergedList[i]

    print('  '.join(mergedList))


    # for y in range(0, numIt, 2):
    #     mergedlist[i], mergedlist[j] = mergedlist[j], mergedlist[i]
    #     print('  '.join(mergedlist))
    #
    # switchCount = x+1
    # for q in range(0, switchCount):
    #     mergedlist[i], mergedlist[j] = mergedlist[j], mergedlist[i]
    #     i = i - 1
    #     j = j - 1
    #     mergedlist[i], mergedlist[j] = mergedlist[j], mergedlist[i]
    #     i = i + 1
    #     j = j + 1



print(Style.RESET_ALL)
input("\nNext...\n")
