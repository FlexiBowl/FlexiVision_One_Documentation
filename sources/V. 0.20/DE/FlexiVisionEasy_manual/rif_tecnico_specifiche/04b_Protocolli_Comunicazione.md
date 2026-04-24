(protocollo)=
# **Kommunikationsprotokoll Roboter-Bildverarbeitung**

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
  - ASCII-Zeichenkette
* - Timeout
  - Konfigurierbar (Standard: 5000 ms)
* - Encoding
  - UTF-8
```

## Verfügbare Befehle

Das System unterstützt die folgenden Befehle über Textzeichenketten, die über die TCP/IP-Verbindung gesendet werden:

### Rezeptverwaltung

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `set_Recipe=nome_ricetta`
  - Lädt die Rezeptur, die dem angegebenen "nome_ricetta" entspricht
  - Keiner
* - `get_Recipe`
  - Gibt den Namen der aktuell geladenen Rezeptur zurück
  - `nome_ricetta`
```

### Lokalisierungsbefehle

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `start_Locator`
  - Startet den Prozess zur Lokalisierung der Teile. Wenn keine entnehmbaren Teile vorhanden sind, wird automatisch die FlexiBowl-Bewegungsroutine aufgerufen.
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Stoppt den Lokalisierungsprozess
  - Keiner
* - `turn_Locator`
  - Wenn kein Teil entnommen wurde, dreht er den FlexiBowl und startet die Suche erneut
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Startet die Lokalisierung ohne Aktivierung des FlexiBowl (nur Bildaufnahme)
  - `Pattern_n;x;y;r`/ Keiner
* - `state_Locator`
  - Gibt den Diagnosestatus des Locators zurück
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```

### FlexiBowl-Befehle

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `start_Empty`
  - Startet die Schnellleerungssequenz (Quick-Emptying) des FlexiBowl
  - `start_Empty ended`
```


### Optionale Hopper-Signale

```{note}
Wenn der Hopper aktiviert werden muss, erhalten wir die Zeichenkette: `"Hopper;signalnumber;time"`

```



Für detaillierte Informationen zur physischen Installation und zu den elektrischen Anschlüssen fahren Sie mit den folgenden Abschnitten fort:
- [Berechnung des optimalen Kameraabstands](05_Calcolo_distanza_ottimale.md)
- [Mechanische Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Verkabelung und Anschlüsse](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

