(backup)=
# **BackUp Management**

## **Übersicht**

Das Backup von FlexiVision One besteht aus dem Kopieren des Ordners `Recipes`, der sich auf dem VisionController befindet. Dieser Ordner enthält alle im System konfigurierten Rezepturen — einschließlich Modelle, Erkennungsparameter und zugehörige Einstellungen — und stellt die einzigen zu sichernden Benutzerdaten dar.

Da kein spezielles Werkzeug erforderlich ist, reduziert sich der Backup-Prozess auf einen einfachen Kopieren-und-Einfügen-Vorgang über den Datei-Explorer.
```{important}
Es wird empfohlen, jedes Mal ein Backup auszuführen, wenn eine Rezeptur erstellt oder geändert wird, und in jedem Fall vor jedem Softwareupdate oder Wartungseingriff am VisionController.
```

---

## **Backup-Inhalt**

Innerhalb des Installationsordners von FlexiVision One ist die folgende Struktur vorhanden:
```
C:\FlexiVision One\
├── Data\
├── Languages\
├── Recipes\          ← unica cartella da includere nel backup
├── Flexivision_Smart_018
└── Package.dat
```

Der einzige Ordner, der Benutzerdaten enthält, ist `Recipes\`. Die anderen vorhandenen Ordner und Dateien gehören zur Softwareinstallation und dürfen nicht in das Backup aufgenommen werden.
```{note}
Der genaue Pfad des Installationsordners kann je nach Systemkonfiguration variieren. Im Zweifelsfall den Pfad in den Softwareeinstellungen prüfen.
```

---

## **Backup-Verfahren**
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Schritt**
  - **Aktion**
* - 1
  - Sicherstellen, dass die Software FlexiVision One **geschlossen** ist.
* - 2
  - Den Datei-Explorer auf dem VisionController öffnen und zu `C:\FlexiVision One\` navigieren.
* - 3
  - Mit der rechten Maustaste auf den Ordner `Recipes` klicken und **Kopieren** auswählen.
* - 4
  - Zum gewünschten Backup-Ziel navigieren (USB-Stick, Netzwerkordner, NAS usw.).
* - 5
  - Den Ordner am Ziel einfügen. Es wird empfohlen, ihn mit Datum umzubenennen, zum Beispiel: `Recipes_backup_2025-06-01`.
```
```{warning}
Das Backup nicht ausführen, während die Software FlexiVision One läuft. Das Kopieren geöffneter Dateien kann unvollständig oder beschädigt sein.
```

---

## **Wiederherstellungsverfahren (Restore)**

Bei Datenverlust oder Austausch des VisionController können die vorherigen Rezepturen mit den folgenden Schritten wiederhergestellt werden:
```{list-table}
:header-rows: 1
:widths: 10 90

* - **Schritt**
  - **Aktion**
* - 1
  - Sicherstellen, dass FlexiVision One auf dem VisionController installiert und **geschlossen** ist.
* - 2
  - Den Datei-Explorer öffnen und zu `C:\FlexiVision One\` navigieren.
* - 3
  - Den vorhandenen Ordner `Recipes` als Vorsichtsmaßnahme umbenennen (z. B. `Recipes_old`).
* - 4
  - Den Backup-Ordner nach `C:\FlexiVision One\` kopieren und in `Recipes` umbenennen.
* - 5
  - FlexiVision One starten: Alle zuvor gespeicherten Rezepturen sind wieder verfügbar.
```
```{important}
Die auf dem VisionController installierte Softwareversion muss mit der Version kompatibel sein, die zum Zeitpunkt des Backups verwendet wurde. Bei einem Softwareupdate vor der Wiederherstellung den technischen Support kontaktieren.
```

---

## **Empfehlungen**

- Mindestens **zwei Backup-Kopien** an getrennten physischen Orten aufbewahren (z. B. ein lokaler USB-Stick und ein entfernter Netzwerkordner).
- Backups immer mit **Datum und Softwareversion** kennzeichnen, um ihre spätere Identifizierung zu erleichtern.
- Den Inhalt des Ordners `Recipes` nicht manuell ändern: Rezepturen dürfen ausschließlich über die FlexiVision One Oberfläche verwaltet werden.
```{tip}
Für Umgebungen mit mehreren VisionController Einheiten wird empfohlen, die Backups in einem freigegebenen Netzwerkordner zu zentralisieren, organisiert nach Maschinenname und Datum.
```
