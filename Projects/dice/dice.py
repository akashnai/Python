import random
import os


q = True
while (q != "q"):
    x = random.randint(1, 6)

    if x == 1:
        os.system("cls")
        print(f"|---------|")
        print(f"|         |")
        print(f"|    0    |")
        print(f"|         |")
        print(f"|---------|")
    if x == 2:
        os.system("cls")
        print(f"|---------|")
        print(f"|         |")
        print(f"|  0   0  |")
        print(f"|         |")
        print(f"|---------|")
    if x == 3:
        os.system("cls")
        print(f"|---------|")
        print(f"|    0    |")
        print(f"|         |")
        print(f"|  0   0  |")
        print(f"|---------|")
    if x == 4:
        os.system("cls")
        print(f"|---------|")
        print(f"|  0   0  |")
        print(f"|         |")
        print(f"|  0   0  |")
        print(f"|---------|")
    if x == 5:
        os.system("cls")
        print(f"|---------|")
        print(f"|    0    |")
        print(f"|  0   0  |")
        print(f"|  0   0  |")
        print(f"|---------|")
    if x == 6:
        os.system("cls")
        print(f"|---------|")
        print(f"|  0   0  |")
        print(f"|  0   0  |")
        print(f"|  0   0  |")
        print(f"|---------|")
    q = input("Press any button(q for exit)")
