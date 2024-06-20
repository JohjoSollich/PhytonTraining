# Aufgabe 1: Bruttopreis berechnen
# Erstellen Sie einen Algorithmus für ein Programm, das nach Eingabe eines Bruttopreises
# (inkl. 19 % USt.) und eines Rabattsatzes (z.B. 12 %) den neuen Bruttopreis,
# die enhaltetene Umsatzsteuer und den Nettopreis berechnet und ausgibt.

bruttopreis = int(input("Bitte hier Bruttopreis eingeben: "))
rabattsatz = int(input("Bitte hier Rabattsatz eingeben: "))
bool = input("drucken? Ja / Nein: ")

bruttopreis_neu = bruttopreis - (bruttopreis * rabattsatz / 100)
nettopreis = bruttopreis_neu / 119 * 100
umsatzsteuer = bruttopreis_neu - nettopreis


if bool == "Ja":
    print("Bruttopreis: ", round(bruttopreis_neu, 2), "€")
    print("Nettopreis: ", round(nettopreis, 2), "€")
    print("Umsatzsteuer: ", round(umsatzsteuer, 2), "€")



