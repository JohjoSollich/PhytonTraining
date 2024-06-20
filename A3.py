# Aufgabe 3: Firmenprämie berechnen
#
# Eine Firma gewährt ihren Angestellten unter folgenden Bedingungen zu Weihnachten eine Prämie:
# Beträgt das Dienstalter (= Anzahl der Dienstjahre) weniger als ein Jahr, wird keine Prämie gegeben;
# beträgt es mindestens ein Jahr aber weniger als sechs Jahre, besteht die Prämie aus 200 €.
# Ist der Mitarbeiter sechs oder mehr Jahre bei der Firma, bekommt er 80 € und dazu für jedes Dienstjahr 20 €.
# Ist er im letzteren Fall außerdem älter als 50 Jahre, so erhält er noch eine Zulage von 50 €

dienstjahre = int(input("Bitte Dienstjahre eingeben: "))
alter = int(input("Bitte Ihr Alter eingeben: "))

if dienstjahre < 1:
    prämie = 0
elif dienstjahre < 6:
    prämie = 200
else:
    prämie = 80 + (20*dienstjahre)
    if alter > 50:
        prämie = prämie + 50


print(f"Der Mitarbeiter erhält eine Prämie in höhe von {prämie}€")