# **Verkabelung und Anschlüsse**
(troubleshooting_alimentazione)=
## Probleme mit der FlexiBowl®-Versorgung

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **LED READY schaltet sich nicht ein**
  - • Stromversorgung nicht korrekt angeschlossen  
    
    • Der Netzschalter steht auf „O“ statt auf „I“  
    
    • Beschädigtes Netzkabel  
    
    • Durchgebrannte Sicherungen in der Frontblende  
  - • Überprüfen Sie den Stromanschluss gemäß der FlexiBowl®-Bedienungsanleitung  
    
    • Schalter auf Position „I“ (ON) stellen  
    
    • Kabel auf Beschädigungen überprüfen und gegebenenfalls austauschen  
    
    • Wenden Sie sich für den Austausch der Sicherung an den technischen Kundendienst  
* - **FlexiBowl® schaltet sich willkürlich aus**
  - • Lose Stromverbindung  
    
    • Elektrische Störungen  
    
  - • Stromanschlüsse festziehen  
    
    • An eine spezielle Leitung mit EMI-Filter anschließen  

```
(troubleshooting_ethernet)=
## Probleme mit der Ethernet-Verbindung

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **FlexiBowl® kommuniziert nicht mit dem VisionController**
  - • FlexiBowl® ist nicht eingeschaltet (LED READY leuchtet nicht)  
    • Das Ethernet-Kabel ist nicht richtig am FlexiBowl® und/oder am VisionController angeschlossen  
    • Ethernet-Kabel beschädigt  
    • Falsche IP-Adresse  
    • FlexiBowl® und VisionController in unterschiedlichen Subnetzen  
    • Firewall blockiert die Kommunikation  
    • Ethernet-Anschluss des VisionControllers ist defekt  
  - • Überprüfen Sie, ob die LED READY am FlexiBowl® leuchtet  
    • Überprüfen Sie den physischen Anschluss des Ethernet-Kabels an beiden Enden  
    • Kabel mit einem Kabeltester prüfen oder austauschen  
    • IP-Konfiguration im [FlexiBowl®-Setup](../QUICKSTART/SETUP/13a_FB_Setup.md) überprüfen  
    • FlexiBowl® und VisionController im selben Netzwerk konfigurieren (z. B.: 192.168.1.x)  
    • Firewall vorübergehend für Testzwecke deaktivieren  
    • Einen anderen Ethernet-Anschluss des VisionControllers ausprobieren  
* - **Unregelmäßige Verbindung**
  - • Kabel zu lang (> 100 m)  
    • Beschädigter oder falsch gecrimpter RJ45-Stecker  
    • Elektromagnetische Störungen  
  - • Die Kabellänge auf unter 100 m verkürzen oder einen Zwischenschalter verwenden  
    • Stecker oder das gesamte Kabel austauschen  
    • Abgeschirmtes Kabel (STP) fern von EMI-Quellen verwenden  
```
(troubleshooting_pneumatica)=
## Probleme mit Pneumatik (Druckluft)

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Flip funktioniert nicht oder der Impuls ist sehr schwach**
  - • Druckluft nicht angeschlossen  
    • Luftschlauch beschädigt oder verstopft  
    • Druckregler geschlossen oder auf Mindestwert eingestellt  
    
    • Unzureichender Druck (< 5 bar)  
    
    
    
    • Luftverluste im Pneumatikkreislauf  
    
    
  - • Druckluft an den FlexiBowl®-Anschluss anschließen (siehe Bedienungsanleitung)  

    • Schlauch auf Knicke/Verstopfungen überprüfen, ggf. austauschen  
    • Druckregler am Bedienfeld öffnen  
    
    • Druck auf 5–6 bar erhöhen  
    
    
    
    • Verbindungsstücke mit Seifenwasser überprüfen, festziehen oder austauschen  
    
    
* - **Air-blow funktioniert nicht**
  - • FlexiBowl® nicht mit Air-Blow-Option ausgestattet   

    • Luftbetätigte Umschalter ohne externe Stromversorgung   

    • Durchflussregler geschlossen   

    • Unzureichender Luftdruck  
  
    
    • Magnetventil defekt
  - • Überprüfen, ob bei dem bestellten FlexiBowl® im Fertigungsblatt der Eintrag Option Blow Test auf True gesetzt ist.  

    • Überprüfen, ob eine externe Druckluftversorgung vorhanden ist (Schlauch im Lieferumfang enthalten)  

    • Wenn mehrere Luftumleiter vorhanden sind, bitte überprüfen, ob der Durchflussregler an der FlexiBowl®-Seite auf einen Wert über Null eingestellt ist  

    • Luftdruck prüfen (5–6 bar)  

    
    • Anweisungen befolgen
```
(troubleshooting_connessione_camera)=
## Probleme mit der Kameraverbindung

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Kamera nicht vom VisionController erkannt**
  - • Das Ethernet-Kabel der Kamera ist nicht angeschlossen  
    
    • Kamera, die an einen Nicht-POE-Anschluss des VisionControllers angeschlossen ist  
    

    
    • Die IP-Adresse der Kamera verursacht einen Konflikt mit den IP-Adressen anderer Geräte im selben Subnetz  
    • PoE-Anschluss des VisionControllers defekt  
  - • Den physischen Anschluss des Kamerakabels überprüfen  
    • Die Kamera NUR an den POE-Anschluss des VisionControllers anschließen  
    • IP-Adresse der Kamera zurücksetzen oder eindeutige statische IP-Adresse konfigurieren  
    • Einen anderen POE-Anschluss des VisionControllers ausprobieren  
* - **Bilder der Kamera sind schwarz oder fehlen**
  - • Beleuchtung ausgeschaltet  
    • Kameraeinstellung zu niedrig  
    • Objektiv mit nicht abgenommenem Schutzdeckel  
    • Objektiv nicht installiert  
    • Kamera ohne Stromversorgung (POE nicht aktiv)  
    
     
    • Kamera defekt  
  - • Prüfen, ob die Beleuchtung eingeschaltet ist  
    • Belichtung in [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md) erhöhen  
    • Schutzkappe vom Objektiv entfernen  
    • Objektiv mit der richtigen Brennweite einsetzen  
    • Prüfen, ob die Kamera-LED leuchtet (Anzeige für POE-Betrieb)  
    • Kamera austauschen  

* - **Die Kamera schaltet sich willkürlich aus**
  - • Unzureichende POE-Stromversorgung (Leistung < Kamerabedarf)  
     
    • Kabel beschädigt  
    
    • Überhitzung der Kamera  
    
    • POE-Anschluss beschädigt  
  - • Verfügbare POE-Leistung prüfen  
    • Ethernet-Kabel austauschen  
    
    • Belüftung im Kamerabereich verbessern  
    
    • PoE-Switch oder VisionController-Anschluss austauschen  
```
(troubleshooting_connessione_toplight)=
## Verbindungsprobleme mit Toplight
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Toplight schaltet sich nicht ein**
  - • 24-V-DC-Stromversorgung nicht angeschlossen  
    
    • Beschädigtes Netzkabel  
    
    • Falsche Spannung (≠ 24V)  
    
    • Toplight defekt  
    
    • Sicherung/Schutzvorrichtung ausgelöst  
  - • 24-V-DC-Stromanschluss überprüfen  
    
    • Kabel überprüfen, bei Beschädigung austauschen  
    
    • Spannung mit Multimeter messen, muss 24 V DC (±10 %) betragen  
    
    • Toplight austauschen  
    
    • Schutzvorrichtungen im Schaltschrank überprüfen  
* - **Schwankende Helligkeit des Toplights**
  - • Instabile Stromversorgung  
    
    • Lose Verbindungen  
    
    • Unterdimensioniertes Netzteil  
    
    • Toplight am Ende der Lebensdauer  
  - • Stabilität der Versorgungsspannung prüfen  
    
    • Alle elektrischen Anschlüsse festziehen  
    
    • Stromaufnahme im Vergleich zur Nennleistung des Netzteils prüfen  
    
    • Toplight austauschen  
* - **Toplight überhitzt sich**
  - • Unzureichende Belüftung  
    
    • Zu hoher Strom  
    
    • Dauerbetrieb zu 100 %  
  - • Luftzirkulation um das Toplight verbessern  
    
    • Sicherstellen, dass die Stromaufnahme die Spezifikationen nicht überschreitet  
    
    • Wenn möglich, einen intermittierenden Arbeitszyklus implementieren  
```
(troubleshooting_multi)=
## Probleme bei Konfigurationen des Multi-Geräts
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **System mit 2–3 FlexiBowl®: Nur eines kommuniziert**
  - • FlexiBowl® ausgeschaltet  
    • IP-Adressen doppelt vergeben  
    • Kabel gekreuzt  
  - • Überprüfen, ob der FlexiBowl® eingeschaltet ist  
    • Jedem FlexiBowl® eine eindeutige IP-Adresse zuweisen (z. B.: 192.168.1.10, .11, .12)  
    • Richtige Sternverkabelung prüfen (keine Daisy-Chain)  
* - **System mit 2–3 Kameras: Nur eine erfasst**
  - • Unzureichende Stromversorgung  
    • IP-Adressen der Kameras stehen in Konflikt  
  - • Prüfen, ob die Stromversorgung zwischen 6 und 26 V liegt  
    • Eindeutige statische IP-Adresse für jede Kamera konfigurieren  
    • Alle Kameras im [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md) aktivieren  
* - **System mit 2–3 Trichtern: fehlerhafte Steuerung**
  - • Trichter in der Software nicht einzeln aktiviert  
    • Falsche Stromversorgung  
    • Falscher Kontakt zum Roboter  
  - • Jeden Trichter im [Trichter-Setup](../QUICKSTART/SETUP/13b_Hopper_Setup.md) aktivieren  
    • Stromversorgung überprüfen  
    • Kontakt zum Roboter überprüfen  
```



