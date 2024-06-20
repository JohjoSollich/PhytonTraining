## Aufgabe 1: Bruttopreis berechnen
Erstellen Sie einen Algorithmus für ein Programm, das nach Eingabe eines Bruttopreises (inkl. 19 % USt.) und eines Rabattsatzes (z.B. 12 %) den neuen Bruttopreis, die enhaltetene Umsatzsteuer und den Nettopreis berechnet und ausgibt.

## Aufgabe 2: Verteilungsrechnung
Entwerfen Sie einen Algorithmus für die Verteilung eines Gewinns auf 3 Personen mit unterschiedlichen Einsätzen. Die drei Einsätze und der zu verteilende Gewinn soll zunächst eingegeben werden. Am Ende der Berechnung soll der jeweilige Gewinn je Person ausgegeben werden.

## Aufgabe 3: Firmenprämie berechnen
Eine Firma gewährt ihren Angestellten unter folgenden Bedingungen zu Weihnachten eine Prämie: Beträgt das Dienstalter (= Anzahl der Dienstjahre) weniger als ein Jahr, wird keine Prämie gegeben; beträgt es mindestens ein Jahr
aber weniger als sechs Jahre, besteht die Prämie aus 200 €.
Ist der Mitarbeiter sechs oder mehr Jahre bei der Firma, bekommt er 80 € und dazu für jedes Dienstjahr 20 €. Ist er im letzteren Fall außerdem älter als 50 Jahre, so erhält er noch eine Zulage von 50 €

## Aufgabe 4: Schaltjahr
Entwerfen Sie einen Algorithmus zu einem Programm, dass dem Benutzer nach Eingabe einer Jahreszahl ausgibt, ob das eingegebene Jahr ein Schaltjahr ist.

Der heute gebräuchliche gregorianische Kalender beinhaltet eine Formel mit drei Kriterien, nach denen die Jahre in Gemein- und Schaltjahre unterteilt werden:

Schaltjahre müssen durch 4 teilbar sein.
Ist das Jahr auch durch 100 teilbar, ist es kein Schaltjahr, es sei denn...
...das Jahr ist ebenfalls durch 400 teilbar – dann ist es ein Schaltjahr.
(Zusatzaufgabe: Schaltjahre gibt es erst seit dem Jahr 1582. Berücksichtigten Sie das in Ihrem Algorithmus)

## Aufgabe 5: Würfelspiel (Differenzierung)
Programmieren Sie ein Würfelspiel, das automatisch eine Ganzzahl zwischen 1 und 6 für zwei Spieler ermittelt. Anschließend soll der Gewinner ermittelt werden oder das Wort unentschieden ausgegeben werden. Gewonnen hat, wer die höhere Zahl gewürfelt hat. Falls ein Spieler mit einer Sechs gewonnen hat, soll zudem ausgegeben werden. Glückwunsch, Sieg mit einer 6.

Zusatzaufgabe: Es soll angegeben werden, ob es sich um einen knappen Sieg (Augenzahl ist nur maximal 1 höher) oder um einen deutlichen Sieg handelt.

## Aufgabe 6: Mäxchen
Sie sollen ein Programm für das Würfelspiel „Mäxchen“ schreiben. Zwei Spieler geben zu Beginn Ihren Namen ein. Anschließend würfelt jeder Spieler mit zwei Würfeln (generieren Sie zwei Zufallszahlen zwischen 1 und 6). Der Wert des Wurfes wird wie folgt bestimmt:

Wird eine 2 und eine 1 gewürfelt, hat man ein Mäxchen. Das ist der höchstmögliche Wert
Es folgen die Paschwürfe (zwei gleiche Zahlen). Je höher der Pasch, desto besser
Trifft keine der beiden ersten Varianten zu, wird der Wert des höherwertigen Würfels als Zehnerstelle, der des niederwertigen als Einerstelle interpretiert.
Es ergibt sich also die folgende Reihenfolge (aufsteigend nach Wertigkeit): 31, 32, 41, 42, 43, 51, 52, 53, 54, 61, 62, 63, 64, 65, 11, 22, 33, 44, 55, 66, 21

Das Programm soll den Wurfwert beider Spieler anzeigen und anschließend den Gewinner verkünden.