import random
darab = 0
print("A generált számok közül a 3-mal oszthatók:")
for _ in range(20):
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        darab = darab + 1
print(f"Összesen {darab} darab 3-mal osztható szám volt a 20 közül.")
