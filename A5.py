import random

spieler1 = random.randint(1, 6)
spieler2 = random.randint(1, 6)

print("Spieler 1 hat eine", spieler1, "gewürfelt.")
print("Spieler 2 hat eine", spieler2, "gewürfelt.")

if spieler1 > spieler2:
    print("Spieler 1 gewinnt!")
    if spieler1 == 6:
        print("Glückwunsch, Sieg mit einer 6")
elif spieler2 > spieler1:
    print("Spieler 2 gewinnt!")
    if spieler2 == 6:
        print("Glückwunsch, Sieg mit einer 6")
else:
    print("Unentschieden!")

differenz = abs(spieler1 - spieler2)
if differenz == 1:
    print("Knapper Sieg!")
elif differenz > 1:
    print("Deutlicher Sieg!")
