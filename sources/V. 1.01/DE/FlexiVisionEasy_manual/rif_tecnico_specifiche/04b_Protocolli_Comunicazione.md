(protocollo)=
# **Kommunikationsprotokoll zwischen Roboter und Bildverarbeitungssystem**

FlexiVision One kommuniziert mit dem Roboter über das **TCP/IP**-Protokoll in einem Ethernet-Netzwerk.

## Protokollspezifikationen

```{list-table}
:header-rows: 1
:widths: 35 65

* - Parameter
  - Wert
* - Protokoll
  - TCP/IP
* - Port
  - Konfigurierbar (Standard: FB1 → 4001 ; FB2 → 4002 ; FB3 → 4003)
* - Abschlusszeichen
  - CHR(13) - Carriage Return
* - Datenformat
  - ASCII-Zeichenfolge
* - Timeout
  - Konfigurierbar (Standard: 5000 ms)
* - Encoding
  - UTF-8
```

## Verfügbare Befehle

Das System unterstützt die folgenden Befehle über Textzeichenfolgen, die über die TCP/IP-Verbindung gesendet werden.

### *Rezeptverwaltung*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `set_recipe=<Name>`
  - Lädt das angegebene Rezept und startet die Synchronisierung der verbundenen FlexiBowl®-Einheiten.
  - Keiner
* - `get_recipe`
  - Gibt den Namen des aktuell geladenen Rezepts zurück.
  - `<Rezeptname>`
```

Beispiel:

```
set_recipe=MyRecipe
```

oder:

```
get_recipe
→ MyRecipe
```

### *Locator-Befehle*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `start_Locator`
  - Startet den Prozess zur Teilelokalisierung. Sind keine greifbaren Teile vorhanden, wird automatisch die Bewegungsroutine des FlexiBowl® aufgerufen. Ist der Locator bereits aktiv, wird der Befehl ignoriert und der Prozess nicht neu gestartet.
    :::{important}
    Ist zum Zeitpunkt des Befehls kein Modell ausgewählt/aktiviert, gibt das System eine Fehlermeldung zurück und der Locator wird nicht gestartet.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Stoppt den Lokalisierungsprozess.
  - Keiner
* - `turn_Locator`
  - Wurde kein Teil aufgenommen, fordert der Befehl eine neue FlexiBowl®-Bewegung an und startet den Suchprozess neu.
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Startet die Lokalisierung ohne Aktivierung des FlexiBowl®; es werden nur die Bildaufnahme und die Bildsuche durchgeführt.
  - `Pattern_n;x;y;r` / Keiner
* - `state_Locator`
  - Gibt den Diagnosestatus des Lokalisierungsprozesses zurück.
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
* - `mix_Locator_<Modelle>`
    :::{tip}
    Weitere Informationen finden Sie im [Abschnitt zu den Mix-Befehlen](mix)
    :::
  - Wählt dynamisch ein oder mehrere Modelle aus und startet den Locator. Zuvor ausgewählte Modelle werden zuerst deaktiviert. Verfügbare Zahlen sind 1 bis 8 (z. B. `mix_Locator_12`, `mix_Locator_248`, `mix_Locator_12345678`).
    :::{note}
    Läuft der Locator bereits, wird der Befehl ignoriert und die aktuelle Auswahl bleibt unverändert.
    :::
  - Normales Locator-Ergebnis / `#Error_mix_locator_not_valid` (wenn kein gültiges Modell gefunden wird)
```

:::{note}
Weitere verfügbare Trennzeichen neben `;` sind: `,`, `|`, `:`, `&`, `$`, `@`, `#`.
:::

:::{note}
Bei `start_Locator` und `mix_Locator_<Modelle>` wird, wenn der Locator bereits läuft, keine Antwort an den Roboter gesendet.
:::

### *FlexiBowl®-Befehle – Emptying*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `start_Empty`
  - Startet die Schnellentleerungssequenz (Quick-Emptying) des FlexiBowl®. Der Befehl kann nicht ausgeführt werden, während der Locator aktiv ist.
  - `Start_Empty Started` / `Locator is Running` / `#Error_flexibowl_not_connect`
* - `stop_Empty`
  - Stoppt die Entleerungssequenz des FlexiBowl®.
  - `Stop_Empty Command Sent` / `#Error_flexibowl_not_connect`
* - `state_Empty`
  - Gibt den aktuellen Status der Entleerungssequenz zurück.
  - `Emptying Running` / `Emptying Stopped` / `#Error_flexibowl_not_connect` / `#Error_invalid_emptying_state`
```

### *Optionale Hopper-Signale*

```{note}
Muss der Hopper aktiviert werden, wird folgende Zeichenfolge empfangen: `"Hopper;signalnumber;time"`
```

## Allgemeine Fehler

```{note}
**FlexiVision-Lizenz**: Ist die Softwarelizenz nicht aktiv, werden Roboterbefehle abgelehnt und es wird Folgendes zurückgegeben:
`#Error_License_not_active`
```

---

## Erweiterte Befehle / Service-Befehle

Die folgenden Befehle sind ausschließlich für technisches Personal.

### *FlexiBowl®-Verbindung*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `connect_flb`
  - Fordert die Verbindung zum FlexiBowl® an. Besteht keine Verbindung, wird die entsprechende Verbindungsaufgabe gestartet.
  - `#Flb1_connected` / `#Flb1_Not_connected`
```

---

Für detaillierte Informationen zur physischen Installation und den elektrischen Anschlüssen fahren Sie mit den folgenden Abschnitten fort:
- [Berechnung des optimalen Kameraabstands](05_Calcolo_distanza_ottimale.md)
- [Mechanische Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Verkabelung und Anschlüsse](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)
