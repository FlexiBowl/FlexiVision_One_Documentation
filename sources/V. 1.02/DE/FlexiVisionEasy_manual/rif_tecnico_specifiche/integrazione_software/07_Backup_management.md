(backup)=
# **BackUp Management**

## Überblick

Die gesamte Konfiguration von FlexiVision One – Hardware-Einrichtung, Kalibrierungen, Werkstückmodelle und Protokollparameter – ist in den Rezeptdateien enthalten. Aus diesem Grund sind Backups unerlässlich, um alle Daten zu sichern.

```{important}
Es wird empfohlen, nach jeder Erstellung oder wesentlichen Änderung eines Rezepts, vor der Aktualisierung der FlexiVision-Software sowie vor jedem Hardwareeingriff am System eine Datensicherung durchzuführen.

**Mindestanforderung**: mindestens einmal pro Woche im normalen Betrieb.
```

---

## Backup-Verfahren

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Schritt**
  - **Aktion**
* - Auf „Backup“ klicken
  - Klicken Sie im Menü „Rezepte“ auf die Schaltfläche „Backup“.
* - FlexiVision-Ordner auswählen
  - Suchen Sie den Laufzeitordner von FlexiVision One auf dem VisionController.
* - Zielordner wählen
  - Wählen Sie den Zielordner für das Backup aus.
* - Benennung mit Datum
  - Vergeben Sie immer einen Namen, der das Datum, die Softwareversion und die System-ID oder andere nützliche Informationen wie den Kundennamen enthält. Beispiele:
    
    - `FV_Recipes_LineA_20260402_SW1.2.xml`
    - `Backup_FlexiVision_ClientABC_Plant3_20260402.xml`
    - `Recipes_FB500_Commissioning_20260315_v1.zip`
    
    Geben Sie die Softwareversion (auf der Startseite sichtbar) im Namen oder in einer angehängten Textdatei an.
```

---

## Vorgehensweise beim Importieren des Backups

```{list-table}
:header-rows: 1
:widths: 30 70

* - **Schritt**
  - **Aktion**
* - Auf „Backup importieren“ klicken
  - Klicken Sie im Bereich „Rezepte“ auf „Backup importieren“.
* - FlexiVision-Laufzeitordner auswählen
  - **Wählen Sie den Ordner aus, der die FlexiVision-Installation enthält.**
* - Pfad der Sicherungsdatei auswählen
  - Geben Sie den Pfad zur Sicherungsdatei an. FlexiVision wird während dieses Vorgangs neu gestartet.
* - Überprüfungen nach der Wiederherstellung
  - Führen Sie nach der Wiederherstellung die folgenden Überprüfungen durch, bevor Sie die Produktion neu starten:

    1. Überprüfen Sie, ob alle erwarteten Rezepte in der Liste auf der Seite „Rezepte“ vorhanden sind.
    2. Vergewissern Sie sich, dass das Hauptrezept fehlerfrei geladen werden kann.
    3. Überprüfen Sie, ob FlexiBowl® und die Verbindungstests der Kamera in der Kameraeinstellung positiv (grün) sind.
    4. Vergewissern Sie sich, dass das Dashboard die korrekt verbundenen Geräte anzeigt.

    **Führen Sie einen Testlauf mit dem operativen Hauptrezept durch, um die korrekte Funktion zu überprüfen.**
```

---

## Korrekte Verwaltung der Rezepte

```{list-table}
:header-rows: 1
:widths: 25 37 38

* - **Aktion**
  - **Richtige Vorgehensweise**
  - **Zu vermeidende Vorgehensweise**
* - Ein Rezept umbenennen
  - Seite „Rezepte“ → Funktion „Umbenennen“ in der Software.
  - Die XML-Datei über den Datei-Explorer umbenennen.
* - Ein Rezept löschen
  - Rezeptseite → Schaltfläche „**Rezept löschen“**.
  - Die XML-Datei manuell löschen.
* - Ein Rezept auf ein anderes System kopieren
  - Rezeptseite → Backup → „Sicherung importieren“ auf dem anderen System.
  - Die XML-Dateien zwischen zwei „Rezepte“-Ordnern kopieren und einfügen.
* - Einen Rezeptparameter ändern
  - Das Rezept im **Bearbeitungsmodus** in der Software öffnen.
  - Die XML-Datei mit einem Texteditor bearbeiten.
```
