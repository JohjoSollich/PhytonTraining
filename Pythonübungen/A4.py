# Aufgabe 4: Schaltjahr
# Entwerfen Sie einen Algorithmus zu einem Programm, dass dem Benutzer nach Eingabe einer Jahreszahl ausgibt, ob das eingegebene Jahr ein Schaltjahr ist.
#
# Der heute gebräuchliche gregorianische Kalender beinhaltet eine Formel mit drei Kriterien, nach denen die Jahre in Gemein- und Schaltjahre unterteilt werden:
#
# Schaltjahre müssen durch 4 teilbar sein.
# Ist das Jahr auch durch 100 teilbar, ist es kein Schaltjahr, es sei denn...
# ...das Jahr ist ebenfalls durch 400 teilbar – dann ist es ein Schaltjahr.
# (Zusatzaufgabe: Schaltjahre gibt es erst seit dem Jahr 1582. Berücksichtigten Sie das in Ihrem Algorithmus)

# Eingabe
jahr = int(input("Bitte Jahreszahl eingeben: "))

# Logik
schaltjahr = False

if jahr > 1582 and jahr % 4 == 0:
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            schaltjahr = True
    else:
        schaltjahr = True

# Ausgabe
if schaltjahr:
    print(f"Das eingegebene Jahr {jahr} ist ein Schaltjahr")
else:
    print(f"Das eingegebene Jahr {jahr} ist kein Schaltjahr")
