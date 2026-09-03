# V. 0.22


```{note}
Diese Seite bezieht sich auf die Version **1.01** dieses Handbuchs, die mit **FlexiVision Studio v0.21** und **v0.22** kompatibel ist.
```

## **Neue Funktionen**

### Mix-Anwendungen

- Kombinierte Verwaltung der Befehle `mix_locator` für Roboter 1, Roboter 2 und Roboter 3 hinzugefügt: Es ist nun möglich, mehrere Modelle gleichzeitig innerhalb einer einzigen Zeichenfolge aufzurufen (z. B. `mix_locator_12`, `mix_locator_248`, `mix_locator_12345678`).
- Eine Gültigkeitsprüfung für die Befehle `mix_locator` wurde hinzugefügt: Wenn die übergebene Zeichenfolge keine gültigen Modelle (von 1 bis 8) enthält, gibt das System einen entsprechenden Fehler zurück.
- Es wurde eine Schutzfunktion für die Befehle `start_locator` und `mix_locator` hinzugefügt: Wenn ein Locator bereits ausgeführt wird, wird der Befehl ignoriert, wodurch ungewollte Neustarts der Aufgabe und unerwartete Änderungen an den aktiven Vorlagen vermieden werden.

### Clearances (Histogramme)

- Es wurde die Unterstützung für drei Arten von Bereichen für die Histogramm-Werkzeuge hinzugefügt – **Rechteck**, **Ringsektor** und **Kreis** –, die über ein spezielles Menü auf der Rezeptseite für alle verfügbaren Modelle und Histogramme ausgewählt werden können.
- Die Seite „Histogramm-Test“ wurde aktualisiert, um die neuen Bereichstypen korrekt anzuzeigen, die je nach Prüfergebnis in Grün oder Rot dargestellt werden.
- Es wurde eine grafische Darstellung des Histogramm-Index und der wichtigsten Messwerte des ausgewählten Bereichs hinzugefügt.

### FlexiBowl®

- Die Funktion **Belt Check** zur Überprüfung des Verschleißzustands und der Sauberkeit des Bandes wurde hinzugefügt:
  - Aufnahme eines Referenzbildes des sauberen Bandes über die Schaltfläche **Save Clean Reference**;
  - automatischer Vergleich des Referenzbildes mit dem aktuellen Bild des Bandes mittels Histogramm;
  - Automatische Einstufung des Bandes in **Light**, **Dark** oder **Medium** je nach Helligkeit des Referenzbildes;
  - Anzeige des Bandzustands mit Prozentwert, Farbe und Textangabe (**Good**, **Warning**, **Poor**);
  - Anzeige des Datums der letzten Belt-Check-Prüfung für jeden FlexiBowl®.
- Der Assistent **Hopper Step Setup** wurde hinzugefügt, um die Anzahl der erforderlichen Sequenzen bis zum Erreichen des Trichterbereichs zu berechnen, mit den Funktionen **Reset Steps**, **Test Sequence** und **Save Hopper Step** sowie einer entsprechenden Anzeige des Kalibrierungsstatus.
- Es wurde die Möglichkeit hinzugefügt, die Parameter der FlexiBowl®-Geräte manuell über die Tastatur einzugeben, als Alternative zur Einstellung über Schieberegler.
- Es wurde eine nicht-modale Warnmeldung hinzugefügt, wenn die Parameter eines FlexiBowl®-Geräts geändert werden, aber noch nicht mit dem tatsächlichen Gerät synchronisiert sind.
- **Auto Reset FlexiBowl** hinzugefügt: Liegt beim Start eines Bewegungsbefehls bereits ein Fehler vor, führt das System automatisch einen Reset durch, bevor der Befehl gestartet wird.

### Sicherheit und Zugriffsrechte

- Es wurde eine Überprüfung der Zugriffsebene für die allgemeinen Schaltflächen der Benutzeroberfläche hinzugefügt: Geschützte Funktionen überprüfen vor der Ausführung die aktuelle Benutzerebene und zeigen bei unzureichenden Berechtigungen eine Meldung an.

## **Verbesserungen**

### Rezept-Assistent

- Der Schaltfläche **NEXT** wurde eine Überprüfung des Picking-Offsets hinzugefügt: Wenn der Offset aktiviert ist, muss er berechnet und gültig sein, bevor im Assistenten fortgefahren werden kann.

### Rezept-Oberfläche

- Das Anzeigeformat der Robot-Pick-Offsets auf den Rezeptseiten wurde korrigiert, sodass nun der Punkt anstelle des Kommas als Dezimaltrennzeichen verwendet wird.

## **Gelöste Probleme**

### Backup-Verwaltung

- Ein Fehler bei der Erstellung des Backups wurde behoben, der auftrat, wenn der Pfad auf dem PC Leerzeichen enthielt.

### Sequenzen

- Ein Darstellungsfehler wurde behoben, durch den Befehle in der Liste der Sequenzen scheinbar doppelt angezeigt werden konnten.
