# **Ersteinrichtung**
```{warning}
**Nicht erreichbare Komponenten**

Wenn FlexiBowl®, Roboter oder Kamera nicht erreichbar sind:

1. Überprüfen Sie, ob alle Ethernet-Kabel korrekt angeschlossen sind  
2. Überprüfen Sie, ob Switch/Router eingeschaltet sind  
3. Überprüfen Sie die IP-Adressen aller Geräte:  
   - Sie müssen sich im selben Subnetz befinden (z. B.: 192.168.1.x)  
   - Es dürfen keine IP-Konflikte vorliegen (zwei Geräte mit derselben IP)  
4. Verwenden Sie den Befehl `ping` im Terminal, um die Erreichbarkeit zu testen  
5. Deaktivieren Sie vorübergehend die Windows-Firewall für den Port/Adapter, der für die GigE-Kameras verwendet wird  

Einzelheiten zur Netzwerkkonfiguration finden Sie unter [Verkabelung und Anschlüsse](cablaggio).
```
(troubleshooting_cam_setup)=
## Fehlerbehebung für den Abschnitt Kameraeinrichtung

```{warning}
**Fokussierungsprobleme**

Wenn das Bild unscharf erscheint:

1. Prüfen Sie, ob sich die Kamera im richtigen Arbeitsabstand befindet ([Calcolo Distanza Ottimale](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))  
2. Überprüfen Sie, ob das Objektiv vollständig festgeschraubt ist   
3. Vergewissern Sie sich, dass sich kein Schmutz oder Fingerabdrücke auf dem Objektiv befinden  
4. Stellen Sie sicher, dass die Kamera genau parallel zur FlexiBowl®-Arbeitsfläche montiert ist  

```
```{tip}
**Probleme mit der Helligkeit**

Wenn das aufgenommene Bild zu dunkel oder zu hell ist:

**Zu dunkel**:
- Überprüfen Sie, ob Backlight/Toplight eingeschaltet ist (Konfig FlexiBowl®)  
- Erhöhen Sie die Belichtungszeit (Parameter Cam Exposure in [Camera FLB])  

**Zu hell (überbelichtet)**:
- Verringern Sie die Belichtungszeit (Parameter Cam Exposure in [Camera FLB])  
- Vergewissern Sie sich, dass kein übermäßiges Umgebungslicht vorhanden ist  
- Passen Sie die Blendenöffnung im Objektivgehäuse der Kamera an  
  :::{warning}
  Seien Sie beim Umgang mit der Kamera besonders vorsichtig, da bereits eine kleine Verschiebung der Kamera die Zuverlässigkeit der Kalibrierung beeinträchtigen kann, wenn diese bereits durchgeführt wurde
  :::
```
```{note}
**Aufnahmeleistung**

Wenn die Bildaufnahme langsam ist:
- Überprüfen Sie, ob das Ethernet-Kabel ein Gigabit-Kabel ist (ab Cat6 )  
- Überprüfen Sie, ob der Netzwerk-Switch ein Gigabit-Ethernet-Switch ist (kein Fast-Ethernet-Switch mit 100 Mbit/s)  
- Ändern Sie die Latenzstufe, wenn es keine Probleme mit blauen Bildschirmen gibt  
- Reduzieren Sie die Paketgröße auf 1500-2000  


Die maximale Bildrate der Kamera beträgt 24 fps (Bilder pro Sekunde), was für alle standardmäßigen Picking-Anwendungen ausreichend ist.
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Bild zu dunkel**
  - • Belichtung der Kamera zu niedrig  
    
    • Toplight ausgeschaltet oder defekt  

    • Backlight ausgeschaltet oder defekt  

    • Toplight mit unzureichender Leistung  
    
    • Objektiv mit Schutzkappe  
  - • Belichtung in den Kameraeinstellungen erhöhen  
    
    • Sicherstellen, dass das Toplight eingeschaltet ist  
    
    • Sicherstellen, dass in der FlexiBowl®-Konfiguration das Häkchen bei „Light On“ gesetzt ist  
    
    • Stromversorgung des Toplights überprüfen  
    
    • Schutzkappe vom Objektiv entfernen  
* - **Bild zu hell (überbelichtet)**
  - • Belichtung in den Kameraeinstellungen zu hoch  
    
    • Reflexionen von der FlexiBowl®-Oberfläche
  - • Belichtung in den Kameraeinstellungen verringern  
    
    • Greiffläche durch eine weniger reflektierende ersetzen  
* - **Bild unscharf**
  - • Linse nicht scharfgestellt  
    
    • Objektiv nicht vollständig festgeschraubt  
    
    • Objektiv verschmutzt  
    
    • Kamera bewegt sich/Vibrationen  
  - • Kamerafokus korrigieren  
    
    • Objektiv festschrauben, bis Metall-Metall-Kontakt besteht  
    
    • Objektiv mit Mikrofasertuch reinigen  
    
    • Kamera besser befestigen und Vibrationen reduzieren  
* - **Bild mit Artefakten oder Linien**  
  - • Elektromagnetische Störungen  
    
    • Kamerakabel beschädigt  
    
    • Kamerasensor beschädigt  
  - • Kamerakabel von EMI-Quellen fernhalten, abgeschirmtes Kabel verwenden  
    
    • Ethernet-Kabel der Kamera austauschen  
    
    • Kamera austauschen  
* - **Kamera nimmt während des Zyklus keine Bilder auf**  
  - • Trigger nicht konfiguriert  
    
  - • Erfassungstrigger korrekt konfigurieren  
* - **Kamera verarbeitet während des Zyklus nicht**  
  - 
```
(scelta_camera)=
### *Konfigurationsverfahren*

```{list-table}
* - **Zugriff auf die Konfiguration**
  - 1. Klicken Sie auf die Schaltfläche **Config Camera X** (wobei X die Nummer der Kamera ist)
    2. Es öffnet sich die erste Seite des Kalibrierungsassistenten, auf der Sie den Parameter „**Cam Exposure**“ ändern können

* - **Aktivierung des erweiterten Modus**
  - 3. Klicken Sie auf die Schaltfläche **Expert** (unten rechts)
    4. Dieser Modus bietet Zugriff auf alle erweiterten Kameraeinstellungen, die für die Erstkonfiguration erforderlich sind
* - **Konfiguration des Bildaufnahmegeräts**
  - 5. Klicken Sie im Fenster **Expert** unter **Settings** auf den Abschnitt **Image Acquisition**
    6. Klicken Sie auf **Image Acquisition Device**
    7. Es öffnet sich ein Menü zur Auswahl der verfügbaren Aufnahmegeräte
* - **Spezifische Kamera-Identifikation**
  - 8. Wählen Sie im Gerätemenü die gewünschte Kamera aus
        - Suchen Sie in der Liste nach der Seriennummer oder dem Modell der Kamera
        - Beispiel: „CAM-CIC-5000-20G-XXXXX" (wobei XXXXX die Seriennummer ist)
    9. Klicken Sie auf die Kamera, um sie auszuwählen
```
:::{video} ../../../../_shared/media/videos/Step2_calib.mp4
  :width: 100%
  :align: center
:::

```{tip}
**Ermittlung der richtigen Seriennummer**

Wenn mehrere Kameras oder Geräte aufgelistet sind:
- Die Seriennummer befindet sich auf einem Etikett an der Kamera
- Vergleichen Sie die letzte Zeichengruppe der Seriennummer, um die richtige Kamera zu identifizieren
- Trennen Sie im Zweifelsfall andere Kameras ab, um die verwendete Kamera zu identifizieren
```


```{list-table} 
* - **Auswahl des Videoformats**
  - 11. Klicken Sie auf **Video Formats**
    12. Wählen Sie aus der Liste der verfügbaren Formate aus **Generic GigEVision**
    13. Wählen Sie **Mono** (monochrom) als Sensortyp
```


```{warning}
**Korrektes Format erforderlich**

Wählen Sie unbedingt **Generic GigEVision Mono**:
- Andere Formate funktionieren möglicherweise nicht oder verursachen Fehler
- Farbformate sind mit dieser Kamera nicht kompatibel
- Wenn das Format nicht verfügbar ist, fehlen möglicherweise Treiber oder Systemkonfigurationen
```

```{list-table}
* - **Erfassungssystem aktivieren**
  - 14. Nachdem Sie das richtige Format ausgewählt haben, klicken Sie auf „**Initialize Acquisition**“.
    15. Warten Sie, bis die Initialisierung abgeschlossen ist (einige Sekunden)
* - **Funktionsprüfung der Datenerfassung**
  - 16. Suchen Sie die Schaltfläche **Run** oben links in der Benutzeroberfläche (Symbol „Play“)
    17. Klicken Sie 5 bis 10 Mal hintereinander auf „**Run**“, um Testbilder aufzunehmen
    18. Beachten Sie den Bildanzeigebereich:
        - Es sollte die Kameraansicht auf dem FlexiBowl® angezeigt werden
        - Das Bild sollte bei jedem Klick auf „Run“ aktualisiert werden
```

(schermo_blu)=
```{warning}
**Diagnose vollständig blauer Bildschirm**

Wenn das aufgenommene Bild während des Tests mindestens einmal **komplett blau** erscheint:

**Ursache**: GigE-Kommunikationsproblem (Netzwerklatenz oder suboptimale Paketgröße)

**Lösung**:

1. Wählen Sie im oberen Menü **GigE** (oder **GigE Vision Settings**)

2. Ändern Sie die folgenden Parameter:
   - **Latency Level** (Latenzstufe)
   - **Packet Size** (Paketgröße)

Fahren Sie mit den folgenden Schritten fort, um diese Parameter optimal zu konfigurieren.
```

---

#### *Latency Level (Latenzstufe)*

```{note}
**Einstellung der Latency**

Der Parameter **Latency Level** steuert den Kommunikationspuffer zwischen der Kamera und VisionController.

**Typische Werte**:
- Standardwert: 0
- Verfügbarer Bereich: 0-3

**So nehmen Sie die Einstellung vor:**

1. Erhöhen Sie den Wert schrittweise
2. Testen Sie nach jeder Änderung die Erfassung (Schaltfläche Run) 5-10 Mal
3. Wenn keine blauen Bildschirme mehr erscheinen, ist der Wert korrekt
4. Wenn weiterhin blaue Bildschirme angezeigt werden, erhöhen Sie den Wert weiter oder versuchen Sie, den Parameter Packet Size zu ändern
```

#### *Packet Size (Paketgröße)*

```{note}
**Einstellung des Packet Size**

Der Parameter **Packet Size** definiert die Größe der über das Ethernet-Netzwerk übertragenen Datenpakete.

**Typische Werte**:
- Standardwert: 8164 Bytes

**So nehmen Sie die Einstellung vor:**

1. Schrittweise auf 8000, 7000 usw. verringern.
2. Testen Sie nach jeder Änderung die Erfassung (Schaltfläche Run) 5-10 Mal
3. Wenn keine blauen Bildschirme mehr erscheinen, ist der Wert korrekt
4. Wenn weiterhin blaue Bildschirme angezeigt werden, verringern Sie den Wert weiter oder versuchen Sie, den Parameter Latency Level zu ändern
```


---

```{list-table}
* - **Abschließende Überprüfung und Speichern**
  - 19. Klicken Sie mindestens 2–3 Mal hintereinander auf „**Run**“
    20. Bitte überprüfen Sie Folgendes:
      - Kein Bild erscheint vollständig blau oder schwarz
      - Die Bilder werden regelmäßig aktualisiert
      - Die Oberfläche der FlexiBowl® ist deutlich sichtbar
      - Die Beleuchtung ist gleichmäßig
    21. Wenn alle Tests positiv ausfallen, ist die Konfiguration korrekt
```

(troubleshooting_calib_cam)=
## Kamera-Kalibrierung

### *Muster nicht erkannt*

```{warning}
**Fehler: „Unable to detect calibration pattern“**

Ursache: Die Software kann das Gittermuster nicht erkennen.

**Lösungen**:
- Erhöhen Sie den Kontrast (passen Sie die Belichtung oder Beleuchtung an)
- Stellen Sie sicher, dass das gesamte Gitter im Bild sichtbar ist
- Verbessern Sie die Schärfe
- Reinigen Sie die Oberfläche des Gitters (Staub oder Fingerabdrücke können stören)
- Überprüfen Sie, dass es sich um das richtige Gitter handelt (Quadrate, keine Kreise oder andere Muster)
```

### *Kalibrierung immer „Bad“ oder „Acceptable“*

```{warning}
**Unzureichende Kalibrierungsqualität**

Wenn die Kalibrierung trotz Anpassungen unter „Excellent“ bleibt:

1. Überprüfen Sie den Arbeitsabstand zwischen Kamera und FlexiBowl® (er muss dem berechneten Wert entsprechen)
2. Stellen Sie sicher, dass die Kamera parallel zur Ebene des FlexiBowl® ausgerichtet ist (sie muss perfekt horizontal sein)
3. Stellen Sie sicher, dass die Kamera stabil ist (keine Vibrationen während der Aufnahme)
4. Überprüfen Sie, ob das Objektiv vollständig festgeschraubt ist

Wenn das Problem weiterhin besteht, liegt möglicherweise ein mechanisches Problem bei der Montage vor. Siehe [Mechanische Installation](09_Installazione_Meccanica.md) zur Überprüfung.
```

### *Fehler nach Wechsel der Beleuchtung*

```{tip}
**Neukalibrierung nach Änderung von Backlight/Toplight**

Wenn Sie von Backlight zu Toplight (oder umgekehrt) wechseln:

1. Die geometrische Kalibrierung bleibt gültig (sie muss nicht erneut durchgeführt werden)
2. Es ist lediglich erforderlich, die Belichtung der Kamera an die neue Beleuchtungsart anzupassen
3. Nehmen Sie ein Testbild auf, um zu prüfen, ob das Muster noch deutlich sichtbar ist

Generell ist es ratsam, sich von Anfang an für eine Beleuchtungsart zu entscheiden und diese Konfiguration beizubehalten.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Kalibrierung schlägt fehl (Softwarefehler)**
  - • Kalibrierungsgitter nicht korrekt erkannt
    
    • Unzureichende/übermäßige Beleuchtung
    
    • Beschädigtes oder verschmutztes Kalibriergitter
    
  - • Zielobjekt flach und gut sichtbar positionieren
    
    • Belichtung der Kamera anpassen, um das Zielobjekt gut darzustellen
    
    • Sauberes und unbeschädigtes Kalibriergitter verwenden
    
* - **Kalibrierungsfehler zu hoch**
  - • Kamera nicht perfekt senkrecht zur Oberfläche
    
    • Kalibriergitter nicht flach
    
    • Übermäßige optische Verzerrung
    
  - • Senkrechte Ausrichtung der Kamera mit Wasserwaage überprüfen (Toleranz ±1°)
    
    • Platzieren Sie das Zielobjekt auf einer festen und ebenen Oberfläche
    
    • Qualität der optischen Linse prüfen, reinigen oder ersetzen
    
* - **Tatsächliche Koordinaten stimmen nicht mit den gemessenen Koordinaten überein**
  - • Falscher Skalierungsfaktor (falsche Tile Size)
    
    • Kamera nach Kalibrierung verschoben
    
  - • Kalibrierung vollständig wiederholen
    
    • Kamera fest fixieren, um Verschiebungen zu vermeiden
    
    • Überprüfen Sie die Abmessungen des Kalibrierungsziels gemäß der Dokumentation
* - **Kalibrierung nur in der Bildmitte gültig**
  - • Periphere optische Verzerrung
    
    • Kalibrierung mit zu wenigen Punkten
  - • Verwenden Sie ein hochwertiges Objektiv mit geringer Verzerrung
    
    • Prüfen Sie, ob der Arbeitsabstand korrekt ist
```



(troubleshooting_fb_setup)=
## Fehlersuche für den Abschnitt FlexiBowl® Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **FlexiBowl® reagiert nicht auf Softwarebefehle**
  - • IP-Adresse nicht konfiguriert oder falsch
    
    • FlexiBowl® nicht mit dem Netzwerk verbunden
    
    • Firewall blockiert die Kommunikation
    
    • FlexiBowl® nicht eingeschaltet
  - • IP-Adresse im FlexiBowl® Setup überprüfen und korrekt konfigurieren
    
    • Verbindung mit einem Ping vom VisionController aus testen
    
    • Firewall zu Testzwecken vorübergehend deaktivieren
    
    • Überprüfen, ob die LED READY am FlexiBowl® leuchtet
* - **FlexiBowl®-Konfiguration kann nicht gespeichert werden**
  - • Festplatte voll

  - • Speicherplatz auf der Festplatte freigeben
 
* - **FlexiBowl®-Parameter werden nicht übernommen**
  - • Schaltfläche „Synchronize Parameters“ wurde nicht gedrückt
    
    • Verbindung zu FlexiBowl® unterbrochen
    
    • FlexiBowl®-Fehler
  - • Nach Änderungen immer auf „Synchronize Parameters“ klicken
    
    • Stabilität der Ethernet-Verbindung prüfen
    
    • FlexiBowl® neu starten
* - **Wizard FlexiBowl® berechnet falsche Parameter**
  - • Falsche Komponentencharakterisierung (Geometrie/Verhalten)
    
    • Falsches FlexiBowl®-Modell ausgewählt
    
    • Drehrichtung falsch eingestellt
  - • Auswahl der Geometrie überprüfen (FLAT/CYLINDRICAL/COMPLEX)
    
    • Größe des installierten FlexiBowl® mit der ausgewählten Größe vergleichen
    
    • Physische Drehrichtung überprüfen und mit der Einstellung vergleichen
```

(troubleshooting_hopper_setup)=
## Fehlersuche für den Abschnitt Trichter-Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Hopper wird nie automatisch aktiviert**
  - • Hopper in der Software nicht aktiviert
    • Falsches Signal-Feld
    • Kontrollbereich nicht definiert
    
    • Schwellenwerte nicht kalibriert
    
    • Trichter nicht elektrisch angeschlossen
  - • Kontrollkästchen „Enable Hopper X“ aktivieren
    • Überprüfen, ob die **Signal**-Nummer mit dem physisch angeschlossenen DO übereinstimmt
    • Kontrollbereich in „Define Area Check“ definieren
    
    • Schwellenwertkalibrierung mit leerem/vollem CAPTURE durchführen
    
    • Elektrische Anschlüsse überprüfen
* - **Trichter wird kontinuierlich aktiviert**
  - • Schwellenwerte falsch kalibriert
    
    • Unzureichende Vibrationszeit (entlädt zu wenige Teile)
    
    • Falscher Parameter „Steps“
  - • Kalibrierung wiederholen, indem ALLE Teile für CAPTURE leer entfernt werden
    
    • Parameter „Time“ erhöhen (z. B. von 500 ms auf 700 ms)
    
    • „Steps“ neu berechnen, indem die tatsächlichen Zyklen gezählt werden
* - **Hopper-Test immer rot (aktiviert sich nicht)**
  - • Zu viele Komponenten im Bereich während der Kalibrierung
    
    • Beleuchtung zwischen Kalibrierung und Test verändert
    
    • Reflexionen/Schatten im Kontrollbereich
  - • Kalibrierung mit der korrekten Mindestanzahl an Teilen wiederholen
    
    • Kalibrierung und Test bei stabiler Beleuchtung durchführen
    
    • Bereich neu positionieren und Zonen mit Reflexionen ausschließen
* - **Hopper-Test immer grün (wird immer aktiviert)**
  - • Kontrollbereich umfasst irrelevante Bereiche
    
    • Kalibrierung im leeren Zustand mit vorhandenen Teilen durchgeführt
    
    • Expression Builder nicht korrekt berechnet
  - • Kontrollbereich enger definieren
    
    • CAPTURE im leeren Zustand wiederholen und sicherstellen, dass der Bereich vollständig sauber ist
    
    • Erneut auf AUTO klicken, um Mean und Std Dev neu zu berechnen
* - **Ungleichmäßiger Komponentenstrom**
  - • Falsche Berechnung der Vibrationszeit
    
    • Zu hohe Anfangsbeladung, die die Payload überschreitet
  - • Überprüfen Sie die Vibrationsberechnung auf Basis der Anfangsbeladung
    
    • Stellen Sie sicher, dass die Beladung die Payload des Trichters nicht überschreitet
```

(troubleshooting_robot_setup)=
## Fehlerbehebung für den Abschnitt Robot Setup

```{warning}
**Verbindungsdiagnose fehlgeschlagen**

Wenn der Roboter keine Verbindung herstellen kann:

**Grundlegende Überprüfungen**:
1. FlexiVision One Server online (grüne Anzeige)
2. Korrekte IP-Adresse im Roboterprogramm
3. Korrekter Port im Roboterprogramm (entspricht dem von FlexiVision One)
4. Ethernet-Kabel korrekt angeschlossen

**Netzwerküberprüfungen**:
1. Ping vom VisionController zum Roboter:
   - Öffnen Sie die Eingabeaufforderung auf VisionController
   - `ping <IP_ROBOT>` (z. B.: `ping 192.168.1.10`)
   - Falls fehlgeschlagen: Problem mit dem physischen Netzwerk/der IP-Konfiguration

2. Ping vom Roboter zum VisionController (sofern die Ping-Funktion auf dem Roboter verfügbar ist)

3. Überprüfen Sie, ob sich Roboter und VisionController im selben Subnetz befinden

**Firewall-Prüfungen**:
1. Windows-Firewall vorübergehend für Testzwecke deaktivieren
2. Falls dies funktioniert: Firewall-Problem → Ausnahme konfigurieren

**Roboterüberprüfungen**:
1. Richtige Syntax des TCP/IP-Verbindungsbefehls überprüfen (siehe Roboterhandbuch)
2. Verbindungs-Timeout prüfen (ggf. erhöhen)
3. Netzwerkberechtigungen auf der Robotersteuerung überprüfen
```

```{note}
**Verbindungsstabilisierung**

Falls die Verbindung häufig unterbrochen wird:

1. Überprüfen Sie die Qualität des Ethernet-Kabels (verwenden Sie mindestens Cat6)
2. Vermeiden Sie zu lange Kabel
3. Stellen Sie sicher, dass kein übermäßiger Netzwerkverkehr im selben Subnetz vorliegt; dazu können Sie Programme wie Wireshark oder TCP Dump verwenden
4. Stellen Sie eine stabile Stromversorgung des VisionControllers sicher
5. Überprüfen Sie die Windows-Protokolle auf Netzwerkfehler

Wenn das Problem weiterhin besteht, wenden Sie sich für eine eingehende Analyse an den technischen Support.
```
```{warning}
**Falsche Befehlssyntax**

Wenn FlexiVision One mit „Invalid command“ antwortet:

1. Überprüfen Sie die genaue Syntax des Befehls (Groß-/Kleinschreibung, Unterstriche usw.)
2. Achten Sie darauf, nach jedem Befehl das Abschlusszeichen CHR(13) zu senden
3. Fügen Sie keine zusätzlichen Leerzeichen am Anfang oder Ende des Befehls ein
4. Überprüfen Sie im Meldungsprotokoll des Abschnitts „Robot Setup“ den Befehl, den FlexiVision One empfangen hat

Richtige vs. falsche Beispiele:
- ✅ `start_Locator` (mit Unterstrich, Kleinbuchstaben)
- ❌ `Start_Locator` (falsche Großbuchstaben)
- ❌ `start Locator` (Leerzeichen statt Unterstrich)
- ❌ `startLocator` (Unterstrich fehlt)

Eine vollständige und korrekte Liste der Befehle finden Sie unter [Protocollo TCP/IP](protocollo).
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Roboter verbindet sich nicht mit FlexiVision One**
  - • IP-Adresse des Roboters befindet sich nicht im selben Subnetz wie der VisionController
    
    • TCP/IP-Port nicht konfiguriert
    
    • Firewall des VisionControllers blockiert die Kommunikation
    
  - • Richtiges Subnetz in „Robot Setup“ überprüfen und konfigurieren
    
    • TCP/IP-Port konfigurieren (typischerweise 5000 oder je nach Roboter)
    
    • Firewall für Testzwecke deaktivieren
    
    • Im [Protocol Setup](../QUICKSTART/SETUP/15_Protocol_Setup.md) ein mit dem Roboter kompatibles Protokoll auswählen
* - **Roboter fährt zu falschen Positionen**
  - • Roboterkalibrierung nicht oder nicht korrekt durchgeführt
    
    • Falscher Roboter-Frame/Tool
    
    • Falscher Greifer-Offset
    
    • Falsche Koordinaten beim Modell-Setup gespeichert
  - • Vollständige Roboterkalibrierung durchführen
    
    • Ausgewählten Frame und Tool am Roboter überprüfen
    
    • Wiederholen Sie die Kalibrierung des Pick-Roboters mit den korrekten Koordinaten
    
    • Führen Sie das Modelltraining erneut durch und speichern Sie dabei die genauen Koordinaten
* - **Verbindung zum Roboter nicht möglich**
  - • Roboter ausgeschaltet
    
    • Ethernet-Kabel nicht angeschlossen
    
    • Roboter und VisionController in unterschiedlichen Subnetzen

  - • Roboter einschalten und in den Automatikmodus versetzen
    
    • Physische Ethernet-Verbindung zwischen Roboter und VisionController überprüfen
    
    • Roboter und VisionController im selben Netzwerk konfigurieren
```

