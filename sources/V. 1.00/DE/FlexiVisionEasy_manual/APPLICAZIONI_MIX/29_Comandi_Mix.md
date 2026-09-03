# **Steuerungen Mix-Anwendung**
```{note}
**Voraussetzungen**

Bevor Sie mit diesem Abschnitt fortfahren, vergewissern Sie sich, dass Sie die Funktionsweise der Mix-Anwendung verstanden und das Rezept mit den Vorlagen der verschiedenen Komponenten korrekt konfiguriert haben. Siehe [Überblick über die Mix-Anwendung](28_Panoramica_Mix.md).
```

---

## Unterschiede auf der Roboterseite

In einer Mix-Anwendung unterscheiden sich die vom Roboter an das Bildverarbeitungssystem gesendeten TCP/IP-Befehle von denen einer Standard-Anwendung.

Der Hauptunterschied betrifft die **Befehlsfamilie zur Lokalisierung**: Die Befehle, die in der Standardanwendung das Präfix `start_` haben, werden durch die entsprechende Familie mit dem Präfix `mix_` ersetzt.

Diese Änderung ermöglicht es dem Bildverarbeitungssystem, die **Mehrkomponenten**-Erkennungslogik zu aktivieren und dem Roboter nicht nur die Koordinaten des lokalisierten Teils, sondern auch die **Kennung des erkannten Modells** zurückzugeben, sodass das Roboterprogramm für jeden Teiltyp die richtige Entnahmestrategie auswählen kann.
```{important}
Der Rückgabewert der Mix-Befehle enthält immer die Kennung des erkannten Musters (`Pattern_n`). Das Roboterprogramm muss so ausgelegt sein, dass es die verschiedenen Antworttypen verarbeiten und je nach identifiziertem Modell die entsprechende Entnahmestrategie anwenden kann.
```

---

## Im Mix-Modus verfügbare Befehle

### *Rezeptverwaltung*

| Befehl | Aktion | Rückgabewert |
|---|---|---|
| `set_Recipe=nome_ricetta` | Lädt das angegebene Mix-Rezept | Keine |
| `get_Recipe` | Gibt den Namen des aktuell geladenen Rezepts zurück | `nome_ricetta` |
```{note}
Die Befehle zur Rezeptverwaltung sind im Standard- und im Mix-Modus identisch.
```

### *Befehle zur Mix-Lokalisierung*

Die Befehle zur Mix-Lokalisierung ermöglichen es dem Roboter, die Koordinaten eines bestimmten Modells innerhalb des Rezepts abzufragen. Jeder Befehl ist einem einzelnen Modell zugeordnet und verwaltet den Suchzyklus eigenständig, einschließlich der Bewegung des FlexiBowl® und der Aktivierung des Trichters, falls erforderlich.

Das Verhalten von `mix_Locator_n` ist wie folgt:

1. Das System nimmt ein Bild auf und sucht nach dem Modell `n`.
2. Wird das Modell bei der ersten Aufnahme nicht gefunden, wird der FlexiBowl® automatisch betätigt und die Suche fortgesetzt.
3. Der Zyklus wird fortgesetzt, bis das Modell `n` lokalisiert wurde oder der Befehl `stop_Locator` gesendet wird.
4. Während der gesamten Suchphase wird der Trichter bei Bedarf automatisch aktiviert.
```{important}
Jeder Befehl `mix_Locator_n` sucht **ausschließlich** nach dem Modell, das der Nummer `n` entspricht.   
Das bedeutet, dass zur Abfrage der Koordinaten eines anderen Modells der für dieses Modell spezifische Befehl verwendet werden muss (z. B. `mix_Locator_2` für Modell 2, `mix_Locator_3` für Modell 3 usw.).
```

| Befehl | Aktion | Rückgabewert |
|---|---|---|
| `mix_Locator_1` | Startet die Suche nach **Modell 1**. Wird es nicht gefunden, wird der FlexiBowl® aktiviert und die Suche automatisch wiederholt, bis das Modell gefunden wird oder `stop_Locator`. Aktiviert den Trichter, falls erforderlich. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | Wie oben, für **Modell 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | Wie oben, für **Modell 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | Wie oben, für **Modell 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | Wenn kein Teil entnommen wurde, wird der FlexiBowl® gedreht und die Mehrkomponentensuche neu gestartet | `Pattern_n;x;y;r` |
| `test_Locator` | Startet die Mehrkomponentensuche, ohne den FlexiBowl® zu aktivieren (nur Bildaufnahme) | `Pattern_n;x;y;r` / Keine |
| `stop_Locator` | Bricht jede laufende Suche ab | Keine |
| `state_Locator` | Gibt den Diagnosestatus des Lokalisierers zurück | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
Die maximale Anzahl der Modelle, die innerhalb eines einzelnen Mix-Rezepts verwaltet werden können, beträgt **8**, entsprechend den Befehlen `mix_Locator_1` … `mix_Locator_8`. Das Roboterprogramm kann die Modelle je nach Anwendungslogik in beliebiger Reihenfolge und Kombination anfordern.
```

### *FlexiBowl®-Befehle*

| Befehl | Aktion | Rückgabewert |
|---|---|---|
| `start_Empty` | Startet die Schnellentleerungssequenz des FlexiBowl® | `start_Empty ended` |

### *Signale für optionalen Trichter*
```{note}
Wenn der Trichter aktiviert werden soll, erhalten wir die Zeichenfolge: `"Hopper;signalnumber;time"`
```

---

## Format des Rückgabewerts

Im Mix-Modus hat der Rückgabewert der Lokalisierungsbefehle das folgende Format:
```
Pattern_n;x;y;r
```

| Feld | Beschreibung |
|---|---|
| `Pattern_n` | Kennung des erkannten Modells (z. B. `Pattern_1`, `Pattern_2`, ...). Entspricht der Nummer des mit dem Befehl `mix_Locator_n` angeforderten Modells. |
| `x` | X-Koordinate des Werkstücks im Arbeitsbereich (in mm, im Referenzsystem des Roboters) |
| `y` | Y-Koordinate des Werkstücks im Arbeitsbereich (in mm, im Referenzsystem des Roboters) |
| `r` | Drehwinkel des Werkstücks (in Grad) |
```{tip}
Das Feld `Pattern_n` ist der Schlüsselparameter für Mix-Anwendungen: Das Roboterprogramm muss es verwenden, um die richtige Entnahmeroutine (Anfahrposition, Greiferöffnung, Greifkraft usw.) entsprechend dem identifizierten Werkstücktyp auszuwählen.
```

---


Informationen zum Kommunikationsprotokoll und zu den TCP/IP-Verbindungsparametern finden Sie unter:

**→ [Kommunikationsprotokoll zwischen Roboter und Bildverarbeitungssystem](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**