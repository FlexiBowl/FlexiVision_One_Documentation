(protocol_setup)=
# **Protocol Setup**

Auf der Seite **Protocol Setup** können Sie die Parameter konfigurieren, die den Kommunikationsfluss und den Datenaustausch zwischen dem Bildverarbeitungssystem FlexiVision One und dem Roboter regeln. Diese Parameter legen fest, wie viele Objekte gesendet werden, in welcher Reihenfolge sie angeordnet sind und wie das System Statistiken und Betriebszustände verwaltet.

---

## Zugriff auf Protocol Setup

1. Rufen Sie im Hauptmenü den Bereich für das Kommunikationsprotokoll auf
2. Wählen Sie **Protocol Setup**
3. Die Benutzeroberfläche mit den konfigurierbaren Parametern wird geöffnet


---

## Konfigurierbare Parameter

![Seite Protocol Setup](../../../../../_shared/media/images/pagina_protocolsetup.png)

```{list-table}
:header-rows: 1
:widths: 35 65

* - **Parameter**
  - **Beschreibung und Funktion**
* - [**Max Object Count Return**](maxobject)
  - Gibt die **maximale** Anzahl von Objekten (d. h. ihre Dreiergruppe von Koordinaten) an, die das Bildverarbeitungssystem in einem einzelnen Durchlauf an den Roboter zurücksenden kann. Wenn das Bildverarbeitungssystem mehr Objekte als diesen Grenzwert erkennt, werden maximal diese Anzahl an Objekten gesendet, die nach dem konfigurierten Sortierkriterium (Sorting Mode) ausgewählt werden.
* - [**Min Object Count Return**](minobject)
  - Gibt die **Mindestanzahl** an Objekten an, die in einem Durchlauf zurückgegeben werden müssen, damit das Ergebnis als gültig angesehen wird. Liegt die Zahl unter diesem Schwellenwert, wird der Durchlauf als ungültig betrachtet.
* - [**Sorting Mode Results**](sortingmode)
  - Legt das **Sortierkriterium** fest, nach dem die Liste der vom Bildverarbeitungssystem zurückgegebenen Objekte sortiert wird. Dieser Parameter bestimmt die Entnahmereihenfolge und legt fest, welche Objekte in die Max Object Count Return einbezogen werden.
    
    *Typische Option:* nach absteigendem Score.
* - [**Pickable parts by the robot detected by vision in each cycle**](pickableparts)
  - Gibt die Anzahl der Greifvorgänge an, die der Roboter pro Lauf des Vision-Systems ausführt. Beispielsweise entspricht ein Doppelgreifvorgang dem Wert 2. Dies stellt nicht die Anzahl der vom Vision-System erkannten Objekte dar, sondern die Anzahl der Roboter-Greifvorgänge pro Zyklus. Parameter für die Berechnung der Statistiken.

* - **Maximum processing time per part with the robot (in seconds)**
  - Definiert die maximale Zeit, nach der das System die Verarbeitung/Übermittlung der Koordinaten für einen Durchlauf als abgeschlossen betrachtet und typischerweise vom Status RUN in den Status IDLE wechselt. Parameter für die **Statistiken und Workflow-Management**.

    :::{attention}
    **Es handelt sich nicht um ein Zeitlimit für einen Roboterfehler**, sondern um einen Zeitbezugspunkt für die Zyklusberechnung und für Produktivitätskennzahlen.
    :::
```

---

## Detaillierte Konfiguration der Parameter

(maxobject)=
### *Max Object Count Return*

```{list-table}
 :class: align-top

* - **Funktion**: 
  - Begrenzt die maximale Anzahl von Koordinaten, die pro Bildverarbeitungszyklus an den Roboter gesendet werden.

* - **Typische Werte:**
  - 
    - **1** : Gängigste Konfiguration für Roboter mit Einzelentnahme
    - **2** : Konfiguration für Roboter mit Doppelentnahme
    - **3** : Konfiguration für Roboter mit Dreifachentnahme
    - **4-8 Objekte**: Für Systeme mit kreisförmiger Verfolgung
    - **>8 Objekte**: Selten erforderlich, kann die Kommunikation überlasten

    :::{tip}
    **So wählen Sie den Wert aus:**
    1. Berücksichtigen Sie die Geschwindigkeit des Roboters (Pick&Place-Zeit pro Teil)
    2. Berücksichtigen Sie die Zykluszeit für Bildverarbeitung + FlexiBowl®
    3. Näherungsformel: `Max Count = (Tempo ciclo visione+FB) / (Tempo pick robot)`

    **Praktisches Beispiel:**
    - Cycle Vision+FlexiBowl®: 3 Sekunden
    - Roboter-Picking-Zeit: 2 Sekunden/Teil
    - Optimale Max Count: 3/2 = 1,5 → Auf 2 Objekte aufrunden
    :::
```

(minobject)=
### *Min Object Count Return*

```{list-table}
* - **Funktion**: 
  - Begrenzt die Mindestanzahl an Koordinaten, die pro Bildverarbeitungszyklus an den Roboter gesendet werden.

* - **Typische Werte:**
  - 
    - **1**: Häufigste Konfiguration - auch nur ein erkanntetes Teil ist akzeptabel
    - **>2**: Nur für spezielle Anwendungen mit obligatorischer Mehrfachentnahme

* - **Systemverhalten:**
  - 
    - **Erfasste Objekte ≥ Min Count**: Koordinate(n) werden an den Roboter gesendet
    - **Erfasste Objekte < Min Count**: Koordinate(n) werden nicht gesendet und die FlexiBowl®-Sequenz wird ausgeführt


* - **Auswirkungen auf die Produktivität**
  - 
    **Min Count = 1** (weniger restriktiv):
    - ✓ Maximale Flexibilität, Roboter arbeitet auch, wenn nur ein Teil vorhanden ist
    - ✗ Zyklen mit geringer Effizienz möglich (1 Teil alle N Sekunden)

    **Min Count = 3** (restriktiver):
    - ✓ Garantiert ein Minimum an Effizienz pro Zyklus
    - ✗ Kann zu Wartezeiten führen, wenn die Befüllung variabel ist
```

(sortingmode)=
### *Sorting Mode Results*


```{list-table}
:header-rows: 1
:widths: 30 70

* - Sortiermodus
  - Beschreibung und Verwendung
* - **By Score (Descending)**
  - Sortieren nach Punktzahl von der höchsten zur niedrigsten. Objekte mit einer besseren Übereinstimmung mit dem Modell werden zuerst gesendet.
    **Am häufigsten verwendet und empfohlen:** Gewährleistet stets die Entnahme der Teile mit der zuverlässigsten Erkennung.
* - **By Score (Ascending)**
  - Sortierung nach Punktzahl von der niedrigsten zur höchsten. Objekte mit einer schlechteren Übereinstimmung mit dem Modell werden zuerst gesendet.
    **NICHT EMPFOHLEN**: Garantiert NICHT immer eine zuverlässigere Erkennung bei der Teileauswahl.
* - **By X Coordinate (Ascending)**
  - Sortiert nach aufsteigender X-Koordinate. Nützlich, wenn der Roboter eine sequentielle Entnahme entlang einer Achse bevorzugt.
* - **By X Coordinate (Descending)**
  - Sortiert nach absteigender X-Koordinate.
* - **By Y Coordinate (Ascending)**
  - Sortiert nach aufsteigender Y-Koordinate.
* - **By Y Coordinate (Descending)**
  - Sortiert nach absteigender Y-Koordinate.
* - **X Alternating**
  - Das System wählt abwechselnd das erste und das letzte auf der X-Achse erkannte Teil aus. Da die beiden ausgewählten Teile weit voneinander entfernt sind, verringert sich das Risiko, dass eine vorherige Entnahme die Teile in der Nähe verschoben hat, was eine sicherere und zuverlässigere Entnahme gewährleistet
* - **Y Alternating**
  - Das System wechselt bei der Auswahl des Teils zwischen dem ersten und dem letzten auf der Y-Achse erfassten Teil. Gleiches Prinzip wie bei X Alternating: Der Abstand zwischen den beiden Aufnahmepunkten minimiert Störungen durch versehentliche Verschiebungen benachbarter Teile.
```

```{tip}
**Auswahl des optimalen Sorting Mode**

**In den meisten Fällen empfohlen: By Score (Descending)**

**Vorteile**:
- Maximale Zuverlässigkeit: Der Roboter nimmt immer die am besten erkannten Teile auf
- Reduziert das Risiko einer falschen Entnahme
- Unabhängig von der physischen Position
```

```{note}
Der Sortiermodus steht in Wechselwirkung mit Max Object Count. Die ersten 15 Objekte (gemäß dem Kriterium) werden gesendet.
```
(pickableparts)=
### *Pickable parts by the robot*

**Funktion**

Statistischer Parameter, der angibt, wie viele Teile der Roboter pro Bildverarbeitungszyklus **tatsächlich aufnimmt**.

**Typische Werte**

- **1**: Roboter mit Einzelgreifer, nimmt jeweils 1 Teil auf
- **2**: Roboter mit Doppelgreifer oder Doppelsauger
- **>2**: Roboter mit Mehrfachgreifer oder Sauger

```{important}
Dieser Wert bezieht sich auf die **physisch aufgenommenen Teile**, nicht auf die vom Bildverarbeitungssystem erkannten Objekte.
```

**Erläuterndes Beispiel**

Szenario: Doppelgreifer, die Bildverarbeitung erkennt 5 Objekte.

- Wenn ich dem Roboter maximal 2 Objekte schicken möchte, stelle ich `Max Object Count = 2` ein.
- Wenn ich möchte, dass der Roboter mindestens 2 Objekte auf einmal aufnimmt, stelle ich `Min Object Count = 2` ein.
- In diesem Fall habe ich `Pickable Parts by the robot = 2` eingestellt.
- Möchte ich hingegen auch die Aufnahme eines einzelnen Objekts zulassen, stelle ich `Max Object Count = 2`, `Min Object Count = 1` und `Pickable Parts by the robot = 2` ein.

**Auswirkungen auf die Dashboard-Statistiken**

Dieser Parameter ist entscheidend für die genaue Berechnung der **Parts Per Minute (PPM)**.

- Formel: `PPM = (Pickable parts x 60) / Tempo ciclo totale in secondi`
- Bei falscher Einstellung entspricht die angezeigte PPM nicht der Realität



---

## Speichern der Konfiguration

```{warning}
**Speichern obligatorisch**

Nach der Konfiguration der Parameter im Protocol Setup:

1. Überprüfen Sie, ob alle Werte korrekt eingestellt sind  
2. Klicken Sie auf Recipes > Save Recipe
3. Die Parameter werden in der Systemkonfiguration gespeichert
```

---

## Nächste Schritte

Sobald das Protocol Setup abgeschlossen ist, ist das System vollständig für den Betrieb konfiguriert:

- [Rezept speichern](ricettabase)





