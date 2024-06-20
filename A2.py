# Aufgabe 2: Verteilungsrechnung
#
# Entwerfen Sie einen Algorithmus für die Verteilung eines Gewinns auf 3 Personen mit unterschiedlichen Einsätzen.
# Die drei Einsätze und der zu verteilende Gewinn soll zunächst eingegeben werden.
# Am Ende der Berechnung soll der jeweilige Gewinn je Person ausgegeben werden.

einsatz1 = int(input("Bitte Einsatz1 in € eingeben: "))
einsatz2 = int(input("Bitte Einsatz2 eingeben: "))
einsatz3 = int(input("Bitte Einsatz3 eingeben: "))
gewinn = int(input("Bitte Gewinn eingeben: "))

gesamteinsatz = einsatz1 + einsatz2 + einsatz3
faktor = gewinn / gesamteinsatz

gewinn_person1 = faktor * einsatz1
gewinn_person2 = faktor * einsatz2
gewinn_person3 = faktor * einsatz3

print("Gewinn für Person 1: ", gewinn_person1, "€")
print("Gewinn für Person 2: ", gewinn_person2, "€")
print("Gewinn für Person 3: ", gewinn_person3, "€")


# print(f"Person 1 erhält {gewinn_person1}€")


