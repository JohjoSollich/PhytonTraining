
import random

spieler1_name = input("Spieler 1, bitte geben Sie Ihren Namen ein: ")
spieler2_name = input("Spieler 2, bitte geben Sie Ihren Namen ein: ")

spieler1_wurf =  (random.randint(1, 6), random.randint(1, 6))
spieler2_wurf =  (random.randint(1, 6), random.randint(1, 6))
spieler1_value = 0
spieler2_value = 0

print(f"{spieler1_name} hat {spieler1_wurf} gewürfelt.")
print(f"{spieler2_name} hat {spieler2_wurf} gewürfelt.")


if spieler1_wurf == (1, 2) or spieler1_wurf == (2, 1):
    spieler1_wert = 21
    spieler1_value = spieler1_wert * 100
elif spieler1_wurf[0] == spieler1_wurf[1]:
    spieler1_wert = spieler1_wurf[0] * 10 + spieler1_wurf[1]
    spieler1_value = spieler1_wert * 10
else:
    spieler1_wert = max(spieler1_wurf) * 10 + min(spieler1_wurf)
    spieler1_value = spieler1_wert

if spieler2_wurf == (1, 2) or spieler2_wurf == (2, 1):
    spieler2_wert = 21
    spieler2_value = spieler2_wert * 100
elif spieler2_wurf[0] == spieler2_wurf[1]:
    spieler2_wert = spieler2_wurf[0] * 10 + spieler2_wurf[1]
    spieler2_value = spieler2_wert * 10
else:
    spieler2_wert = max(spieler2_wurf) * 10 + min(spieler2_wurf)
    spieler2_value = spieler2_wert

print(f"{spieler1_name} hat einen Wurfwert von {spieler1_wert}.")
print(f"{spieler2_name} hat einen Wurfwert von {spieler2_wert}.")

if spieler1_value > spieler2_value:
    gewinner = spieler1_name
elif spieler2_value > spieler1_value:
    gewinner = spieler2_name
else:
    gewinner = "Unentschieden"

print("Gewinner:", gewinner)
