(dashboard)=
# **Anwendungsüberwachung: Dashboard**

Das **Dashboard** ist die Hauptschnittstelle für die Echtzeitüberwachung des FlexiVision One-Systems. Auf dieser Seite können Sie die Prozesseffizienz überprüfen, die Zykluszeiten analysieren, die Erkennung der Komponenten validieren und eventuelle Engpässe im System ermitteln.


---

## Übersicht über die Benutzeroberfläche

Die Benutzeroberfläche des Dashboards ist in vier Hauptbereiche unterteilt:
![Seite „Hooper Setup“](../../../../_shared/media/images/pagina_dashboard.png)
1. [**Betriebssteuerung**](controllooperativo): Befehle und Ausführungsstatus
2. [**Bildverarbeitung**](analisivisione): Anzeige der erfassten Teile und Details
3. [**Leistungsindikatoren**](indicatoriperformance): Konnektivität und Zykluszeiten
4. [**Grafische Analyse**](analisigrafica): Historische Diagramme zu Produktivität und Zeiten

---
(controllooperativo)=
## Betriebssteuerung - Befehle und Ausführungsstatus

```{list-table}
:header-rows: 1
:widths: 25 75

* - Element
  - Beschreibung und Funktion
* - **In Run**
  - Statusanzeige, die anzeigt, ob das System derzeit in Betrieb ist.  
    **Grün** 🟢: System aktiv und betriebsbereit.  
    **Rot** 🔴: System angehalten oder im Pausenmodus.
* - **In Run Time**
  - Zeigt die Gesamtbetriebszeit des Systems seit dem Start der Anwendung an. 
* - **FlexiBowl®-Auswahl**
  - Dropdown-Menü zur Auswahl des spezifischen FlexiBowl®, der überwacht werden soll. 
* - **Test Locator**
  - Nimmt ein Foto des Sichtbereichs auf und startet die Erkennung der vorhandenen Komponenten. 
```

```{tip}
**Test Locator**
Nützlich für:
- Um zu überprüfen, ob die Teile tatsächlich vom Bildverarbeitungssystem erkannt werden.
- Für den Fall, dass es zu einer Kollision zwischen Roboter und Bauteil kommt und die Zuverlässigkeit der Sicherheitsabstände überprüft werden soll
```

---
(analisivisione)=
## Bildanalyse

In der Mitte des Dashboards werden die Daten zu den vom Bildverarbeitungssystem identifizierten Komponenten angezeigt.

### *Detected Vision Parts (Erkannte Bildverarbeitungs-Teile)*

**Detected Vision Parts** zeigt:
- In Echtzeit von der Kamera aufgenommenes Bild
- Ein **Verlaufsdiagramm** der Erfassungen der letzten 30 Sekunden, das den Verlauf der Anzahl der pro Aufnahme erkannten Teile anzeigt.


### *Tabelle der erkannten Modelle*

**Details zu den erkannten Komponenten**

Die Tabelle unter dem Bild listet alle im Picking-Bereich vorhandenen Komponenten mit den folgenden Parametern auf:

```{list-table}
:header-rows: 1
:widths: 15 20 65

* - Feld
  - Datentyp
  - Beschreibung
* - **Id**
  - Ganzzahl
  - Eindeutige fortlaufende Kennung der Komponente (0, 1, 2, ...).   
  Id 0 = Komponente mit der höchsten Punktzahl (beste Übereinstimmung mit dem Modell, wenn wie empfohlen nach „Score Descending“ sortiert).
* - **X**
  - Millimeter
  - X-Koordinate des Bauteils.
* - **Y**
  - Millimeter
  - Y-Koordinate des Bauteils.
* - **Rot (Rotation)**
  - Grad
  - Drehwinkel der Komponente. 
* - **Score**
  - Prozentsatz
  - Prozentwert (0,00-1,00 oder 0%-100%), der den Grad der Erkennungszuverlässigkeit ausdrückt. Er steht für die Übereinstimmung/Genauigkeit mit dem Referenzmodell. Höherer Score = bessere Übereinstimmung.
```

```{list-table} **Interpretation des Scores**

* - **Score > 0.90 (90%)**:
  - 
    - Hervorragende Übereinstimmung mit dem Modell
    - Picking mit hoher Zuverlässigkeit

* - **Score 0.80-0.90 (80-90%)**:
  - 
    - Gute Übereinstimmung
    - Sicheres Picking, sofern der Accept Threshold richtig konfiguriert ist

* - **Score 0.70-0.80 (70-80%)**:
  - 
    - Akzeptable Übereinstimmung
    - Die Konsistenz im Laufe der Zeit überprüfen

* - **Score < 0.70 (< 70%)**:
  - 
    - Geringe Übereinstimmung
    - Bei wiederkehrenden Ereignissen das Modell oder Accept Threshold überprüfen.
```

---
(indicatoriperformance)=
## Status- und Leistungsindikatoren

### *Konnektivität*

Statusindikatoren Anzeige für die Kommunikation mit externen Geräten:

```{list-table}
:header-rows: 1
:widths: 25 75

* - Indikator
  - Beschreibung
* - **FlexiBowl®**
  - Status der Hardwareverbindung zwischen dem VisionController (PC) und FlexiBowl®.  
    **Grün**: Verbunden und kommunizierend.  
    **Rot**: Verbindung unterbrochen oder Kommunikationsfehler.
* - **Roboter**
  - Status der Kommunikation mit dem Roboter.   
    **Grün**: TCP/IP-Verbindung hergestellt.  
    **Rot**: Verbindung unterbrochen oder Zeitüberschreitung bei der Kommunikation.
```

```{warning}
**Maßnahmen bei einer Unterbrechung der Verbindung**

**FlexiBowl® rot**:
- Überprüfen Sie das Ethernet-Kabel FlexiBowl® → VisionController
- Überprüfen Sie die FlexiBowl®-Stromversorgung
- Überprüfen Sie die FlexiBowl®-IP im FlexiBowl®-Setup
- Versuchen Sie, eine neue Verbindung herzustellen oder die Software neu zu starten

**Roboter rot**:
- Überprüfen Sie das Ethernet-Kabel Roboter → VisionController
- Prüfen, ob der Roboter eine TCP/IP-Verbindung hergestellt hat
- TCP/IP-Port im Roboter-Setup überprüfen
- Roboterprogramm überprüfen (IP-Adresse des VisionControllers und Port im Abschnitt „Roboter-Setup“ korrekt eingegeben)

In der Produktion müssen beide Indikatoren immer grün sein.
```

### *Zeitanalyse*

Das System liefert eine detaillierte Aufschlüsselung der Zykluszeiten, um mögliche Engpässe zu erkennen und den Prozess zu optimieren.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Zeitposten
  - Beschreibung
* - **Kameraverarbeitungszeit**
  - Zeit, die für die Bildaufnahme vom Kamerasensor benötigt wird. Einschließlich Belichtungszeit und Datenübertragung. 
* - **Locator Processing Time**
  - Zeit, die der Bildverarbeitungsalgorithmus benötigt, um die Komponenten im aufgenommenen Bild zu lokalisieren und zu erkennen. Abhängig von: Anzahl der aktiven Modelle, Komplexität der Modelle, Anzahl der Abstände. 
* - **Total Vision Processing**
  - Summe der Zeiten für Kamera und Locator. Stellt die Gesamtzeit dar, die das Bildverarbeitungssystem benötigt, um ein Bild zu verarbeiten und die Koordinaten zu senden.       
* - **Total FlexiBowl® Time**
  - Zeit, die der FlexiBowl® benötigt, um eine vollständige Bewegungssequenz auszuführen. 
* - **Total Robot Time**
  - Geschätzte oder gemessene Zeit für den vollständigen Pick-&-Place-Vorgang des Roboters. Beinhaltet: Anfahren → Greifen → Anheben → Ablegen → Zurückfahren. 
* - **Total Processing Time**
  - Gesamtzeit des gesamten Zyklus (Vision + FlexiBowl® + Roboter). Bezeichnet die Zeit vom Beginn eines Zyklus bis zum Beginn des nächsten. Bestimmt die theoretische maximale Produktivität (PPM).
```

```{tip}
**Auswertung der Zeiten zur Optimierung**

Anhand des Zeitdiagramms lässt sich der **Engpass** des Systems ermitteln:

**Wenn „Total Vision Processing“ den größten Anteil ausmacht**:
- Zu viele aktive Modelle → Nicht benötigte Modelle deaktivieren
- Zu komplexe Modelle → Durch einen höheren Score-Schwellenwert vereinfachen
- Zu viele Clearances → Anzahl oder Größe der Clearances reduzieren
- Hohe Kamera-Verarbeitungszeit → Belichtungszeit verkürzen

**Wenn „Total FlexiBowl® Time“ den größten Anteil ausmacht**:
- Zu viele Pausen → Synchronisation von Flip/Move optimieren und Stabilisierungspause (Pause X ms) verkürzen
- Bewegungssequenz zu langsam → Geschwindigkeit in Config FlexiBowl® erhöhen
- Drehwinkel zu groß → Move Angle verringern
- Shake zu lang → SHAKE-Geschwindigkeit erhöhen und SHAKE-Zyklen reduzieren  

**Wenn die „Total Robot Time“ den größten Anteil ausmacht**:
- Roboterbahn nicht optimiert → Bahnplanung des Roboters optimieren
- Robotergeschwindigkeit zu niedrig → Bewegungsgeschwindigkeit erhöhen (sofern sicher)
- Ablageabstand zu groß → Ablagepunkt näher positionieren
- Greifzeiten zu lang → Greiferöffnung/-schließung optimieren

**Optimierungsziel**: Die drei Zeiten ausgleichen, um die Gesamtverarbeitungszeit zu reduzieren.
```

---
(analisigrafica)=
## Grafische Analyse

Die Grafiken im unteren Bereich des Dashboards ermöglichen eine prädiktive und diagnostische Analyse der Systemleistung im Zeitverlauf.

### *1. Parts Per Minute (PPM)*

```{list-table}
* - **Produktivitätsdiagramm**
  - Zeigt die durchschnittliche Produktivität des Systems an, ausgedrückt in **entnommenen Teilen pro Minute** (Parts Per Minute).

* - **Merkmale**:
  - 
    - X-Achse: Zeit 
    - Y-Achse: PPM (Teile/Sekunde)
    - Trendlinie: Gleitender Durchschnitt zur Ermittlung von Trends

* - **Verwendung**:
  - 
    - Überwachung der Produktivitätsstabilität im Zeitverlauf
    - Erkennen Sie Leistungseinbußen
    - Berechnung des tatsächlichen Durchsatzes im Vergleich zum theoretischen Durchsatz
```

```{tip}

  :::{list-table} **PPM-Auslegung**

    * - **PPM konstant und stabil**:
      - 
        ✓ System gut konfiguriert  
        ✓ Parameter optimiert  
        ✓ Keine kritischen Engpässe  

    * - **Progressiv sinkender PPM**:
      - 
        ⚠️ Möglicher Verschleiß der Teile (FlexiBowl®-Grip-Oberfläche)  
        ⚠️ Der Trichter leert sich 
        ⚠️ Schmutzablagerungen an Kamera/Beleuchtung  

    * - **PPM mit starken Schwankungen**:
      - 
        ⚠️ Instabilität im Prozess  
        ⚠️ Gelegentliche Erkennungsprobleme  
        ⚠️ Äußere Störungen (Vibrationen, wechselndes Licht)  

    * - **Korrekturmaßnahmen**:
      - 
        - Korrelation anhand von Zeitdiagrammen analysieren
        - Ermitteln, welche Komponente (Vision/FlexiBowl®/Roboter) Abweichungen verursacht
        - Auf bestimmte Parameter einwirken
  :::
```

### *2. Fill Hopper (Trichter befüllen)*

```{list-table}
* - **Grafik Trichteraktivierungen**
  - Zeigt den Verlauf der an den Trichter (Hopper) gesendeten Entleerungsimpulse an.

* - **Merkmale**:
  - 
    - X-Achse: Zeit
    - Y-Achse: Trichteraktivierungen (Ereignisse)
    - Spitzen: Jeder Spitzenwert steht für eine Entleerungsaktivierung

* - **Verwendung**:
  - 
    - Wirksamkeit der Trichterkonfiguration überprüfen
    - Anomalien im Entleerungsverhalten erkennen
```

```{tip}
  
  :::{list-table} **Analyse des Fill-Hopper-Musters**

    * - **Regelmäßige und kontinuierliche Aktivierungen**:
      - 
        ✓ Optimale Hopper-Konfiguration  
        ✓ Stabiler und vorhersehbarer Teilefluss  
        ✓ Berechenbare Betriebsdauer (z. B.: Aktivierung alle 10 Minuten)  

    * - **Immer häufiger auftretende Aktivierungen**:
      - 
        ⚠️ Der Trichter leert sich (weniger Teile = mehr Aktivierungen, um den Füllstand aufrechtzuerhalten)  
        ⚠️ Unzureichende Entladezeit aufgrund geringen Volumens    
        **Maßnahme**: Aufladen des Hoppers rechtzeitig planen

    * - **Keine Aktivierung über einen längeren Zeitraum**:
      - 
        ⚠️ Roboter steht still oder läuft verlangsamt (Teile werden nicht verarbeitet)  
        ⚠️ Mögliches Systemproblem, das keine Teile anfordert    
        **Maßnahme**: Produktionsstatus prüfen

    * - **Sehr kurz aufeinanderfolgende Auslösungen (Burst)**:
      - 
        ⚠️ Hopper-Schwellenwert falsch konfiguriert (zu hoch)  
        ⚠️ Unzureichende Schritte (Teile kommen nicht rechtzeitig an)  
        **Maßnahme**: „Config Hopper“ überprüfen
  :::
```

### *3. Vision - FlexiBowl® - Roboter (Vergleichsdiagramm)*

```{list-table} 
* - **Diagramm mit überlappenden Zeiträumen**
  - Ein Vergleichsdiagramm mit drei Linien, in dem die Dauer der einzelnen Prozesse zeitlich übereinandergelegt wird.

* - **Verwendung**: 
  - Sofort erkennen, welcher Prozess die Gesamtzykluszeit am stärksten beeinflusst und wie sich dies im Laufe der Zeit verändert.
```
---

## Qualitätsüberwachung - Zu überwachende kritische Indikatoren

```{list-table}
* - **Komponenten-Score**
  - Sicherstellen, dass der **Score** der erkannten Komponenten stets über dem Toleranzschwellenwert (Accept Threshold) liegt, der bei der Modellkonfiguration festgelegt wurde.

* - **Überwachung der Werte**:
  - 
    - Tabelle der erkannten Modelle regelmäßig überprüfen
    - Sicherstellen, dass typische Werte zwischen 0,85 und 0,95 liegen
    - Untersuchen, ob die Werte regelmäßig unter 0,80 fallen

* - **Progressiv sinkende Werte**:
  - 
    ⚠️ Echte Teile weichen vom Trainingsteil ab (Produktionsabweichungen)  
    ⚠️ Beleuchtung verändert (schwächeres Hintergrundlicht, Verschmutzung)  
    ⚠️ Kamera nicht mehr scharfgestellt (Vibrationen, Stöße)  
    ⚠️ FlexiBowl®-Oberfläche verschmutzt (störende Muster)  

* - **Korrekturmaßnahmen**:
  - 
    - Kamera, Beleuchtung und FlexiBowl®-Oberfläche reinigen
    - Fokussierung der Kamera überprüfen
    - Bei geänderten Teilen ein erneutes Training des Modells in Betracht ziehen
    - Akzeptanzschwelle senken, wenn die Werte zwar zuverlässig, aber niedriger sind
```
---

## Best Practices für die Produktionsüberwachung

### *Tägliche Kontrollen*

```{list-table}
* - **Zu Beginn der Produktion** (5 Minuten):
  - 
    - Prüfen Sie den FlexiBowl®- und Roboter-Verbindungsanzeigen (grün).
    - Prüfen Sie, ob die ersten Zyklen normale Werte (>0,85) aufweisen.
    - Man kann beobachten, dass sich PPM auf dem erwarteten Wert stabilisiert.

* - **Während der Produktion** (Kontrolle alle 1–2 Stunden):
  - 
    - PPM überprüfen, um die Stabilität sicherzustellen
    - Füllstand des Trichters kontrollieren, um den Nachfüllbedarf abzuschätzen
    - Log auf Fehler oder Warnungen überprüfen

* - **Am Ende der Schicht** (2 Minuten):
  - 
    - Notieren Sie den durchschnittlichen PPM-Wert der Schicht
    - Überprüfen Sie die Anzahl der Trichteraktivierungen
    - Überprüfen Sie auf eventuelle Anomalien oder Ereignisse
    - Vergleichen Sie mit den Daten des Vortags
```
Diese Mindestroutine gewährleistet eine schnelle Problemerkennung und gewährleistet die Nachverfolgbarkeit der Leistung.

### *Leistungsbericht*  

```{tip} **Zu erfassende Schlüsselkennzahlen**
Zur Bewertung der Leistung im Zeitverlauf erfassen Sie:

  :::{list-table} 

    * - **Täglich**:
      - 
        - Durchschnittlicher PPM-Wert der Schicht
        - Gesamtzahl der aufgenommenen Teile
        - Anzahl der Hopper-Aktivierungen
        - Gesamtausfallzeit (und Ursachen)

    * - **Wöchentlich**:
      - 
        - PPM-Trend (steigend/fallend?)
        - Vergleich von theoretischem und realem PPM
        - Durchschnittlicher Score der erkannten Komponenten
        - Eventuelle Konfigurationsänderungen und deren Auswirkungen

    * - **Monatlich**:
      - 
        - Overall Equipment Effectiveness (OEE)
        - Analyse der hauptsächlichen Engpässe
        - Notwendigkeit der vorausschauenden Wartung
        - ROI des Systems
  :::

Diese Daten ermöglichen eine kontinuierliche Optimierung und rechtfertigen Investitionen in Verbesserungen.
```

---

```{raw} html
<div style="border: 2px solid #0d6efd; border-radius: 12px; padding: 2rem; margin: 1.5rem 0; background-color: #f0f6ff; display: flex; align-items: flex-start; gap: 2rem;">
  <div style="flex: 1; min-width: 0;">
    <div style="font-size: 1.2rem; font-weight: 700; color: #0d6efd; margin-bottom: 0.5rem;"> Das System ist nun betriebsbereit!</div>
    <div style="font-size: 0.95rem; color: #444; line-height: 1.6;">Glückwunsch! Das FlexiVision One-System ist nun vollständig konfiguriert, optimiert und für die Produktion validiert.</div>
  </div>
  <div style="flex: 1.4; background: white; border-radius: 8px; padding: 1.2rem 1.5rem; border: 1px solid #d0e4ff; font-size: 0.88rem; color: #333; line-height: 1.8;">
    <div style="font-weight: 600; margin-bottom: 0.5rem;">Zusammenfassung des abgeschlossenen Arbeitsablaufs:</div>
    <div>✓ Hardware-Einrichtung (FlexiBowl®, Roboter, Kamera)</div>
    <div>✓ Vollständige Kalibrierung (Kamera, Roboter)</div>
    <div>✓ FlexiBowl® für optimale Handhabung konfiguriert</div>
    <div>✓ Trichter für automatische Beschickung konfiguriert (falls vorhanden)</div>
    <div>✓ Teilemodelle erstellt und optimiert</div>
    <div>✓ System mit Dashboard-Überwachung validiert</div>
    <div>✓ Leistung geprüft und stabil</div>
    <div style="margin-top: 0.8rem; font-style: italic; color: #555;">Das System ist bereit für den Einsatz in der Produktion mit minimaler Überwachung.</div>
  </div>
  <div style="flex: 0.7; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.9rem;">
    <div style="color: #555; font-weight: 600;">Neueste nützliche Tools:</div>
    <a href="../FEHLERSUCHE/26_trb_shooting_guide.html" style="display: block; padding: 0.6rem 1rem; background: #0d6efd; color: white; border-radius: 6px; text-decoration: none; font-weight: 500;"> Troubleshooting</a>
    <div style="font-size: 0.82rem; color: #555; margin-top: -0.4rem; padding-left: 0.3rem;">Leitfaden zur Fehlerbehebung bei häufigen Problemen</div>
    <a href="../27_Support.html" style="display: block; padding: 0.6rem 1rem; background: #0d6efd; color: white; border-radius: 6px; text-decoration: none; font-weight: 500;"> Support</a>
    <div style="font-size: 0.82rem; color: #555; margin-top: -0.4rem; padding-left: 0.3rem;">Kontakt zum technischen Support</div>
  </div>
</div>
```
