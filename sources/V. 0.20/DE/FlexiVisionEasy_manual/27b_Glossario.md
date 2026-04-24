# **Glossar** 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Begriff
  - Definition
* - **Accept Threshold**
  - Mindestschwelle für die Ähnlichkeit (Score 0.0–1.0), damit ein erkanntes Objekt vom Pattern Matching akzeptiert wird. Typische Werte: 0.70–0.90.
* - **Air-blow**
  - Optionales Pneumatikmodul zur Trennung der Komponenten auf der Scheibe durch Druckluftstöße. Erfordert eine Versorgung mit 5–6 bar.
* - **Artefakt**
  - Fehler im aufgenommenen Bild, verursacht durch elektromagnetische Störungen, Verkabelungsprobleme oder Fehlfunktionen des Sensors.
* - **Kamerakalibrierung**
  - Korrelation zwischen Pixeln und realen Koordinaten mithilfe eines Kalibriertargets mit bekanntem Muster. Berechnet die intrinsischen und extrinsischen Parameter der Kamera.
* - **Clearance**
  - Analyse der Verteilung der Graustufen in einem definierten Bereich. Wird zur Erkennung der Anwesenheit/Abwesenheit von Objekten verwendet (Greiferprüfung, freier Bereich).
* - **POE-Kamera**
  - Industriekamera, die über ein einziges Ethernet-Kabel versorgt und verbunden wird. Standard: IEEE 802.3af (15.4W) oder 802.3at (30W).
* - **CAPTURE**
  - Softwarebefehl zur Aufnahme der Referenzbilder der leeren und vollen Scheibe, die für die automatische Berechnung der Hopperschwellen erforderlich sind.
* - **COMPLEX / FLAT / CYLINDRICAL**
  - Geometrische Kategorien der Komponenten im FlexiBowl Wizard. *FLAT*: flache Formen (Unterlegscheiben, Dichtungen). *CYLINDRICAL*: zylindrische Formen (Stifte, Schrauben). *COMPLEX*: unregelmäßige oder asymmetrische Geometrien.
* - **Arbeitsabstand**
  - Optimaler Abstand zwischen Objektiv und Scheibenoberfläche. In Standardkonfigurationen typischerweise 950–1000mm.
* - **Optische Verzerrung**
  - Geometrische Verformung des Bildes durch das Objektiv. Wird während der Kamerakalibrierung automatisch kompensiert.
* - **Belichtung**
  - Lichtsammelzeit des Kamerasensors. Gemessen in μs oder ms; beeinflusst direkt die Bildqualität in der Produktion.
* - **Feature Threshold**
  - Schwelle für die Merkmalsextraktion (Kanten, Linien) während des Modelltrainings. Typische Werte: 0.3–0.8.
* - **FlexiBowl**
  - Zuführsystem mit vibrierender Rotationsscheibe zur zufälligen Positionierung und Ausrichtung von Komponenten für die robotergestützte Entnahme.
* - **FlexiBowl Wizard**
  - Geführte Prozedur zur automatischen Berechnung der optimalen FlexiBowl-Parameter basierend auf Geometrie und Verhalten der Komponenten.
* - **Flip**
  - Pneumatischer Impuls unter der Scheibe zum Neupositionieren der Komponenten. Konfigurierbar über *Flip Count* (Anzahl der Impulse) und *Flip Delay* (Intervall in ms zwischen den Impulsen).
* - **Grab Train Image**
  - Softwarebefehl zur Aufnahme des Bildes, das für das Training eines neuen Modells verwendet wird.
* - **Gripper Offset**
  - Korrekturvektor (ΔX, ΔY, ΔRZ), der den Versatz zwischen dem optischen Zentrum des Bildverarbeitungssystems und dem TCP des Greifers kompensiert.
* - **Hotspot**
  - Bereich direkter Lichtreflexion im Bild. Er erscheint als überbelichteter Bereich und kann die Erkennung beeinträchtigen.
* - **Objektiv**
  - Optische Komponente der Kamera. Es muss bis zum Metall-Metall-Kontakt eingeschraubt werden; die Brennweite (z. B. 16mm, 25mm) bestimmt das Sichtfeld beim Arbeitsabstand.
* - **Model (Modell)**
  - Geometrisches Template der Komponente, das während des Trainings erstellt wird. Jede Rezeptur unterstützt bis zu 8 Modelle.
* - **Modellursprung**
  - Referenzpunkt auf der Komponente, der als Mittelpunkt des Koordinatensystems für die Positionsberechnung verwendet wird. Entspricht typischerweise dem Greif-TCP.
* - **Orthogonalität**
  - Rechtwinkligkeit der Kamera zur Scheibe (Toleranz ±1°). Kann mit einer Präzisionswasserwaage überprüft werden.
* - **Pattern Matching**
  - Algorithmus, der Komponenten im Bild lokalisiert, indem er sie mit dem während des Trainings gespeicherten Referenzmodell vergleicht.
* - **Protocol (Protokoll)**
  - Kommunikationsformat zwischen VisionController und Roboter. Definiert Nachrichtenstruktur, Reihenfolge der Koordinaten und Maßeinheiten.
* - **Recipe (Rezeptur)**
  - XML-Datei mit allen Systemkonfigurationsparametern: Modelle, Schwellen, Kalibrierungen, FlexiBowl-Setup und Roboter-Setup.
* - **Region Search**
  - Rechteckiger Bereich im Bild, in dem das Pattern Matching die Suche ausführt. Reduziert die Verarbeitungszeit und erhöht die Genauigkeit.
* - **ROI (Region of Interest)**
  - Rechteckiger Bereich, der die Komponente im Bild während des Modelltrainings begrenzt.
* - **RZ / Rotation Z**
  - Rotationswinkel um die Z-Achse, der zur Ausrichtung der Komponente an den Roboter übermittelt wird. Angegeben in Grad (0–360°).
* - **Score**
  - Ähnlichkeitsindex (0.0–1.0) zwischen dem Modell und dem erkannten Objekt. Bestimmt die Erkennungssicherheit.
* - **Greifer-Freiraum-Simulatoren**
  - Physische Objekte, die während des Trainings um die Komponente platziert werden, um die vom Greifer beim Entnehmen belegten Bereiche aus dem Modell auszuschließen.
* - **Steps**
  - Anzahl der Vibrationszyklen des Hoppers, die erforderlich sind, damit die Komponenten den Entnahmebereich erreichen. Kritischer Parameter für die Synchronisation mit dem Roboterzyklus.
* - **Subnet**
  - FlexiBowl und VisionController müssen für die TCP/IP-Kommunikation dasselbe Subnet (z. B. 192.168.1.x) verwenden.
* - **Synchronize Parameters**
  - Softwarebefehl, der die Parameter vom VisionController an den FlexiBowl überträgt. Nach jeder Änderung erforderlich, damit die Einstellungen wirksam werden.
* - **Kalibriertarget**
  - Gedrucktes geometrisches Muster (Kreise oder Schachbrett) mit bekannten Abmessungen und ebener Oberfläche, das für die Kamerakalibrierung verwendet wird.
* - **Timeout**
  - Maximale Wartezeit auf eine Antwort in der Kommunikation. Bei Überschreitung wird ein Fehler erzeugt.
* - **Tilt**
  - Neigung der Kamera gegenüber der horizontalen Ebene. Zulässiger Wert: 0° ± 1°.
* - **Toplight**
  - LED-Beleuchtung oberhalb der Scheibe, die eine gleichmäßige Beleuchtung von oben gewährleistet. Versorgung: 24V DC.
* - **Training**
  - Prozess zur Erstellung des Erkennungsmodells durch Auswahl der charakteristischen Merkmale der Komponente aus einem Referenzbild.
* - **Trigger**
  - Startsignal für die Bildaufnahme. Kann softwarebasiert (zeitgesteuert) oder hardwarebasiert (externes elektrisches Signal) sein.
* - **Vision Result**
  - Ausgabe des Bildverarbeitungssystems: Koordinaten (X, Y, RZ) und Score der erkannten Komponente, die zur Entnahme an den Roboter übertragen werden.
* - **VisionController**
  - Industriecomputer, auf dem FlexiVision One ausgeführt wird, der die Kameras verwaltet, Bilder verarbeitet und mit FlexiBowl und Roboter kommuniziert.
```

