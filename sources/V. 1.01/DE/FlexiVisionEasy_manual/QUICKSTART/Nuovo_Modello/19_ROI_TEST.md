(roitest)=  
# **Definition von ROI und Toleranzen**

In diesem Abschnitt werden die Suchregion (Region Search) und die Erkennungstoleranzen für das erstellte Modell festgelegt. Diese Parameter bestimmen, wo und mit welcher Genauigkeit FlexiVision One während des Betriebs nach den Teilen sucht.

**Was ist die Region Search?**
Die **Region Search** ist der Bereich, in dem FlexiVision One die zu entnehmenden Komponenten sucht und erkennt.

# Verfahren

Nachdem Sie auf der Trainingsseite auf Weiter" geklickt haben, öffnet sich automatisch die Seite **„Define Robot Picking Limit Area Model“.**



## Schritt 1: Bereichsdefinition

:::{video} ../../../../../_shared/media/videos/TastoInfo_DefineRobotArea_1280x720.mp4
    :width: 100%
    :align: center
:::
```{list-table}
* - **1**
  - Bearbeiten Sie auf der Seite „**Define Robot Picking Limit Area Model**“ **definieren**das Feld, um den Suchbereich abzugrenzen
* - **2**
  - Sobald die Größe des Suchbereichs korrekt eingestellt ist, klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
* - **3**
  - Es öffnet sich die Seite „**Locator Model 1 Cam 1**“
```
```{tip}
Abmessungeneren Sie den Bereich entsprechend dem tatsächlichen Arbeitsraum des Roboters und vermeiden Sie Bereiche, die nicht erreichbar sind.
```
:::{tip}
Bei Fragen während der Konfiguration klicken Sie bitte auf die Schaltfläche „**INFO**“ auf der aktuellen Seite.
:::

### *Übersicht über die Benutzeroberfläche von „Locator Model“*

![Seite Locator Modell](../../../../../_shared/media/images/pagina_locatormodel.png)
```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Beschreibung
* - **Test**
  - Führt einen Echtzeit-Erkennungstest mit den aktuellen Parametern durch
* - **Accept Threshold**
  - Mindestschwelle für die Wiedergabetreue (Score), die ein Teil haben muss, um akzeptiert zu werden
* - **Results Panel**
  - TFenster, das alle erkannten Teile mit Details (ID, Koordinaten, Score) anzeigt
```
### Video-Tutorial
Erklärendes Video-Tutorial zu den folgenden Schritten 2 und 3:
:::{video} ../../../../../_shared/media/videos/TastiInfo_LocatorModel_1280x720.mp4
    :width: 100%
    :align: center
:::




## Schritt 2: Vorbereitung der Szene
```{list-table}
:widths: 5 95

* - **4**
  - Platzieren Sie **weitere Teile** zufällig im Sichtbereich um das Referenzteil herum, ohne dass sie mit diesem verwechselt werden.
    
    :::{warning}
    Das für das Training verwendete Referenzteil darf nicht berührt werden! Und verlieren Sie sie nicht aus den Augen!
    :::
```

## Schritt 3: Testdurchführung und Accept Threshold
```{list-table}
:widths: 5 95

* - **5**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon"> , um die Erkennung durchzuführen

* - **6**
  - Beobachten Sie, wie viele Teile erkannt werden und mit welchen Werten

* - **7**
  - Passen Sie den **Accept Threshold** an die Anforderungen der Anwendung an
    
    :::{note}
    **Was ist der Accept Threshold?**
    
    Es handelt sich um den **Mindestwert für die Übereinstimmung** (Score), den eine erkannte Komponente im Vergleich zum Referenzmodell aufweisen muss, um akzeptiert zu werden.
    
    - **Wert 0,95** → Akzeptiert nur Komponenten mit einer Übereinstimmung von ≥ 95 %
    - **Wert 0,80** → Akzeptiert nur Komponenten mit einer Übereinstimmung von ≥ 80 %
    - **Höherer Wert** → Strenger (weniger Fehlalarme)
    - **Niedrigster Wert** → Toleranter (erkennt auch Komponenten, die dem Referenzmodell weniger ähnlich sind)
    :::
```
```{tip}

**Empfohlener iterativer Ansatz:**

1. Beginnen Sie mit Accept Threshold = 0.85
2. Führen Sie einen Test durch und beobachten Sie die Ergebnisse
3. Wenn **zu viele Teile akzeptiert** werden (einschließlich Fehlalarme) → Erhöhen Sie den Schwellenwert (z. B.: 0.90)
4. Wenn **zu wenige Teile erkannt** werden (gute Teile werden aussortiert) → Verringern Sie den Schwellenwert verringern (z. B. 0.80)
5. Wiederholen Sie den Vorgang, bis Sie den optimalen Wert für die Anwendung gefunden haben

**Ziel**: Den höchstmöglichen Wert finden, der alle guten Teile erkennt, aber die schlechtesten aussortiert.
```
:::{tip}
Bei Fragen während der Konfiguration klicken Sie bitte auf die Schaltfläche „**INFO**“ auf der aktuellen Seite.
:::

---

## Interpretation der Ergebnisse

### *Anzeige der erkannten Komponenten*

Im Bereich „Results“ werden alle erkannten Komponenten angezeigt, die den Accept Threshold erfüllen:
```{list-table}
:header-rows: 1
:widths: 15 25 60

* - Feld
  - Typ
  - Beschreibung
* - **Id**
  - Ganzzahl
  - Eindeutige fortlaufende Kennung (0, 1, 2, ...)
* - **X**
  - Millimeter
  - X-Koordinate des Teils (Bezug zum Ursprung des Kalibrierungsgitters)
* - **Y**
  - Millimeter
  - Y-Koordinate des Teils (Bezug zum Ursprung des Kalibrierungsgitters)
* - **Drehung**
  - Grad
  - Drehwinkel des Teils (0-360°)
* - **Score**
  - Prozentsatz
  - Übereinstimmungsgrad mit dem Referenzmodell (0.00-1.00) Prioritätssystem
```
```{admonition} Sistema di Priorità
:class: info
FlexiVision One sortiert standardmäßig alle erkannten Teile automatisch nach **absteigendem Score**:
- **Id 0** → Teil mit dem höchsten Score (am ähnlichsten zum Referenzmodell)
- **Id 1** → Zweitbestes Teil
- **Id 2** → Drittbestes Teil
- Und so weiter...
```
### *Beispiel für die Interpretation*

Angenommen, nach dem Test erscheinen folgende Ergebnisse:

| Id| X| Y| Drehung| Score
|----|-------|-------|----------|-------|
| 0 | 125.4 | -45.2 | 15.3° | 0.92 |
| 1 | -80.1 | 32.5 | 178.5° | 0.89 |
| 2 | 45.7 | 110.3 | 92.1° | 0.86 |
| 3 | -150.2 | -95.7 | 45.8° | 0.83 |

**Auswertung:**
- **Id 0**: Die beste Übereinstimmung (92%) wird zuerst entnommen
- **Id 1:** Gute Übereinstimmung (89%), zweite Option
- **Id 2**: Befriedigende Übereinstimmung (86%), dritte Option
- **Id 3:** Akzeptable Übereinstimmung (83%), vierte Option

Wenn der Wert für „Accept Threshold“ 0,85 wäre:
- Id 0, 1, 2 würden akzeptiert
- Id 3 würde verworfen werden (Score 0,83 < 0,85)

---

# Abschluss

## Schritt 4: Reinigung und Fortsetzung
```{list-table}
* - **8**
  - Entfernen Sie **alle Teile** aus dem Bereich, a**ußer dem Referenzteil** und den beiden Objekten an dessen Seiten
    :::{danger}
      **Verschieben Sie das Referenzteil nicht!**
      Achten Sie auch beim Bereinigen der Szene darauf, das Referenzteil nicht zu berühren oder zu verschieben. Seine Koordinaten werden in der letzten Phase noch für die Roboterkalibrierung benötigt.
    :::
* - **9**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> → die Seite „**Clearances**“ wird geöffnet
```
```{seealso}
Fahren Sie mit der [Konfiguration der Clearances](istogrammi) fort, um die Freiräume zu definieren.
```

