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
### *So verwenden Sie die Befehle Start und Mix richtig*

FlexiVision One unterstützt zwei unterschiedliche Anwendungsmodi, je nachdem, ob auf dem FlexiBowl® nur ein Komponententyp oder mehrere verschiedene Komponenten gleichzeitig geladen sind. Welcher Befehl zu verwenden ist, hängt von der Konfiguration der Anwendung ab: `start_Locator` und `mix_Locator_<Modelle>` **dürfen innerhalb desselben Rezepts niemals austauschbar verwendet werden**.

**Standardanwendung – eine einzelne Komponente**

In einer Standardanwendung ist auf dem FlexiBowl® nur ein Komponententyp geladen. Die verschiedenen Modelle dienen dazu, die unterschiedlichen Greifseiten derselben Komponente zu erkennen, zum Beispiel:

- Modell 1 = Komponente, Greifseite 1
- Modell 2 = dasselbe Komponente, Greifseite 2
- Modell 3 = dasselbe Komponente, Greifseite 3

In dieser Konfiguration wird ausschließlich `start_Locator` verwendet: Der Befehl startet automatisch die sequenzielle Suche über alle erstellten Modelle (zuerst Modell 1, dann Modell 2, Modell 3 usw.). Wird keine gültige Instanz gefunden, dreht sich der FlexiBowl® und der Suchzyklus beginnt von neuem.

```{important}
In einer Standardanwendung **dürfen niemals Mix-Befehle gesendet werden** (`mix_Locator_<Modelle>`). Die Suche über die verschiedenen Seiten derselben Komponente wird bereits automatisch von `start_Locator` übernommen.
```

**Mix-Anwendung – verschiedene Komponenten**

In einer Mix-Anwendung sind mehrere verschiedene Komponenten gleichzeitig auf dem FlexiBowl® geladen. Jedes Modell ist einer bestimmten Komponente und/oder einer ihrer Greifseiten zugeordnet, zum Beispiel:

- Modell 1 = Komponente 1
- Modell 2 = Komponente 2

Die entsprechenden Befehle lauten:

- `mix_Locator_1` → sucht nur Komponente 1 (Modell 1)
- `mix_Locator_2` → sucht nur Komponente 2 (Modell 2)

Im Gegensatz zu `start_Locator` sucht ein Mix-Befehl **ausschließlich** die Modelle, die in der Befehlsnummer angegeben sind. Um mehrere Modelle gleichzeitig zu suchen – seien es verschiedene Seiten derselben Komponente oder unterschiedliche Komponenten –, genügt es, die jeweiligen Nummern aneinanderzureihen, zum Beispiel:

- Modell 1 = Komponente 1, Greifseite 1
- Modell 2 = Komponente 1, Greifseite 2
- Modell 3 = Komponente 2, Greifseite 1
- Modell 4 = Komponente 2, Greifseite 2

In diesem Fall gilt:

- `mix_Locator_12` → sucht gleichzeitig die Modelle 1 und 2 (beide Seiten von Komponente 1)
- `mix_Locator_34` → sucht gleichzeitig die Modelle 3 und 4 (beide Seiten von Komponente 2)

Jeder Mix-Befehl sucht somit nur und ausschließlich die diesem Befehl zugeordneten Modelle, ohne die Suche auf die übrigen Modelle im Rezept auszudehnen.

**Zusammenfassung**

| Anwendungskonfiguration | Zu verwendender Befehl |
| --- | --- |
| Eine einzelne Komponente, mit einer oder mehreren Greifseiten | `start_Locator` |
| Mehrere verschiedene Komponenten gemeinsam geladen | `mix_Locator_<Modelle>` |

```{note}
Die beiden Befehle sind nicht austauschbar: `mix_Locator_12` verhält sich **nicht** wie `start_Locator` und führt keine automatische sequenzielle Suche über alle Modelle durch – es sucht nur die Modelle 1 und 2.
```

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
