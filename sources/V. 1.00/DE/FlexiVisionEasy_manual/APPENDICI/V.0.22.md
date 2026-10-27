# V. 0.22


## **Neue Funktionen**

### Mix-Anwendungen

- Die kombinierte Verwaltung der `mix_Locator`-Befehle für Roboter 1, Roboter 2 und Roboter 3 wurde hinzugefügt: Es können nun mehrere Modelle gleichzeitig innerhalb einer einzigen Zeichenfolge aufgerufen werden (z. B. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
- Eine Gültigkeitsprüfung für `mix_Locator`-Befehle wurde hinzugefügt: Enthält die empfangene Zeichenfolge keine gültigen Modelle (von 1 bis 8), gibt das System einen eigenen Fehler zurück.
- Für die Befehle `start_Locator` und `mix_Locator` wurde ein Schutz hinzugefügt: Läuft bereits ein Locator, wird der Befehl ignoriert. Dadurch werden unerwünschte Neustarts des Tasks und unerwartete Änderungen an den aktiven Modellen vermieden.

### Clearances (Histogramme)

- Es wurde die Unterstützung von drei Regionstypen für die Histogram-Tools hinzugefügt — **Rechteck**, **Kreisringsegment** und **Kreis** —, die über ein eigenes Menü auf der Rezeptseite für alle verfügbaren Modelle und Histogramme ausgewählt werden können.
- Die Seite Test Histogram wurde aktualisiert, um die neuen Regionstypen korrekt darzustellen; sie werden je nach Ergebnis der Prüfung grün oder rot gezeichnet.
- Die grafische Anzeige des Histogram-Index und der wichtigsten Messwerte der ausgewählten Region wurde hinzugefügt.

### FlexiBowl®

- Die Funktion **Belt Check** zur Kontrolle von Verschleiß- und Sauberkeitszustand des Bandes wurde hinzugefügt:
  - Aufnahme eines Referenzbildes des sauberen Bandes über die Schaltfläche **Save Clean Reference**;
  - automatischer Vergleich zwischen Referenzbild und aktuellem Bild des Bandes mittels Histogram;
  - automatische Klassifizierung des Bandes in **Light**, **Dark** oder **Medium** anhand der Helligkeit der Referenz;
  - Anzeige des Bandzustands mit Prozentwert, Farbe und Textangabe (**Good**, **Warning**, **Poor**);
  - Anzeige des Datums des letzten Belt Check für jeden FlexiBowl®.
- Der geführte Ablauf **Hopper Step Setup** wurde hinzugefügt, um die Anzahl der Sequenzen zu berechnen, die zum Erreichen des Trichterbereichs erforderlich sind, mit den Funktionen **Reset Steps**, **Test Sequence** und **Save Hopper Step** sowie der zugehörigen Anzeige des Kalibrierungsstatus.
- Es wurde die Möglichkeit hinzugefügt, die Parameter der FlexiBowl® manuell über die Tastatur einzugeben, als Alternative zur Einstellung per Slider.
- Eine nicht modale Warnmeldung wurde hinzugefügt, wenn die Parameter eines FlexiBowl® geändert, aber noch nicht mit dem realen Gerät synchronisiert wurden.
- **Auto Reset FlexiBowl** wurde hinzugefügt: Liegt beim Start eines Bewegungsbefehls bereits ein Fehler vor, führt das System automatisch den Reset durch, bevor der Befehl gestartet wird.

### Sicherheit und Zugriffe

- Für die allgemeinen Schaltflächen der Oberfläche wurde die Prüfung der Zugriffsebene hinzugefügt: Geschützte Funktionen prüfen vor der Ausführung die aktuelle Benutzerebene und zeigen bei unzureichenden Berechtigungen eine Meldung an.

## **Verbesserungen**

### Assistent zur Rezepterstellung

- Der Schaltfläche **NEXT** wurde eine Prüfung des Picking Offset hinzugefügt: Ist der Offset aktiviert, muss er berechnet und gültig sein, bevor im Assistenten fortgefahren werden kann.

### Rezeptoberfläche

- Das Anzeigeformat der Robot-Pick-Offsets auf den Rezeptseiten wurde korrigiert; als Dezimaltrennzeichen wird nun der Punkt anstelle des Kommas erzwungen.

## **Behobene Probleme**

### Backup-Verwaltung

- Ein Fehler bei der Backup-Erstellung wurde behoben, der auftrat, wenn der Pfad auf dem PC Leerzeichen enthielt.

### Sequenzen

- Ein Anzeigeproblem wurde behoben, durch das in der Sequenzliste scheinbar doppelte Befehle angezeigt werden konnten.
