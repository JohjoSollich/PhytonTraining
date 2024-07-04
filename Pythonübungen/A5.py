#Aufgabe 5: Würfelspiel (Differenzierung)
#Programmieren Sie ein Würfelspiel, das automatisch eine Ganzzahl
#zwischen 1 und 6 für zwei Spieler ermittelt.
#Anschließend soll der Gewinner ermittelt werden oder das Wort unentschieden
#ausgegeben werden. Gewonnen hat, wer die höhere Zahl gewürfelt hat.
#Falls ein Spieler mit einer Sechs gewonnen hat, soll zudem ausgegeben werden.
#"Glückwunsch, Sieg mit einer 6".

#Zusatzaufgabe: Es soll angegeben werden, ob es sich um einen knappen Sieg
#(Augenzahl ist nur maximal 1 höher) oder um einen deutlichen Sieg handelt.

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
