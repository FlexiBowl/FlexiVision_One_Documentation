(hoppersetup)=
# **Hopper Setup**

In diesem Abschnitt wird die Vorgehensweise zur Konfiguration des Trichters (Hopper) beschrieben. Der Trichter ist die Komponente, die automatisch Teile in den FlexiBowl® befördert, sobald der Füllstand unter einen Mindestwert fällt.

:::{important}  **Betriebslogik**  

FlexiVision steuert die Aktivierungslogik des Trichters. Er sendet die Zeichenfolge `Hopper;signalnumber;time`, wenn er die Aktivierung für notwendig erachtet. 
:::
```{note}
**Voraussetzungen**

Stellen Sie vor dem Fortfahren Folgendes sicher:
- Der Trichter wurde mechanisch installiert 
- Die elektrischen Anschlüsse sind hergestellt (Steuersignale und Stromversorgung)
- Die FlexiBowl® ist bereits angeschlossen
```
---
## Vorbereitung der physischen Einrichtung

````{list-table}
* - **0**
  - Demontieren Sie das Kalibrierungsgitter und stellen Sie das ursprüngliche Layout wieder her:
    - Setzen Sie die Oberfläche wieder ein
    - Setzen Sie den Mittelflansch wieder ein 
    - Befestigen Sie den Mittelflansch mit den vier Schrauben
````
---
## Zugriff auf die Hopper-Konfiguration

```{list-table}
* - **1** 
  - Klicken Sie auf der Hauptseite der Software auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Suchen Sie auf der SETUP-Seite das Symbol **Hopper Setup** und klicken Sie darauf
    ```{dropdown} Setup-Seite 
       ![Setup-Seite](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3** 
  - Die Seite zur Konfiguration des Trichters wird geöffnet
```

---

## Übersicht über die Benutzeroberfläche Hopper Setup

Die Seite Hopper Setup enthält verschiedene Abschnitte zur Konfiguration der Betriebsparameter der verschiedenen Trichter:

![Seite Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Abschnitt
  - Beschreibung
* - **Enable Hopper**
  - Schalter zum Aktivieren/Deaktivieren der Verwendung des Trichters im System
* - **Steps**
  - Anzahl der erforderlichen Sequenzen, in denen der Teil der Scheibe, der sich gerade im Sichtbereich befindet, unter den Auslaufbereich des Trichters gelangt
* - **Time**
  - Dauer der Trichteraktivierung in Millisekunden
* - **Signal**
  - Nummer des digitalen Signals, das zur Steuerung des Trichters verwendet wird
* - **Config Hopper**
  - Schaltfläche zum Konfigurieren des Trichters (für die spätere Verwendung)
```


---
(confighopper)=
# **Konfiguration des Trichters (Hopper)**

Die Konfiguration des Trichters ermöglicht die Steuerung der automatischen Zuführung von Komponenten auf die Scheibe des FlexiBowl®. Das System erkennt mit Hilfe von Bildverarbeitung, wann der Füllstand zu niedrig ist und aktiviert den Trichter.

## Schritt 1: Zugriff auf die Konfiguration
```{list-table}
* - **1**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">.   
    Im Abschnitt **Hopper Setup** können Sie die angeschlossenen Ladeeinheiten anzeigen und verwalten.
    
    :::{dropdown} Seite Hopper Setup 
    ![Seite Hooper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
    :::
* - **2**
  - Geben Sie im Feld **Signal** die Nummer des digitalen Signals (DO - Digital Output) ein, das zur Steuerung des Trichters verwendet wird
    :::{warning}
      Es ist äußerst wichtig, die richtige Signalnummer einzugeben:
      - Eine falsche Nummer aktiviert das falsche (potenziell gefährliche) Signal
      - Beachten Sie den bei der Installation erstellten Schaltplan
      - Wenden Sie sich im Zweifelsfall an denjenigen, der die Verkabelung vorgenommen hat
    :::
* - **3**
  - Aktivieren Sie das Kästchen **Enable Hopper X**, um den entsprechenden Hopper zu aktivieren.
      :::{important}
      Aktivieren Sie den Trichter nur, wenn das Gerät korrekt installiert ist
      :::
* - **4**
  - Klicken Sie auf die Schaltfläche **Config Hopper X**, um die spezifische Konfiguration aufzurufen 
```
## Schritt 2: Festlegen des Überwachungsbereichs

:::{video} ../../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
    :width: 100%
    :align: center
:::

In diesem Schritt legen Sie den Bereich der Scheibe fest, den die Kamera für die Entleerung überwachen soll.
```{list-table}
* - **5**
  - Passen Sie den blauen Rahmen auf dem Bildschirm an, um den Bereich einzurahmen, in dem die Komponenten erfasst werden sollen.
```
:::{tip}
Wenn Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO**-Taste auf der aktuellen Seite.
:::

## Schritt 3: Festlegung der Schwellenwerte

:::{video} ../../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
:width: 100%
:align: center
:::
```{list-table}
* - **6**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small">, um die Seite **Define Value Hopper Cam** aufzurufen, auf der Sie das System anweisen, zwischen einer leeren und einer vollen Scheibe zu unterscheiden.
    :::{dropdown} Seite Define Value Hopper Cam 
    ![Seite Define Value Hopper Cam](../../../../../_shared/media/images/pagina_valuehopper.png)
    :::
* - **7**
  - Entfernen Sie alle Komponenten aus dem Sichtbereich und klicken Sie auf die erste Schaltfläche **CAPTURE**.
* - **8**
  - Legen Sie die Mindestanzahl an Komponenten fest, die im Sichtbereich verbleiben sollen. Fällt die Zahl unter diesen Schwellenwert, wird der Trichter aktiviert.
* - **9**
  - Klicken Sie auf die zweite Schaltfläche **CAPTURE**.
* - **10**
  - Durch Klicken auf <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> im Expression Builder berechnet das System automatisch die Werte für **Mean** (Mittelwert) und **Standard Deviation** (Standardabweichung).
* - **11**
  - Entfernen Sie einige Teile und klicken Sie auf <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">. 
* - **12**
  - Beobachten Sie die Ergebnisanzeige:
    - **Grün** 🟢: Füllstand unzureichend, der Trichter wird aktiviert (Entleerung erforderlich)
    - **Rot** 🔴: Füllstand ausreichend, der Trichter wird NICHT aktiviert (OK)

      :::{warning}
      **Unzureichende Kalibrierung**

      Wenn das System den Füllstand nicht korrekt erkennt:

      **Problem: Immer grün (Trichter immer aktiv)**  
      → Schwellenwert zu niedrig oder Störungen im Bereich  
      → Lösung: Anzahl der Teile bei der zweiten Erfassung erhöhen, Sauberkeit des Bereichs überprüfen  

      **Problem: Immer rot (Trichter wird nie aktiviert)**  
      → Schwellenwert zu hoch oder Überwachungsbereich nicht repräsentativ  
      → Lösung: Reduzieren Sie die Anzahl der Teile in der zweiten CAPTURE-Erfassung, wiederholen Sie AUTO  

      **Problem: Fehlerhaftes Verhalten (wechselt zufällig zwischen grün und rot)**  
      → Instabile Beleuchtung oder zu kleiner Bereich  
      → Lösung: Stabile Hintergrundbeleuchtung prüfen, Überwachungsbereich vergrößern, Kalibrierung wiederholen  
      :::
```
```{note}
**Hopper Fill Threshold**

Der Parameter **Hopper Fill Threshold** definiert den prozentualen Schwellenwert des Sichtfelds, bei dessen Unterschreitung der Hopper automatisch aktiviert wird.

Der Wert 100 % entspricht der während des zweiten CAPTURE erfassten Stückzahl (voller Bereich). Ein Schwellenwert von 50 % entspricht also der Hälfte dieser Menge.

Das System setzt den Anfangswert automatisch auf **70 %**, was für die meisten Anwendungen ein gutes Gleichgewicht darstellt.

**Änderung während des Betriebs**

Der Schwellenwert kann angepasst werden, ohne den Erfassungsvorgang zu wiederholen:

- Um **weniger Teile** zu entladen → den Prozentsatz verringern (z. B. 50 %) und auf **AUTO** klicken
- Um **mehr Teile** zu entladen → den Prozentsatz erhöhen (z. B. 85 %) und auf **AUTO** klicken

```

:::{tip}
Wenn Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO**-Taste auf der aktuellen Seite.
:::

## Schritt 4: Betriebsparameter

Kehren Sie zum Hauptbildschirm von Hopper Setup zurück, um das mechanische Verhalten festzulegen.
![Seite Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
```{list-table} Betriebsparameter
:widths: 20 80
:header-rows: 1

* - **Parameter**
  - **Beschreibung und Vorgehensweise**
* - **Steps**
  - Anzahl der erforderlichen FlexiBowl®-Vorschübe (Sequenzen), um die Teile vom Sichtbereich zum Entladebereich des Trichters zu befördern.
* - **Time**
  - Millisekunden der Trichteraktivierung.   Empfohlener Wert: **100 – 1000 ms** (Durchschnitt: **500 ms**). Passen Sie den Wert je nach gewünschtem Durchsatz um ±50 ms an.
```
```{tip}
   Die Aktivierungszeit hängt nicht nur vom eingestellten Wert ab, sondern auch vom Volumen der derzeit im Trichterbehälter vorhandenen Teile. Für einen gleichmäßigen Durchsatz ist es unerlässlich, eine konstante Beladung aufrechtzuerhalten.
```
```{tip}
Der Zeitwert steht in engem Zusammenhang mit dem Ladevolumen des Trichters: 
- Bei einem vollen Trichter befinden sich mehr Teile im Auslaufbereich 
- Bei einem halbvollen Trichter befinden sich weniger Teile im Auslaufbereich 

```
:::{important}
Generell ist es wichtig, die maximale Beladung des verwendeten Trichters niemals zu überschreiten. 
:::

### *Berechnung des Parameters Schritte*

![Erste Seite Schritte](../../../../../_shared/media/images/Steps1.png)
![Zweite Seite Schritte](../../../../../_shared/media/images/Steps2.png)
![Dritte Seite Schritte](../../../../../_shared/media/images/Steps3.png)
![Vierte Seite Schritte](../../../../../_shared/media/images/Steps4.png)

## Speichern der Konfiguration
```{warning}
**Obligatorische Rezeptspeicherung**

Am Ende der Hopper-Konfiguration:

  :::{list-table}
    * - 1. 
      - Überprüfen Sie, ob alle Parameter korrekt konfiguriert sind:
        - Überwachungsbereich positioniert
        - Schwellenwerte kalibriert (TEST funktioniert)
        - Steps und Time eingestellt
    * - 2. 
      - Kehren Sie zur Hauptseite zurück <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon icon-small">
    * - 3. 
      - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon icon-small">
    * - 4. 
      - Bestätigen Sie die Speicherung
  :::
**WICHTIG**: Jede vorgenommene Änderung wird **NUR** gespeichert, wenn das Rezept vor dem Verlassen oder Wechseln der Seite ordnungsgemäß gespeichert wurde.

Ohne Speichern gehen alle Trichterkonfigurationen beim Schließen von FlexiVision One verloren!
```

---


## Nächste Schritte

Nach Abschluss des Trichter-Setups (oder Überspringen, falls nicht vorhanden) fahren Sie fort mit:

- [Roboter-Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Rezept speichern](ricettabase)



