# **Glossar** 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Begriff
  - Definition
* - **Accept Threshold**
  - Mindestähnlichkeitsschwelle (Wert 0,0–1,0), damit ein erkanntes Objekt vom Musterabgleich akzeptiert wird. Typische Werte: 0.70–0.90.
* - **Air-blow**
  - Optionales Pneumatikmodul zur Trennung der Komponenten auf der Scheibe mittels Druckluftstößen. Erfordert eine Versorgungsdruck von 5–6 bar.
* - **Artefakt**
  - Fehler im aufgenommenen Bild, der durch elektromagnetische Störungen, Probleme mit der Verkabelung oder Fehlfunktionen des Sensors verursacht wird.
* - **Kamerakalibrierung**
  - Korrelation von Pixeln und realen Koordinaten mittels Kalibrierungsziel mit bekanntem Muster. Berechnet die intrinsischen und extrinsischen Parameter der Kamera.
* - **Clearance**
  - Analyse der Verteilung von Graustufen über einen bestimmten Bereich. Wird verwendet, um das Vorhandensein/Fehlen von Objekten zu erkennen (Greifersteuerung, freier Bereich).
* - **POE-Kamera**
  - Industriekamera, die über ein einziges Ethernet-Kabel mit Strom versorgt und angeschlossen wird. Standard: IEEE 802.3af (15,4 W) oder 802.3at (30 W).
* - **CAPTURE**
  - Softwarebefehl zur Erfassung von Referenzbildern der leeren und vollen Scheibe, die für die automatische Berechnung der Schwellenwerte des Trichters erforderlich sind.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Geometrische Kategorien von Komponenten im FlexiBowl® Wizard. *FLAT*: flache Formen (Unterlegscheiben, Dichtungen). *CYLINDRICAL*: zylindrische Formen (Stifte, Schrauben). *COMPLEX*: unregelmäßige oder asymmetrische Geometrien.
* - **Arbeitsabstand**
  - Optimaler Abstand zwischen Linse und Scheibenoberfläche. In der Regel 950-1000 mm in Standardkonfigurationen.
* - **Optische Verzerrung**
  - Geometrische Verzerrung des Bildes durch das Objektiv. Wird bei der Kamerakalibrierung automatisch kompensiert.
* - **Belichtungszeit**
  - Lichtempfangszeit des Kamerasensors. Gemessen in μs oder ms; wirkt sich direkt auf die Bildqualität in der Produktion aus.
* - **Feature Threshold**
  - Schwellenwert für die Erkennung von Merkmalen (Kanten, Linien) während des Modelltrainings. Typische Werte: 0.3–0.8.
* - **FlexiBowl®**
  - Zuführsystem mit vibrierender Drehscheibe zur zufälligen Positionierung und Ausrichtung von Bauteilen für die Aufnahme durch einen Roboter.
* - **FlexiBowl® Wizard**
  - Assistent zur automatischen Berechnung der optimalen FlexiBowl®-Parameter basierend auf der Geometrie und dem Verhalten der Bauteile.
* - **Flip**
  - Pneumatischer Impuls unter der Scheibe zur Neupositionierung der Bauteile. Konfigurierbar über *Flip Count* (Anzahl der Impulse) und *Flip Delay* (Intervall in ms zwischen den Impulsen).
* - **Grab Train Image**
  - Software-Befehl zur Erfassung des Bildes, das für das Training eines neuen Modells verwendet werden soll.
* - **Gripper Offset**
  - Korrekturvektor (ΔX, ΔY, ΔRZ), der den Versatz zwischen dem optischen Zentrum des Bildverarbeitungssystems und dem Greifer TCP ausgleicht.
* - **Hotspot**
  - Bereich der direkten Lichtreflexion im Bild. Er erscheint als überbelichteter Bereich und kann die Erkennung beeinträchtigen.
* - **Linse**
  - Optische Komponente der Kamera. Sie muss mit Metall-auf-Metall-Kontakt verschraubt werden; die Brennweite (z. B. 16 mm, 25 mm) bestimmt das Sichtfeld bei der Arbeitsdistanz.
* - **Modell**
  - Geometrische Vorlage des in der Trainingsphase erstellten Bauteils. Jedes Rezept unterstützt bis zu 8 Modelle pro FlexiBowl®.
* - **Modellursprung**
  - Referenzpunkt auf dem Bauteil, der als Mittelpunkt des Koordinatensystems für die Positionsberechnung dient. Entspricht in der Regel dem Greif-TCP.
* - **Orthogonalität**
  - Rechtwinkligkeit der Kamera zur Scheibe (Toleranz ±1°). Überprüfbar mit Präzisionswasserwaage.
* - **Pattern Matching**
  - Algorithmus, der die Bauteile im Bild lokalisiert, indem er sie mit dem während der Trainingsphase gespeicherten Referenzmodell vergleicht.
* - **Protokoll**
  - Kommunikationsformat zwischen VisionController und Roboter. Legt die Struktur der Nachrichten, die Reihenfolge der Koordinaten und die Maßeinheiten fest.
* - **Rezept**
  - XML-Datei, die alle Konfigurationsparameter des Systems enthält: Vorlagen, Schwellenwerte, Kalibrierungen, FlexiBowl®- und Roboter-Setup.
* - **Region Search**
  - Rechteckiger Bereich im Bild, in dem der Musterabgleich die Suche durchführt. Reduziert die Verarbeitungszeiten und erhöht die Genauigkeit.
* - **ROI (Region of Interest)**
  - Rechteckiger Bereich, der das Bauteil im Bild während des Modelltrainings abgrenzt.
* - **RZ / Drehung Z**
  - Drehwinkel um die Z-Achse, der dem Roboter zur Ausrichtung des Bauteils mitgeteilt wird. Angegeben in Grad (0-360°).
* - **Score**
  - Index der Ähnlichkeit (0.0-1.0) zwischen dem Modell und dem erkannten Objekt. Bestimmt die Zuverlässigkeit der Erkennung.
* - **Greifer-Umriss-Simulatoren**
  - Physische Objekte, die während des Trainings um das Bauteil herum positioniert werden, um die vom Greifer bei der Aufnahme eingenommenen Bereiche aus dem Modell auszuschließen.
* - **Steps**
  - Anzahl der Bewegungen der FlexiBowl®, die erforderlich sind, damit die Komponenten aus dem Sichtbereich in den Entladebereich des Trichters gelangen. 
* - **Subnet**
  - Subnetz, das FlexiBowl® und VisionController für die TCP/IP-Kommunikation gemeinsam nutzen müssen (z.B. 192.168.1.x).
* - **Synchronize Parameters**
  - Softwarebefehl, der die Parameter an den FlexiBowl® überträgt. Nach jeder Änderung erforderlich, um die Einstellungen wirksam zu machen.
* - **Timeout**
  - Maximale Zeit, die auf eine Antwort der Kommunikation gewartet wird. Bei Überschreitung wird ein Fehler generiert.
* - **Tilt**
  - Neigung der Kamera gegenüber der horizontalen Ebene. Zulässiger Wert: 0° ± 1°.
* - **Toplight**
  - Über der Scheibe angebrachte LED-Beleuchtung, die für eine gleichmäßige Ausleuchtung von oben sorgt. Stromversorgung: 24V DC.
* - **Training**
  - Prozess zur Erstellung des Erkennungsmodells durch Auswahl der charakteristischen Merkmale des Bauteils aus einem Referenzbild.
* - **Trigger**
  - Startsignal für die Bildaufnahme. Kann softwaregesteuert (zeitgesteuert) oder hardwaremäßig (externes elektrisches Signal) erfolgen.
* - **Vision Result**
  - Ausgabe des Bildverarbeitungssystems: Koordinaten (X, Y, RZ) und Bewertung des erkannten Bauteils, die zur Aufnahme an den Roboter übertragen werden.
* - **VisionController**
  - Industriecomputer, auf dem FlexiVision One läuft, der die Kameras steuert, die Bilder verarbeitet und mit FlexiBowl® und dem Roboter kommuniziert.
```

