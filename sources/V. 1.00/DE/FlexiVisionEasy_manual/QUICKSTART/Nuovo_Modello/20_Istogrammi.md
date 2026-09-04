(istogrammi)=
# **Die Clearances** 
Auf dieser Seite erfahren Sie, wie Sie Clearances konfigurieren, um sicherzustellen, dass kritische Bereiche frei von Hindernissen sind.

 **Was ist ein Clearance?**  
Ein **Clearance** in FlexiVision One ist ein Werkzeug, das einen bestimmten Bildbereich überwacht, um sicherzustellen, dass dieser frei ist. Es wird beispielsweise verwendet, um zu überprüfen, ob der für den Greifer zum Ergreifen des Bauteils erforderliche Raum nicht von anderen Objekten belegt ist.
````{note} Funktionsprinzip.

Das Clearance analysiert die Graustufenveränderungen in einem definierten Bereich:
- 🟢 **Grün** → Freier Bereich (OK für die Aufnahme)
- 🔴 **Rot** → Belegter Bereich (Vorhandensein von Hindernissen)
````
:::{attention}
Die Verwendung der Clearances variiert je nach dem Teil, für das das Modell erstellt werden soll. Diese Beurteilung ist Aufgabe der Person, die für die Erstellung der Anwendung zuständig ist.
:::
--- 
(setupclearances)=
## Schritt 1: Physikalische Einrichtung

:::{danger} **Achtung!**
  Wir zeigen Ihnen das Verfahren mit dem Greifer-Tool, das unbedingt die Konfiguration von Clearances für die Modelle erfordert. Andere Werkzeuge für den Roboter benötigen möglicherweise keine Clearances, um ihren Platzbedarf zu simulieren.
:::
:::{video} ../../../../../_shared/media/videos/Step1.mp4
    :width: 100%
    :align: center
:::
````{list-table}
:widths: 5 95

* - **1**
  - Über das **Roboter-Pendant**:
    - Wählen Sie den **Rahmen** und das auf FlexiVision One kalibrierte **Werkzeug** aus
    - Bringen Sie die **letzte Achse** des Werkzeugs auf **Null-Drehung** (Rz = 0°)
* - **2**
  - Simulieren Sie einen Greifvorgang:
    - Öffnen Sie den Greifer
    - Bringen Sie das Roboterwerkzeug auf das Bauteil in Höhe der Oberfläche, als ob Sie es greifen wollten
* - **3**
  - Positionieren Sie **zwei Objekte** an den Seiten des Greifers, um nach dem Entfernen des Roboters die freien Bereiche zwischen dem Referenzteil und den beiden Objekten zu erhalten.
  Diese stellen die Ausmaßbereiche des Robotergreifers dar.
    
    :::{important}
    Platzieren Sie die Objekte etwas weiter auseinander als unbedingt nötig, um Fehler bei der Modellerstellung zu vermeiden. (Abstand 2–3 mm)
    :::
    
* - **4**
  - Koordinaten notieren:
  - Speichern Sie die Koordinaten der letzten Roboterachse:
    - **X** (X-Koordinate)
    - **Y** (Y-Koordinate)
    - **Rz** (Rotation um Z)
    
    :::{important}
    Notieren Sie diese Koordinaten! Sie sind für die Roboterkalibrierung unerlässlich.
    :::
* - **5**
  - Entfernen Sie den Roboter mit dem Pendant, **ohne etwas auf der Oberfläche zu verschieben**
````
:::{tip}
Bei Fragen während der Konfiguration klicken Sie bitte auf die Schaltfläche „**INFO**“ auf der aktuellen Seite.
:::
---

## Schritt 2: Aufruf der Seite „Clearance“
````{list-table}
:widths: 5 95

* - **6**
  - Auf der Seite „**Locator Model**“ öffnet sich nach dem Klicken auf „**Next**“ die Liste der verfügbaren Clearances (bis zu 8 pro Modell).
    
    :::{dropdown} **Seite „Clearances“**
    
      ![Seite „Clearances“](../../../../../_shared/media/images/pagina_clearances.png)
    
      | Element | Beschreibung |
      |----------|-------------|
      | **Clearance 1...8** | Verfügbare Slots zum Erstellen von bis zu 8 verschiedenen Clearances für dasselbe Modell |
      | **Test (global)** | Schaltfläche zum gleichzeitigen Testen aller aktivierten Clearances |
      | **Next** | Weiter zur nächsten Phase (Roboter-Pick) nach der Konfiguration der Clearances |
    :::
* - **7**
  - Klicken Sie auf „**Clearance 1**“, um die Seite zur Konfiguration des ersten Freiraums „Clearance 1“ zu öffnen
    
    :::{dropdown} **Seite Clearance 1**

      ![Seite Clearance 1](../../../../../_shared/media/images/pagina_clearance1.png)

      | Parameter | Funktion |
      |-----------|----------|
      | **Enable Clearance** | Aktiviert diesen Freiraum und macht ihn betriebsbereit |
      | **Expression Builder** | Werkzeug zur automatischen Konfiguration der Erkennungsschwellen |
      | **Mean and Standard Deviation** | Statistische Werte, die für den ausgewählten Bereich berechnet wurden (Mittelwert und Standardabweichung der Graustufen) |
      | **Test** | Sofortige Überprüfung der Funktion „Clearance“ |
      | **Result** | Visuelle Statusanzeige (Grün = OK, Rot = Triggered) |
    :::
````
---

## Schritt 3: Aktivierung und Positionierung des Bereichs

:::{video} ../../../../../_shared/media/videos/Step3.mp4
    :width: 100%
    :align: center
:::
````{list-table}
* - **8**
  - Klicken Sie auf „**Enable Clearance**“, um den Freiraum zu aktivieren
* - **9**
  - Verschieben Sie den Clearance-**Rahmen** in den Bereich, der frei bleiben muss
      - Typischerweise: Greiferbereich (ein Freiraum pro Greiferbereich)
      - Ränder um das Teil herum
      - Durchfahrtsbereiche des Roboters
    :::{important}
    Beachten Sie immer diese beiden wichtigen Aspekte:
    - Der ROI des Freiraums muss bei der Konfiguration vollständig frei sein (also frei von Objekten, Schatten, Artefakten)
    - Erstellen Sie den Freiraum immer etwas größer als unbedingt nötig, um Fehlalarme zu vermeiden.

    Die Nichtbeachtung dieser beiden Punkte kann zu Kollisionen des Roboters führen, was Schäden am FlexiBowl®, an Komponenten oder am Roboter selbst zur Folge haben kann.
    :::
````
:::{tip}
Bei Fragen während der Konfiguration klicken Sie bitte auf die Schaltfläche „**INFO**“ auf der aktuellen Seite.
:::
---

## Schritt 4: Automatische Konfiguration

:::{video} ../../../../../_shared/media/videos/Step4.mp4
    :width: 100%
    :align: center
:::
````{list-table}
* - **10**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> im Expression Builder
* - **11**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">
* - **12**
  - Prüfen Sie, ob das Kästchen **grün** wird
* - **13**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
````
````{warning}
**Was ist zu tun, wenn der Test fehlschlägt (rotes Kästchen)?**

Wenn das Kästchen nach AUTO rot wird:

**Mögliche Ursachen:**
- Es befindet sich tatsächlich etwas im Bereich (Teil, Schatten, Verschmutzung)
- Die Beleuchtung hat sich zwischen der AUTO- und der TEST-Konfiguration verändert
- Der ausgewählte Bereich umfasst Ränder des FlexiBowl® oder Artefakte

**Lösungen:**
1. Überprüfen Sie visuell, ob der Bereich vollständig frei ist
2. Wiederholen Sie AUTO unter stabilen Lichtverhältnissen
3. Wiederholen Sie TEST zur Überprüfung
````
:::{tip}
Sollten Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO-Taste** auf der aktuellen Seite.
:::
---

## Mehrere Clearances – Wann sie zu verwenden sind

Erstellen Sie mehrere Clearances, wenn:
- Das Roboterwerkzeug eine Greifzange ist: Für jeden der beiden Bereiche, die die Greifzange an den Seiten des Referenzbauteils einnimmt, ist ein Clearance erforderlich
- Es mehrere kritische Punkte zu überwachen gibt
- Der Greifbereich besondere Geometrien aufweist

### *Schritt 2-3: Wiederholung*
Wählen Sie eine neue Clearance aus der Clearance-Liste aus, z. B. „Clearance 2“, und wiederholen Sie die Schritte 2–3.
Wiederholen Sie den Vorgang für jede erforderliche Clearance (bis zu 8 pro Modell).

### *Schritt 4: Gesamttest*

Klicken Sie auf der Seite mit der Liste aller Clearances auf „**TEST**“, um alle Clearances gleichzeitig anzuzeigen

![Seite „Clearances“](../../../../../_shared/media/images/activatedclearances.png)
---

## Interpretation der Status

### *Status der Clearances*

````{list-table}
:header-rows: 1
:widths: 10 15 30 45

* - Farbe
  - Status
  - Bedeutung
  - Bild
* - 🟢 Grün
  - OK
  - Freier Bereich, Aufnahme möglich
  - ![](../../../../../_shared/media/images/greenclearances.png)
* - 🔴 Rot
  - Triggered
  - Bereich belegt, Aufnahme nicht möglich
  - ![](../../../../../_shared/media/images/redclearances.png)
````
:::{note}
In den Feldern „Clearances“ sind deren Abmessungen in mm angegeben.
:::

### *Was bedeutet „Triggered“?*

Eine Freigabe wird rot (triggered), wenn sie in ihrem Inneren Folgendes erkennt:
- Vorhandensein anderer Komponenten
- Erhebliche Schatten oder Spiegelungen
- Jedes Element, das den Bereich belegt

---

## Schritt 5: Abschluss
````{list-table}
* - **14**
  - Nachdem Sie alle erforderlichen Clearances konfiguriert haben, klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon">
* - **15**
  - Die Seite **Robot Model Pick Cam** wird geöffnet
````
````{seealso}
Führen Sie die [Roboter-Pick-Kalibrierung](robotpick) durch, um die Konfiguration abzuschließen.
````

