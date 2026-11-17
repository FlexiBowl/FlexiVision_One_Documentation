(hoppersetup)=
# **Hopper Setup**

Dieser Abschnitt beschreibt das Verfahren zur Konfiguration des Hoppers (Trichter). Der Hopper ist die Komponente, die automatisch Teile auf den FlexiBowl® nachfüllt, wenn der Füllstand unter einen Mindestwert sinkt.
 
:::{important}  **Funktionslogik**  
 
FlexiVision steuert die Aktivierungslogik des Hoppers. Es sendet die Zeichenfolge `Hopper;signalnumber;time`, wenn eine Aktivierung als notwendig erachtet wird. 
:::
````{note}
**Voraussetzungen**
 
Bevor Sie fortfahren, stellen Sie sicher, dass:
- der Hopper mechanisch installiert wurde 
- die elektrischen Anschlüsse abgeschlossen sind (Steuersignale und Stromversorgung)
- der FlexiBowl® bereits angeschlossen ist
````
---
## Vorbereitung des physischen Setups
 
````{list-table}
* - **0**
  - Das Kalibriergitter demontieren und das ursprüngliche Layout wiederherstellen:
    - Die Oberfläche neu positionieren
    - den mittleren Flansch neu positionieren 
    - den mittleren Flansch mit seinen vier Schrauben befestigen
````
---
## Zugriff auf die Hopper-Konfiguration
 
````{list-table}
* - **1** 
  - Klicken Sie auf der Hauptseite der Software auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Suchen Sie auf der Seite SETUP das Symbol **Hopper Setup** und klicken Sie darauf
```{dropdown} Setup-Seite 
       ![Setup-Seite](../../../../../_shared/media/images/pagina_setup1.png)
```
* - **3** 
  - Die Konfigurationsseite des Hoppers wird geöffnet
````
 
---
 
## Übersicht der Hopper-Setup-Oberfläche
 
Die Seite Hopper Setup enthält mehrere Bereiche zur Konfiguration der Betriebsparameter der verschiedenen Hopper:
 
![Seite Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
 
````{list-table}
:header-rows: 1
:widths: 30 70
 
* - Bereich
  - Beschreibung
* - **Enable Hopper**
  - Schalter zum Aktivieren/Deaktivieren der Verwendung des Hoppers im System
* - **Steps**
  - Anzahl der erforderlichen Sequenzen, mit denen der aktuell im Sichtbereich befindliche Abschnitt der Scheibe unter den Entladebereich des Hoppers gelangt
* - **Wizard Steps**
  - Startet den geführten Vorgang zur automatischen Berechnung des Parameters Steps (siehe [Wizard Steps](wizardsteps))
* - **Time**
  - Dauer der Hopper-Aktivierung in Millisekunden
* - **Wizard Time**
  - Startet den geführten Vorgang zur automatischen Berechnung der Aktivierungsparameter des Hoppers (siehe [Wizard Time](wizardtime))
* - **Signal**
  - Nummer des Digitalsignals, mit dem der Hopper gesteuert wird
* - **Config Hopper**
  - Schaltfläche zur Konfiguration des Hoppers (im Folgenden zu verwenden)
````
 
---
(confighopper)=
# **Konfiguration des Hoppers**
 
Die Konfiguration des Hoppers ermöglicht die Verwaltung der automatischen Nachfüllung der Komponenten auf der Scheibe des FlexiBowl®. Das System nutzt die Bildverarbeitung, um zu bestimmen, wann der Füllstand unzureichend ist, und aktiviert den Hopper.
 
## Schritt 1: Zugriff auf die Konfiguration
````{list-table}
* - **1**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">.   
    Im Bereich **Hopper Setup** können Sie die angeschlossenen Ladeeinheiten anzeigen und verwalten.
    
    :::{dropdown} Seite Hopper Setup 
    ![Seite Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
    :::
* - **2**
  - Geben Sie im Feld **Signal** die Nummer des Digitalsignals (DO - Digital Output) ein, mit dem der Hopper gesteuert wird
    :::{warning}
      Es ist unbedingt erforderlich, die richtige Signalnummer einzugeben:
      - Eine falsche Nummer aktiviert das falsche Signal (potenziell gefährlich)
      - Konsultieren Sie den während der Installation erstellten Schaltplan
      - Wenden Sie sich im Zweifelsfall an die Person, die die Verkabelung durchgeführt hat
    :::
* - **3**
  - Aktivieren Sie das Kontrollkästchen **Enable Hopper X**, um den entsprechenden Hopper zu aktivieren.
      :::{important}
      Aktivieren Sie den Hopper nur, wenn das Gerät korrekt installiert ist
      :::
* - **4**
  - Klicken Sie auf die Schaltfläche **Config Hopper X**, um auf die spezifische Konfiguration zuzugreifen 
````
## Schritt 2: Definition des Kontrollbereichs
 
:::{video} ../../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
    :width: 100%
    :align: center
:::
 
In dieser Phase wird der Teil der Scheibe definiert, den die Kamera für die Entladung überwachen muss.
````{list-table}
* - **5**
  - Passen Sie den blauen Rahmen auf dem Bildschirm an, um den Bereich einzurahmen, in dem Komponenten erkannt werden.
````
:::{tip}
Bei Fragen während der Konfiguration konsultieren Sie die Schaltfläche **INFO** auf der aktuellen Seite.
:::
 
## Schritt 3: Definition der Schwellenwerte
 
:::{video} ../../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
:width: 100%
:align: center
:::
````{list-table}
* - **6**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small">, um auf die Seite **Define Value Hopper Cam** zuzugreifen, auf der das System darauf trainiert wird, zwischen leerer und voller Scheibe zu unterscheiden.
    :::{dropdown} Seite Define Value Hopper Cam 
    ![Seite Define Value Hopper Cam](../../../../../_shared/media/images/pagina_valuehopper.png)
    :::
* - **7**
  - Entfernen Sie alle Komponenten aus dem Sichtbereich und klicken Sie auf die erste Schaltfläche **CAPTURE**.
* - **8**
  - Platzieren Sie die Mindestanzahl der Komponenten, die Sie im Sichtbereich behalten möchten. Sinkt die Anzahl unter diesen Schwellenwert, wird der Hopper aktiviert.
* - **9**
  - Klicken Sie auf die zweite Schaltfläche **CAPTURE**.
* - **10**
  - Durch Klicken auf <img src="../../../../../_shared/media/images/tasto_AUTO.png" class="inline-icon"> im Expression Builder berechnet das System automatisch die Werte für **Mean** (Mittelwert) und **Standard Deviation** (Standardabweichung).
* - **11**
  - Entfernen Sie einige Teile und klicken Sie auf <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">. 
* - **12**
  - Beobachten Sie die Ergebnisanzeige:
    - **Grün** 🟢: Füllstand unzureichend, Hopper aktiviert sich (Entladung erforderlich)
    - **Rot** 🔴: Füllstand ausreichend, Hopper aktiviert sich NICHT (OK)
 
      :::{warning}
      **Unzureichende Kalibrierung**
 
      Wenn das System den Füllstand nicht korrekt erkennt:
 
      **Problem: Immer grün (Hopper wird immer aktiviert)**  
      → Schwellenwert zu niedrig oder Störungen im Bereich  
      → Lösung: Anzahl der Teile bei der zweiten Erfassung erhöhen, Sauberkeit des Bereichs prüfen  
 
      **Problem: Immer rot (Hopper wird nie aktiviert)**  
      → Schwellenwert zu hoch oder Überwachungsbereich nicht repräsentativ  
      → Lösung: Anzahl der Teile bei der zweiten Erfassung CAPTURE reduzieren, AUTO wiederholen  
 
      **Problem: Fehlerhaftes Verhalten (wechselt zufällig zwischen grün/rot)**  
      → Instabile Beleuchtung oder Bereich zu klein  
      → Lösung: Stabiles Backlight prüfen, Überwachungsbereich vergrößern, Kalibrierung wiederholen  
      :::
````
````{note}
**Hopper Fill Threshold**
 
Der Parameter **Hopper Fill Threshold** definiert den prozentualen Füllstand-Schwellenwert des Sichtbereichs, unterhalb dessen sich der Hopper automatisch aktiviert.
 
Der Wert 100 % entspricht der während der zweiten Erfassung (CAPTURE) erfassten Teilemenge (voller Bereich). Folglich entspricht ein Schwellenwert von 50 % der Hälfte dieser Menge.
 
Das System setzt den Anfangswert automatisch auf **70 %**, was für die meisten Anwendungen ein gutes Gleichgewicht darstellt.
 
**Nachträgliche Anpassung**
 
Der Schwellenwert kann angepasst werden, ohne den Erfassungsvorgang zu wiederholen:
 
- Um **weniger Teile** zu entladen → Prozentsatz verringern (z. B. 50 %) und auf **AUTO** klicken
- Um **mehr Teile** zu entladen → Prozentsatz erhöhen (z. B. 85 %) und auf **AUTO** klicken
 
````
 
:::{tip}
Bei Fragen während der Konfiguration konsultieren Sie die Schaltfläche **INFO** auf der aktuellen Seite.
:::
 
## Schritt 4: Betriebsparameter
 
Kehren Sie zum Hauptbildschirm von Hopper Setup zurück, um das mechanische Verhalten festzulegen.
![Seite Hopper Setup](../../../../../_shared/media/images/pagina_hoppersetup.png)
 
````{list-table} Betriebsparameter
:widths: 20 80
:header-rows: 1
 
* - **Parameter**
  - **Beschreibung und Vorgehensweise**
* - **Steps**
  - Anzahl der Vorschübe (Sequenzen) des FlexiBowl®, die erforderlich sind, um die Teile vom Sichtbereich zum Entladebereich des Hoppers zu bringen. Kann manuell eingestellt oder über den [Wizard Steps](wizardsteps) berechnet werden.
* - **Time**
  - Aktivierungszeit des Hoppers in Millisekunden. Empfohlener Wert: **100 – 1000 ms** (Durchschnitt: **500 ms**). Je nach gewünschtem Durchfluss um ±50 ms anpassen. Kann manuell eingestellt oder über den [Wizard Time](wizardtime) berechnet werden.
````
````{tip}
   Die Aktivierungszeit hängt nicht nur vom eingestellten Wert ab, sondern auch von der aktuell im Hopper-Behälter vorhandenen Menge an Komponenten. Es ist wichtig, eine konstante Füllmenge für einen gleichmäßigen Durchfluss aufrechtzuerhalten.
````
````{tip}
Der Wert Time hängt eng mit der Füllmenge des Hoppers zusammen: 
- Bei vollem Hopper befinden sich mehr Teile im Entladebereich 
- Bei halbvollem Hopper befinden sich weniger Teile im Entladebereich 
 
````
:::{important}
Generell ist es wichtig, die maximale Füllmenge des verwendeten Hoppers niemals zu überschreiten. 
:::
 
---
 
(wizardsteps)=
### *Wizard Steps: Geführte Berechnung des Parameters Steps*
 
Der **Wizard Steps** unterstützt den Bediener bei der Berechnung der Anzahl der Sequenzen, die erforderlich sind, damit ein Teil, das in der Mitte des Sichtbereichs platziert wird, den Entladebereich des Hoppers erreicht.
 
:::{dropdown} Hopper Step Setup Cam X
![Hopper Step Setup](../../../../../_shared/media/images/pagina_hopperstepwizard.png)
:::
 
````{list-table}
* - **1**
  - Platzieren Sie ein einzelnes Teil in der Mitte des Sichtbereichs.
    :::{important}
    Stellen Sie sicher, dass die aktuell auf dem FlexiBowl® geladene Sequenz die endgültige ist, also dieselbe, die in der Produktion verwendet wird. Ein späterer Sequenzwechsel würde den berechneten Wert ungültig machen.
    :::
* - **2**
  - Klicken Sie auf **Reset Steps**, um den Zähler zurückzusetzen und den Kalibrierungsvorgang zu starten.
* - **3**
  - Klicken Sie auf **Test Sequence**, um eine einzelne Sequenz des FlexiBowl® auszuführen.
    :::{tip}
    Warten Sie, bis die Sequenz abgeschlossen ist, bevor Sie eine weitere ausführen.
    :::
* - **4**
  - Klicken Sie wiederholt auf **Test Sequence**, bis das Teil den Hopper-Bereich erreicht. Der **Current Step Count** wird nach jeder ausgeführten Sequenz automatisch aktualisiert.
* - **5**
  - Wenn das Teil den Hopper-Bereich erreicht, klicken Sie auf **Save Hopper Step**, um den aktuellen Wert als Parameter Steps zu speichern.
````
 
:::{warning}
Der mit dem Wizard Steps berechnete Wert **bleibt nach einem Neustart der Software nicht erhalten**, wenn das Rezept nicht gespeichert wird. Denken Sie daran, das Rezept am Ende des Vorgangs zu speichern (siehe [Speichern der Konfiguration](#salvataggio-configurazione)).
:::
 
Die Anzeige **Calibration Active** zeigt den Status der laufenden Kalibrierung an:
 
| Farbe | Status |
| --- | --- |
| 🔴 Rot | Kalibrierung nicht aktiv / noch nicht gestartet |
| 🟢 Grün | Kalibrierung läuft / abgeschlossen |
 
 
### *Berechnung des Parameters Steps*
 
![Erste Seite Steps](../../../../../_shared/media/images/Steps1.png)
![Zweite Seite Steps](../../../../../_shared/media/images/Steps2.png)
![Dritte Seite Steps](../../../../../_shared/media/images/Steps3.png)
![Vierte Seite Steps](../../../../../_shared/media/images/Steps4.png)
 
---
 
(wizardtime)=
### *Wizard Time: Geführte Berechnung der Aktivierungsparameter*
 
Der **Wizard Time** unterstützt den Bediener bei der Einstellung der Aktivierungsparameter des Hoppers (Amplitude, Frequenz und Aktivierungszeit) und überprüft deren Wirkung durch einen direkten Test des Teileflusses.
 
:::{dropdown} FlexiBowl® X Hopper – Time and Parameter Setup
![Hopper Time Setup](../../../../../_shared/media/images/pagina_hoppertimewizard.png)
:::
 
````{list-table}
* - **1**
  - Füllen Sie den Hopper mit einer ausreichenden Menge an Teilen, um die normalen Betriebsbedingungen zu simulieren.
* - **2**
  - Überprüfen Sie, ob die Teile korrekt positioniert sind und sich frei zum Hopper-Auslass bewegen können.
* - **3**
  - Stellen Sie die Werte für **Amplitude (V)**, **Frequency (Hz)** und **Activation Time (ms)** über die entsprechenden Schieberegler oder durch direkte Eingabe des Werts im Zahlenfeld ein.
* - **4**
  - Klicken Sie auf **Test Hopper**, um den Hopper mit den eingestellten Parametern zu aktivieren und den Teilefluss zu überprüfen.
* - **5**
  - Passen Sie die Werte an und wiederholen Sie den Test, bis das gewünschte Zuführverhalten erreicht ist.
````
 
:::{tip}
Fahren Sie mit der Konfiguration des nächsten Abschnitts (Hopper Step) erst fort, wenn der Teilefluss zufriedenstellend ist.
:::
 
## Speichern der Konfiguration
````{warning}
**Speichern des Rezepts obligatorisch**
 
Nach Abschluss der Hopper-Konfiguration:
 
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
      - Bestätigen Sie das Speichern
  :::
**WICHTIG**: Jede vorgenommene Änderung wird **NUR** gespeichert, wenn das Rezept korrekt gespeichert wird, bevor Sie die Seite verlassen oder wechseln.
 
Ohne Speichern gehen beim Schließen von FlexiVision One alle Hopper-Konfigurationen verloren!
````
 
---
 
 
## Nächste Schritte
 
Sobald das Hopper Setup abgeschlossen ist (oder übersprungen wurde, falls nicht vorhanden), fahren Sie fort mit:
 
- [Robot Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Speichern des Rezepts](ricettabase)
 
