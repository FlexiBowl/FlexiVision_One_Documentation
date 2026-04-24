(distanza_lavoro)=
# **Berechnung des optimalen Arbeitsabstands**

Dieser Abschnitt definiert den empfohlenen Arbeitsabstand (Working Distance) zwischen der Kamera und dem FlexiBowl-Teller sowie die daraus resultierende Auswahl der erforderlichen Objektive zur Gewährleistung des korrekten Sichtfelds (Field of View, FOV).

Die korrekte Wahl von Arbeitsabstand und Objektiv ist wesentlich, um:
- Sicherzustellen, dass die gesamte nutzbare Oberfläche des FlexiBowl sichtbar ist
- Die erforderliche Auflösung zur Erkennung der Teile zu erhalten
- Optische Verzerrungen zu minimieren
- Die Kalibrierung des Systems zu erleichtern

---

## Empfohlene Arbeitsabstände und Objektivauswahl

Die Wahl des Objektivs hängt eng vom empfohlenen Montageabstand zwischen Kamera und Oberfläche des FlexiBowl-Tellers ab. Die Einhaltung des Standard-Arbeitsabstands gewährleistet das korrekte FOV und minimiert Probleme durch optische Verzerrung.


```{note}
**Objektiv bereits enthalten**

Das für das in der Bestellung angegebene FlexiBowl-Modell geeignete Objektiv ist immer im FlexiVision One Paket enthalten und wird in einer von der Kamera getrennten Verpackung geliefert. Es muss nicht separat erworben werden.
```

### Schema der Abstände und des Sichtfelds

Das folgende Diagramm zeigt die Beziehung zwischen Arbeitsabstand, Brennweite des Objektivs und resultierendem Sichtbereich für die verschiedenen FlexiBowl-Modelle.

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Arbeitsabstand
:width: 40%
:align: center
```

**Legende zum Schema:**
- **Arbeitsabstand**: Vertikaler Abstand zwischen der Frontfläche des Objektivs und der Oberfläche des FlexiBowl-Tellers
- **Sichtbereich**: Bereich der FlexiBowl-Oberfläche, der vom Sichtfeld der Kamera abgedeckt wird

### Übersichtstabelle nach Modell

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - FlexiBowl-Modell
  - Empfohlener Arbeitsabstand (Working Distance)
  - Im Kit enthaltenes Objektiv (Brennweite)
* - **FB 200**
  - 800 mm 
  - 35 mm
* - **FB 350**
  - 1000 mm
  - 35 mm
* - **FB 500**
  - 1000 mm
  - 25 mm
* - **FB 650**
  - 1000 mm
  - 16 mm
* - **FB 800**
  - 1000 mm
  - 16 mm
* - **FB 1200**
  - 1300 mm
  - 12 mm
```

```{warning}
**Bedeutung des korrekten Abstands**

Erhebliche Abweichungen vom empfohlenen Arbeitsabstand können Folgendes verursachen:

- **Abstand zu kurz**: Unzureichendes FOV (ein Teil des FlexiBowl ist nicht sichtbar).
- **Abstand zu lang**: Unzureichende Auflösung zur Erkennung kleiner Teile, Unschärfe

Die in der Tabelle angegebenen Abstände bei der mechanischen Montage der Kamera stets einhalten.
```
### Kamerapositionierung 

**Korrekte Konfiguration.** Die Kamera muss zentral und mit derselben Winkelausrichtung zur Sichtfläche des FlexiBowl (Backlight-Zone) positioniert werden. Auf diese Weise deckt das Sichtfeld (grün dargestellt) den gesamten Arbeitsbereich symmetrisch ab und gewährleistet den korrekten Betrieb des Bildverarbeitungssystems.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Arbeitsabstand
:width: 70%
:align: center
```

**Fehlerhafte Konfigurationen.** Die Bilder zeigen Beispiele einer nicht korrekten Kamerapositionierung: Das Sichtfeld (rot dargestellt) ist gegenüber dem Sichtbereich versetzt, deckt den Arbeitsbereich nur teilweise ab oder schließt Bereiche außerhalb davon ein. Diese Konfigurationen beeinträchtigen die Teileerkennung und den Betrieb des Bildverarbeitungssystems.  

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Arbeitsabstand
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Arbeitsabstand
:width: 60%
:align: center
```
---

## TopLight-Positionierung 

Wenn das System ein TopLight (Beleuchtung von oben) enthält, muss dessen Positionierung dieselbe Winkelausrichtung wie die Kamera haben, um eine gleichmäßige Beleuchtung zu gewährleisten. Es muss auf einer mechanisch vom Kamerahalter unabhängigen Halterung installiert werden, sodass zum Entfernen oder Austauschen des Beleuchtungssystems die Kamera nicht gelöst oder demontiert werden muss.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Empfohlener Wert
* - **Abstand von der FlexiBowl-Oberfläche**
  - Ähnlich der Working Distance der Kamera (±100 mm)
* - **Position zur Kamera**
  - Konzentrisch (gleiche optische Achse wie die Kamera)
* - **Ausrichtung**
  - Parallel zur FlexiBowl-Oberfläche und mit derselben Winkelausrichtung der Kamera (lange Seite des Sichtbereichs - lange Seite der Beleuchtung)
* - **Relative Höhe Kamera-TopLight**
  - Sichtoptik bündig mit der oberen Oberfläche des Top Light (freien Zugang zu den Einstellringen der Sichtoptik lassen)
    :::{figure} ../../../../_shared/media/images/posizione_cam_TPL_B.png
    :alt: Arbeitsabstand
    :width: 80%
    :align: center
    :::
```

```{tip}
Um die beste Gleichmäßigkeit der Beleuchtung zu erzielen, die soeben aufgeführten Hinweise befolgen 
```

```{warning}
**Direkte Reflexionen vermeiden**

Beim Positionieren des TopLight sicherstellen, dass:

- Das Licht nicht direkt von der Oberfläche des FlexiBowl zur Kamera reflektiert wird (Blendung)
- Keine Schatten durch mechanische Komponenten entstehen
- Die Beleuchtung über die gesamte nutzbare Oberfläche möglichst gleichmäßig ist

```

---

## Zugehörige Referenzen

Zur Vervollständigung der Installation und Konfiguration des Systems:

- **Mechanische Installation der Kamera**: [Mechanische Installation](../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md)
- **Technische Spezifikationen der Kamera**: [Spezifikationen FlexiVision One](04_Specifiche_FlexiVision.md)
- **Systemkalibrierung**: [Kamerakalibrierung](../QUICKSTART/SETUP/14_calibrazione_camera.md)
- **Elektrische Verkabelung**: [Verkabelung und Anschlüsse](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md)

