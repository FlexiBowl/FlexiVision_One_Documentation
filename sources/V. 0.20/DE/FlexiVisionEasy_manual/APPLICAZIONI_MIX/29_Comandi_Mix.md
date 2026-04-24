# **Befehle der Mix-Anwendung**
```{note}
**Voraussetzungen**

Bevor Sie mit diesem Abschnitt fortfahren, stellen Sie sicher, dass Sie die Funktionsweise der Mix-Anwendung verstanden und die Rezeptur mit den Modellen der verschiedenen Komponenten korrekt konfiguriert haben. Siehe [Übersicht Mix-Anwendung](28_Panoramica_Mix.md).
```

---

## Unterschiede auf Roboterseite

In einer Mix-Anwendung ändern sich die TCP/IP-Befehle, die vom Roboter an das Bildverarbeitungssystem gesendet werden, gegenüber denen einer Standardanwendung.

Der Hauptunterschied betrifft die **Familie der Lokalisierungsbefehle**: Die Befehle, die in der Standardanwendung das Präfix `start_` haben, werden durch die äquivalente Familie mit dem Präfix `mix_` ersetzt.

Diese Änderung ermöglicht es dem Bildverarbeitungssystem, die **Mehrkomponenten**-Erkennungslogik zu aktivieren und dem Roboter nicht nur die Koordinaten des lokalisierten Teils zurückzugeben, sondern auch die **Kennung des erkannten Modells**, sodass das Roboterprogramm die korrekte Entnahmestrategie für jeden Teiletyp auswählen kann.
```{important}
Der Rückgabewert der Mix-Befehle enthält immer die Kennung des erkannten Patterns (`Pattern_n`). Das Roboterprogramm muss darauf vorbereitet sein, die verschiedenen Antworttypen zu verarbeiten und die geeignete Entnahmelogik anhand des identifizierten Modells anzuwenden.
```

---

## Im Mix-Modus verfügbare Befehle

### Rezeptverwaltung

| Befehl | Aktion | Rückgabewert |
|---|---|---|
| `set_Recipe=nome_ricetta` | Lädt die angegebene Mix-Rezeptur | Keiner |
| `get_Recipe` | Gibt den Namen der aktuell geladenen Rezeptur zurück | `nome_ricetta` |
```{note}
Die Befehle zur Rezeptverwaltung sind im Standard- und Mix-Modus identisch.
```

### Mix-Lokalisierungsbefehle

Die Mix-Lokalisierungsbefehle ermöglichen es dem Roboter, die Koordinaten eines bestimmten Modells innerhalb der Rezeptur anzufordern. Jeder Befehl ist einem einzelnen Modell gewidmet und verwaltet den Suchzyklus eigenständig, einschließlich der Bewegung des FlexiBowl® und der Aktivierung des Hoppers, falls erforderlich.

Das Verhalten von `mix_Locator_n` ist wie folgt:

1. Das System nimmt ein Bild auf und sucht nach Modell `n`.
2. Wenn das Modell bei der ersten Aufnahme nicht gefunden wird, wird der FlexiBowl® automatisch betätigt und die Suche wird fortgesetzt.
3. Der Zyklus läuft weiter, bis Modell `n` lokalisiert wird oder der Befehl `stop_Locator` gesendet wird.
4. Während der gesamten Suchphase wird der Hopper bei Bedarf automatisch aktiviert.
```{important}
Jeder Befehl `mix_Locator_n` sucht **ausschließlich** nach dem Modell, das der Nummer `n` entspricht.   
Das bedeutet, dass für die Anforderung der Koordinaten eines anderen Modells der spezifische Befehl für dieses Modell verwendet werden muss (z. B. `mix_Locator_2` für Modell 2, `mix_Locator_3` für Modell 3 usw.).
```

| Befehl | Aktion | Rückgabewert |
|---|---|---|
| `mix_Locator_1` | Startet die Suche nach **Modell 1**. Wenn es nicht gefunden wird, betätigt er den FlexiBowl® und wiederholt die Suche automatisch bis zum Auffinden oder bis `stop_Locator`. Aktiviert den Hopper bei Bedarf. | `Pattern_1;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_2` | Wie oben, für **Modell 2** | `Pattern_2;x;y;r` / `Hopper;signalnumber;time` |
| `mix_Locator_3` | Wie oben, für **Modell 3** | `Pattern_3;x;y;r` / `Hopper;signalnumber;time` |
| … | … | … |
| `mix_Locator_8` | Wie oben, für **Modell 8** | `Pattern_8;x;y;r` / `Hopper;signalnumber;time` |
| `turn_Locator` | Wenn kein Teil entnommen wurde, dreht er den FlexiBowl® und startet die Mehrkomponenten-Suche erneut | `Pattern_n;x;y;r` |
| `test_Locator` | Startet die Mehrkomponenten-Lokalisierung ohne Aktivierung des FlexiBowl® (nur Bildaufnahme) | `Pattern_n;x;y;r` / Keiner |
| `stop_Locator` | Unterbricht jede laufende Suche | Keiner |
| `state_Locator` | Gibt den Diagnosestatus des Locators zurück | `Locator is Running` / `Locator is in Error` / `Locator is not Running` |

```{tip}
Die maximale Anzahl von Modellen, die innerhalb einer einzelnen Mix-Rezeptur verwaltet werden können, beträgt **8**, entsprechend den Befehlen `mix_Locator_1` … `mix_Locator_8`. Das Roboterprogramm kann die Modelle in beliebiger Reihenfolge und Kombination anfordern, abhängig von der Anwendungslogik.
```

### FlexiBowl®-Befehle

| Befehl | Aktion | Rückgabewert |
|---|---|---|
| `start_Empty` | Startet die Schnellleerungssequenz des FlexiBowl® | `start_Empty ended` |

### Optionale Hopper-Signale
```{note}
Wenn der Hopper aktiviert werden muss, erhalten wir die Zeichenkette: `"Hopper;signalnumber;time"`
```

---

## Format des Rückgabewerts

Im Mix-Modus hat der Rückgabewert der Lokalisierungsbefehle das folgende Format:
```
Pattern_n;x;y;r
```

| Feld | Beschreibung |
|---|---|
| `Pattern_n` | Kennung des erkannten Modells (z. B. `Pattern_1`, `Pattern_2`, …). Entspricht der Nummer des Modells, das mit dem Befehl `mix_Locator_n` angefordert wurde. |
| `x` | X-Koordinate des Teils im Arbeitsbereich (in mm, im Referenzsystem des Roboters) |
| `y` | Y-Koordinate des Teils im Arbeitsbereich (in mm, im Referenzsystem des Roboters) |
| `r` | Rotationswinkel des Teils (in Grad) |
```{tip}
Das Feld `Pattern_n` ist der Schlüsselparameter für Mix-Anwendungen: Das Roboterprogramm muss es verwenden, um die korrekte Entnahmeroutine (Anfahrposition, Greiferöffnung, Greifkraft usw.) basierend auf dem identifizierten Teiletyp auszuwählen.
```

---


Informationen zum Kommunikationsprotokoll und zu den TCP/IP-Verbindungsparametern finden Sie unter:

**→ [Kommunikationsprotokoll Roboter-Bildverarbeitung](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md)**
