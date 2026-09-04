(protocollo)=
# **Kommunikationsprotokoll zwischen Roboter und Bildverarbeitungssystem**

FlexiVision One kommuniziert mit dem Roboter über das TCP/IP-Protokoll im Ethernet-Netzwerk.

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
* - Terminierungszeichen
  - CHR(13) - Carriage Return
* - Datenformat
  - ASCII-String
* - Timeout
  - Konfigurierbar (Standard: 5000 ms)
* - Encoding
  - UTF-8
```

## Verfügbare Befehle

Das System unterstützt die folgenden Befehle über Textstrings, die über die TCP/IP-Verbindung gesendet werden:

### *Rezeptverwaltung*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `set_Recipe=nome_ricetta`
  - Lädt das Rezept, das dem angegebenen „nome_ricetta“ entspricht
  - Keine
* - `get_Recipe`
  - Gibt den Namen des aktuell geladenen Rezepts zurück
  - `nome_ricetta`
```

### *Befehle zur Lokalisierung*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `start_Locator`
  - Startet den Prozess zur Lokalisierung der Teile. Wenn keine aufnehmbaren Teile vorhanden sind, ruft automatisch die Bewegungsroutine des FlexiBowl® auf.
    :::{important}
    Se al momento del comando non risulta selezionato/abilitato alcun modello, il sistema restituisce un messaggio di errore e il Locator non viene avviato.
    :::
  - `Pattern_n;x;y;r` / `Hopper;signalnumber;time`
* - `stop_Locator`
  - Stoppt den Lokalisierungsprozess
  - Keine
* - `turn_Locator`
  - Wenn keine Teile aufgenommen wurden dreht der FlexiBowl® und startet die Suche neu
  - `Pattern_n;x;y;r`
* - `test_Locator`
  - Startet die Lokalisierung ohne Aktivierung des FlexiBowl® (nur Bildaufnahme)
  - `Pattern_n;x;y;r`/ Keine
* - `state_Locator`
  - Gibt den Diagnosestatus des Lokalisierers zurück
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```

:::{note}
Neben `;` stehen folgende weitere Trennzeichen zur Verfügung: `,`, `|`, `:`, `&`, `$`, `@`, `#`.
:::

### *FlexiBowl®-Befehle*

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Befehl
  - Aktion
  - Rückgabewert
* - `start_Empty`
  - Startet die Schnellentleerungssequenz (Quick-Emptying) des FlexiBowl®
  - `start_Empty ended`
```


### *Signale des optionalen Trichters*

```{note}
Wenn der Trichter aktiviert werden soll, erhalten wir die Zeichenfolge: `"Hopper;signalnumber;time"`

```



Ausführliche Informationen zur Installation und zum elektrischen Anschluss finden Sie in den folgenden Abschnitten:
- [Berechnung des optimalen Arbeitsabstands der Kamera](05_Calcolo_distanza_ottimale.md)
- [Mechanische Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- [Verkabelung und Anschlüsse](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

