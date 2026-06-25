(specifiche_tecniche)=
# **Detaillierte technische Daten zum FlexiVision One**

Dieser Abschnitt enthält die vollständigen technischen Daten des FlexiVision One-Systems, einschließlich Details zur Industriekamera, zum VisionController, zum Kalibrierungsraster, zu den Kommunikationsprotokollen und zu den Hardwarekonfigurationen.

---
(specifiche_camera)=
## Kamera

```{figure} ../../../../_shared/media/images/camera_nuova.png
  :alt: Camera FlexiVision One CAM-CIC-5000-20G-1
  :align: center
  :width: 70%
```

Das FlexiVision One-System verwendet hochauflösende Kameras mit Gigabit-Ethernet-Schnittstelle, um eine schnelle Bildaufnahme und präzise Bauteilerkennung zu gewährleisten.

### *Elektrische Spezifikationen*
```{list-table}
:header-rows: 1
:widths: 40 60

* - **Merkmal**
  - **Spezifikationen**
* - Modell
  - CAM-CIC-5000-20G-1
* - Effektive Pixel
  - 5 MP 12448 × 2048
* - SNR
  - \>38 dB
* - Dynamic Range
  - 70 dB
* - GPIO
  - 6-poliger Hirose-Stecker: 1 optoisolierter Eingang, 1 optoisolierter Ausgang, 1 konfigurierbarer I/O-Anschluss ohne optische Isolierung
* - Bildformat
  - Mono8 / 10 / 10Packed
* - Binning 
  - Unterstützt
* - Gain
  - X1 ~ X32
* - Bereich
  - 0 bis 4, unterstützt LUT
* - Belichtungszeit
  - 34.23 μS ~ 1S
* - Triggermodus
  - Software / Hardware / Freilauf
* - Bildpuffer
  - 256 MB
* - Benutzereinstellungen
  - Unterstützt zwei Sätze benutzerdefinierter Konfigurationen
* - Stromversorgung
  - PoE / DC über Hirose-Anschluss, mit 12 V oder 24 V Spannung
* - Leistungsaufnahme
  - 12V ≈ 3.2 W
* - Objektivanschluss
  - C-mount
* - Betriebstemperatur
  - -30°C ~ +50°C
* - Lagertemperatur
  - -30°C ~ +80°C
* - Zertifizierungen
  - CE, UL, FCC, RoHS
* - Auflösung
  - 2448 x 2048
* - Pixelgröße
  - 3.45 × 3,45 μm
* - Sensor
  - IMX264 CMOS Global Shutter
* - Sensorgröße
  - 2/3"
* - Bildfrequenz
  - 24 fps
* - Bittiefe
  - 12 bit
* - Schnittstelle
  - GigE, POE
```

### *GPIO-Anschluss (Hirose 6-polig)*

```{figure} ../../../../_shared/media/images/Pin_Cam.png
:alt: Steckverbinder GPIO Hirose 6-pin
:align: center
:width: 70%

Rückansicht der Kamera mit Anschlüssen
```

```{list-table}
:header-rows: 1
:widths: 10 20 70

* - **Pin**
  - **Signal**
  - **Beschreibung**
* - 1
  - Power
  - Stromeingang DC 12V oder 24V
* - 2
  - Line1
  - Optoisolierter Eingang
* - 3
  - Line2
  - GPIO 1I/O, per Software konfigurierbar, ohne Optoisolierung
* - 4
  - Line0
  - Optoisolierter Ausgang
* - 5
  - IO GND
  - Optoisolierte Masse
* - 6
  - GND
  - Masse
```

```{warning}
**Erforderliche Netzwerkanforderungen**

Die Gigabit-Ethernet-Schnittstelle ist obligatorisch und erfordert eine kompatible Netzwerkinfrastruktur: einen Gigabit-Ethernet-Switch und Ethernet-Kabel mindestens der Kategorie Cat6 oder Cat7 mit S/STP-Abschirmung.

Die Nichtbeachtung dieser Anforderung beeinträchtigt die Funktionsfähigkeit der Kamera vollständig. Stellen Sie sicher, dass alle Netzwerkkomponenten (Kabel, Switches, Anschlüsse) den GigE-Standard unterstützen.
```

### *Stromversorgungsmethoden*

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - **Methode**
  - **Beschreibung**
  - **Anforderungen**
* - **PoE**
  - Stromversorgung und Daten über ein einziges Ethernet-Kabel. Leistungsaufnahme 3,2 W bei 12 Vdc.
  - Erfordert einen PoE-Injektor oder einen PoE-kompatiblen Switch gemäß IEEE 802.3af/at
* - **Externes Kamerakabel im Lieferumfang enthalten**
  - Externe Gleichstromversorgung über 6-poligen Hirose-Stecker mit 112 V oder 24 V. Im Bausatz enthalten.
  - Separates Ethernet-Kabel nur für Daten erforderlich
```

```{tip}
**Welche Methode soll gewählt werden?**

- **PoE**: ideal für saubere Installationen mit nur einem Kabel, erfordert jedoch spezielle Netzwerkhardware
- **Externe Stromversorgung**: flexiblere Standardlösung, für die meisten Anwendungen empfohlen
```
(Kabel)=
### *Stromversorgungskabel*
```{figure} ../../../../_shared/media/images/Cavo_Specfiche.png
:alt: Spezifikationen des Kamerastromkabels
:align: center
:width: 100%

Spezifikationen des Kameranetzkabels
```
```{list-table}
:widths: 30 70
:header-rows: 1

* - Parameter
  - Wert

* - **Beschreibung**
  - 10 Meter langes I/O-Kabel, HRS6P-Stecker

* - **Kompatibilität**
  - Kameras der CIC-Serie

* - **Länge**
  - 10 Meter (133')

* - **Stecker 1P1**
  - Push/Pull 6P RECP Shell SZ 7 Buchse

* - **Leiterquerschnitt**
  - 22 AWG

* - **Kabeltyp**
  - Geschirmt, 3 verdrillte Paare, flexibel

* - **Kabelfarben**
  - Pin 1: Braun, Pin 2: Grün, Pin 3: Rosa, Pin 4: Gelb, Pin 5: Grau, Pin 6: Weiß

* - **Abschirmung**
  - Abschirmung auf allen Leitern

* - **Konformität**
  - UL/CSA und RoHS
```



### *Physikalische Spezifikationen und Abmessungen*
![Dimensioni Camera](../../../../_shared/media/images/Dimensioni_Cam.png)
```{list-table}
:header-rows: 1
:widths: 40 60

* - **Merkmal**
  - **Wert**
* - Breite × Höhe 1Gehäuse
  - 29 × 29 mm
* - Tiefe 1Gehäuse
  - 42,0 mm
* - Gesamttiefe 1einschließlich rückseitigem Anschluss
  - 48,9 mm
* - Frontüberstand 1Objektivfassung
  - 12.60 mm
* - Achsabstand der seitlichen Befestigungslöcher 1M2
  - 20,0 × 23,7 mm
* - Vordere Befestigungslöcher
  - 2× M2 Tiefe 3 mm
* - Seitliche Befestigungslöcher
  - 4× M2 Tiefe 3,5 mm + 3× M3 Tiefe 3,5 mm
* - Gewicht
  - 88 g
```
---
(specifiche_obiettivo)=
## Objektiv
```{figure} ../../../../_shared/media/images/Ottica_000046.png
:alt: Camera FlexiVision One CAM-CIC-5000-20G-1
:align: center
:width: 50%
```
```{dropdown} Obiettivo 35mm
| Parameter | Referenzvergrößerung | M.O.D. |
|------------|-----------------------------|--------|
| **Linsentyp** | CCTV Lens | CCTV Lens |
| **Fokusposition** | Reference Magnification | M.O.D. |
| **Vergrößerung** | 0,069 | 0,167 |
| **Brennweite (mm)** | 34,97 | 34,97 |
| **F-Zahl (Fno)** | 2,00 ~ 16,00 | 2,00 ~ 16,00 |
| **Numerische Apertur (NA)** | - | - |
| **Arbeitsabstand / Objekt (mm)** | 500,0 / 507,0 | 200,0 / 207,0 |
| **Objekt-Bild-Abstand (mm)** | 555.75 | 259.16 |
| **Mechanische Tubuslänge (mm)** | 36.30 ~ 38.20 | 36.30 ~ 38.20 |
| **Backfokus Linse (mm)** | 14.75 | 18.16 |
| **Schärfentiefe (mm)** | 35.476 | 6.336 |
| **Auflösung @550nm (µm)** | - | - |
| **Position der Hauptebene vorne / hinten. (mm)** | 37,60 / -22,61 | 37,60 / -22,61 |
| **Pupillenposition Ein-/Ausgang (mm)** | 25,22 / -41,78 | 25,22 / -41,78 |
| **Pupillendurchmesser Ein-/Ausgang (mm)** | 17,03 / 26,36 | 17,03 / 26,36 |
| **Bildwinkel 1° H × V** | 13,69 × 10,34 | 12,62 × 9,76 |
| **TV-Verzeichnung 1%** | -0,088 | -0,142 |
| **Relative Beleuchtungsstärke 1%** | 44,95 | 50.20 |
| **Gewicht (g)** | 50 | 50 |
| **Mount-Anschluss** | C-Mount | C-Mount |
| **Bildkreis (mm)** | φ11 | φ11 |
| **Maximal kompatible Kamera** | 2/3" | 2/3" |
```
```{dropdown} Obiettivo 25mm
| Parameter | Referenzvergrößerung | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Linsentyp** | CCTV Lens | CCTV Lens |
| **Fokusposition** | Reference Magnification | M.O.D. |
| **Vergrößerung** | 0,049 | 0,152 |
| **Brennweite (mm)** | 25,00 | 25,00 |
| **F-Zahl (Fno)** | 1,60 ~ 16,00 | 1,60 ~ 16,00 |
| **Numerische Apertur (NA)** | - | - |
| **Arbeitsabstand / Objekt (mm)** | 500,0 / 510,0 | 150,0 / 160,0 |
| **Objekt-Bild-Abstand (mm)** | 553.34 | 205.92 |
| **Mechanische Tubuslänge (mm)** | 34.60 ~ 38.50 | 34.60 ~ 38.50 |
| **Backfokus Linse (mm)** | 13.75 | 16.33 |
| **Schärfentiefe @PCoC 0.04mm (mm)** | 54.223 | 5.835 |
| **Auflösung @550nm (µm)** | - | - |
| **Position der Hauptebene vorne / hinten. (mm)** | 29,42 / -12,46 | 29,42 / -12,46 |
| **Pupillenposition Ein-/Ausgang (mm)** | 18,48 / -31,94 | 18,48 / -31,94 |
| **Pupillendurchmesser Ein-/Ausgang (mm)** | 15.92 / 28.32 | 15.92 / 28.32 |
| **Bildwinkel 1° H × V** | 19.39 × 14.64 | 18.05 × 13.89 |
| **TV-Verzeichnung 1%** | -0.041 | -0.271 |
| **Relative Beleuchtungsstärke 1%** | 49.78 | 53.52 |
| **Gewicht (g)** | 50 | 50 |
| **Mount-Anschluss** | C-Mount | C-Mount |
| **Bildkreis (mm)** | φ11 | φ11 |
| **Maximal kompatible Kamera** | 2/3" | 2/3" |
```
```{dropdown} Obiettivo 16mm
| Parameter | Referenzvergrößerung | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Linsentyp** | CCTV Lens | CCTV Lens |
| **Fokusposition** | Reference Magnification | M.O.D. |
| **Vergrößerung** | 0,031 | 0,095 |
| **Brennweite (mm)** | 16,16 | 16,16 |
| **F-Zahl (Fno)** | 1,60 ~ 16,00 | 1,60 ~ 16,00 |
| **Numerische Apertur (NA)** | - | - |
| **Arbeitsabstand / Objekt (mm)** | 500,0 / 507,0 | 150,0 / 157,0 |
| **Objekt-Bild-Abstand (mm)** | 554.26 | 205.30 |
| **Mechanische Tubuslänge (mm)** | 35.50 ~ 37.00 | 35.50 ~ 37.00 |
| **Backfokus Linse (mm)** | 12.16 | 13.20 |
| **Schärfentiefe @PCoC 0.04mm (mm)** | 131.893 | 14.387 |
| **Auflösung @550nm (µm)** | - | - |
| **Position der Hauptebene vorne / hinten. (mm)** | 28,44 / -4,50 | 28,44 / -4,50 |
| **Pupillenposition Ein-/Ausgang (mm)** | 18,85 / -28,07 | 18,85 / -28,07 |
| **Pupillendurchmesser Ein-/Ausgang (mm)** | 10.18 / 25.02 | 10.18 / 25.02 |
| **Bildwinkel 1° H × V** | 30.37 × 22.92 | 29.62 × 22.39 |
| **TV-Verzeichnung 1%** | -0.472 | -0.674 |
| **Relative Beleuchtungsstärke 1%** | 32.75 | 36.61 |
| **Gewicht (g)** | 50 | 50 |
| **Anschluss (Mount)** | C-Mount | C-Mount |
| **Bildkreis (mm)** | φ11 | φ11 |
| **Maximal kompatible Kamera** | 2/3" | 2/3" |
```
```{dropdown} Obiettivo 12mm
| Parameter | Referenzvergrößerung | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Linsentyp** | CCTV Lens | CCTV Lens |
| **Fokusposition** | Reference Magnification | M.O.D. |
| **Vergrößerung** | 0,023 | 0,075 |
| **Brennweite (mm)** | 12,00 | 12,00 |
| **F-Zahl (Fno)** | 1,80 ~ 16,00 | 1,80 ~ 16,00 |
| **Numerische Apertur (NA)** | - | - |
| **Arbeitsabstand / Objekt (mm)** | 500,0 / 505,6 | 150,0 / 155,0 |
| **Objekt-Bild-Abstand (mm)** | 559.55 | 209.55 |
| **Mechanische Tubuslänge (mm)** | 39.20 ~ 40.10 | 39.20 ~ 40.10 |
| **Backfokus Linse (mm)** | 12.23 | 12.84 |
| **Schärfentiefe @PCoC 0.04mm (mm)** | 277.576 | 28.121 |
| **Auflösung @550nm (µm)** | - | - |
| **Position der Hauptebene vorne / hinten. (mm)** | 17,71 / -0,05 | 17,71 / -0,05 |
| **Pupillenposition Ein-/Ausgang (mm)** | 11,68 / -12,18 | 11,68 / -12,18 |
| **Pupillendurchmesser Ein-/Ausgang (mm)** | 6.67 / 13.41 | 6.67 / 13.41 |
| **Bildwinkel 1° H × V** | 40.54 × 30.77 | 39.40 × 30.05 |
| **TV-Verzeichnung 1%** | -0.983 | -0.905 |
| **Relative Beleuchtungsstärke 1%** | 40.64 | 42.64 |
| **Gewicht (g)** | 60 | 60 |
| **Mount-Anschluss** | C-Mount | C-Mount |
| **Bildkreis (mm)** | φ11 | φ11 |
| **Maximal** kompatible Kamera | 2/3" | 2/3" |
```
---
(specifiche_VC)=
## VisionController
```{figure} ../../../../_shared/media/images/VisionController.png
:alt: VisionController FlexiVision One
:align: center
:width: 80%
```

Das FlexiVision One-System läuft auf einem Industrie-PC (VisionController), der als Hauptsteuerung für die Bildverarbeitungssoftware dient. ARS liefert den VisionController bereits vorkonfiguriert und getestet mit der installierten FlexiVision One-Software.

### *Elektrische Spezifikationen*

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Merkmale**
  - **Spezifikationen**
* - CPU
  - Intel Core i3-1115G4 1.7 14.1 GHz
* - Arbeitsspeicher (RAM)
  - 8G DDR4 3200 MHz
* - Speicher
  - 256G 
* - TPM
  - TPM 2.0
* - Betriebssystem
  - Win11 LTSC 2024
* - Ein-/Aus-Taste
  - Ja (Frontplatte mit Kontrollleuchte)
* - Ethernet-Anschlüsse
  - **i3/i7:** 3× Gb LAN
* - USB-Anschlüsse
  - 6× USB 3.0 TypA
* - Videoausgang
  - 2× HDMI 
* - Audio
  - Line Out + MIC (2-in-1-Buchse)
* - Stromversorgung (V DC)
  - 12 ~ 32 V DC
* - Betriebstemperatur
  - 1°C ~ +50°C
* - Lagertemperatur
  - -20°C ~ +65°C
* - Luftfeuchtigkeit
  - <90% (nicht kondensierend)
* - Gehäusematerial
  - Aluminiumlegierung + Stahl
* - Schutzart
  - IP20
* - Installationsmethode
  - Wandmontage (DIN-Schiene optional)
* - Leistungsaufnahme
  - 25 W
* - Abmessungen (W × H × T)
  - 59.8 × 200 × 119,5 mm
* - Gewicht
  - 2 kg
* - Zertifizierungen
  - CE, UL
```

### *PC-Anschlüsse*
```{figure} ../../../../_shared/media/images/Spec_Elettriche_PC.png
:alt: Schema elettrico VisionController
:align: center
:width: 50%
```


```{list-table}
:header-rows: 1
:widths: 10 25 65

* - **Ref.**
  - **Anschluss**
  - Beschreibung
* - A
  - Einschaltknopf
  - Ein- und Ausschalten des Geräts
* - B
  - ETH 10/100/1000 Mbit – RJ45 (LAN 1)
  - Gigabit-Ethernet-Anschluss 1
* - C
  - ETH 10/100/1000 Mbit – RJ45 (LAN 2)
  - Gigabit-Ethernet-Anschluss 2
* - D
  - Serieller Anschluss (RS232) COM1
  - Serielle Schnittstelle RS232 COM1
* - E
  - Serieller Anschluss (RS232) COM2
  - Serielle Schnittstelle RS232 COM2
* - F
  - Stromversorgungsanschluss
  - Stromversorgungseingang 12–32 V DC (3-polige Klemmleiste)
* - G
  - Audioausgang + MIC (3,5-mm-Klinkenstecker)
  - 1× Line-Audioausgang + Mikrofoneingang (3,5-mm-Klinkenstecker)
* - H
  - 6× USB-A
  - USB-Anschlüsse (USB 3.0 Typ A für i3/i7-Versionen)
* - I
  - Videoanschluss 2
  - **B2B12/B2B14:** HDMI 2 — **B2B15/B2B16:** DisplayPort
* - L
  - HDMI-Anschluss 1
  - HDMI-Videoausgang 1
* - M
  - ETH 10/100/1000 Mbit - RJ45 1LAN 3
  - Gigabit-Ethernet-Anschluss 3
```
### *Physikalische Spezifikationen*

```{figure} ../../../../_shared/media/images/dimensioni_VC.png
:alt: Dimensioni VisionController
:align: center
:width: 80%
```

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Schraubenlöcher**
  - M5
* - **Merkmal**
  - **Wert**
* - Breite (gesamt mit Halterungen)
  - 245,00 mm
* - Breite (Gehäuse)
  - 227.00 mm
* - Breite der Anschlussleiste
  - 200,00 mm
* - Höhe (gesamt mit Halterungen)
  - 123,00 mm
* - Höhe des Gehäuses
  - 120,00 mm
* - Tiefe
  - 61,10 mm
```

---
(laser)=
## Laser-Tool für die Kalibrierung 
Das Laser-Tool ist eine fortschrittliche Kalibrierungslösung, die die Genauigkeit der Speicherung des Referenzpunktes des Roboters verbessert.
Der Hauptvorteil des Lasers besteht darin, dass er keinen physischen Kontakt mit dem Kalibrierungsgitter benötigt. Der Laser fungiert als hochpräziser Zeiger und ermöglicht es dem Bediener, den Zielpunkt visuell und wiederholgenau auf dem Gitter auszurichten, wodurch ein weitaus höherer Grad an Genauigkeit erzielt wird als bei der Verwendung einer physischen Spitze. 
Diese Präzision ist für den Erfolg der Kalibrierung unerlässlich und ergänzt sich perfekt mit der Wiederholgenauigkeit, die das spezielle ARS-Kalibriergitter gewährleistet.


![Laser Kal](../../../../_shared/media/images/laser.png) 

| Merkmal| Laser-Werkzeug (Laser Tool)| Standard-Spitzenwerkzeug (Tip Tool)
|--|--|--|
| Referenzierungsmethode| Berührungslos / visueller Zeiger| Berührend / mechanische/physische Spitze
| Referenzgenauigkeit| Höchste Genauigkeit; der Bediener richtet den Punkt visuell präzise aus.| Mittel, abhängig vom Sehvermögen des Bedieners
| Benutzerfreundlichkeit| Vereinfacht den visuellen Ausrichtungsvorgang.| Erfordert größere Sorgfalt bei der Positionierung und der Vermeidung von Neigungen.
| Hauptvorteil| Ermöglicht die Speicherung des Roboter-Referenzpunkts mit höchstmöglicher Genauigkeit, was für die endgültige Genauigkeit des Pickings unerlässlich ist.| Grundlegende Methode, jedoch weniger präzise als der Laser.


```{image} ../../../../_shared/media/images/laserscomp.png
:width: 1px
:class: hidden
```
```{raw} html
<div style="display: flex; align-items: flex-start; gap: 2rem;">
  <img src="../../_images/laserscomp.png" style="width: 280px; flex-shrink: 0;" />
  <table style="border-collapse: collapse; font-size: 0.95em; align-self: center;">
    <thead>
      <tr style="background: #d0d0d0;">
        <th style="padding: 6px 16px; text-align: left;">POS.</th>
        <th style="padding: 6px 16px; text-align: left;">BESCHREIBUNG</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding: 5px 16px;">1</td><td style="padding: 5px 16px;">OBERER VERSCHLUSSDECKEL</td></tr>
      <tr><td style="padding: 5px 16px;">2</td><td style="padding: 5px 16px;">CR2032-3V-KNOPFZELLEN-BATTERIEFACH</td></tr>
      <tr><td style="padding: 5px 16px;">3</td><td style="padding: 5px 16px;">KUPPLUNGSFLANSCH</td></tr>
      <tr><td style="padding: 5px 16px;">4</td><td style="padding: 5px 16px;">KLEMME</td></tr>
      <tr><td style="padding: 5px 16px;">5</td><td style="padding: 5px 16px;">WERKZEUGKÖRPER</td></tr>
      <tr><td style="padding: 5px 16px;">6</td><td style="padding: 5px 16px;">LASER-ZEIGER</td></tr>
      <tr><td style="padding: 5px 16px;">7</td><td style="padding: 5px 16px;">FEDERDÄMPFER</td></tr>
      <tr><td style="padding: 5px 16px;">8</td><td style="padding: 5px 16px;">ABSTANDSHALTER</td></tr>
    </tbody>
  </table>
</div>
```
:::{important}
Die Halterung zum Montieren des Laser-Tools anstelle des Robotertools wird **NICHT** mitgeliefert, da sie für jeden Roboter variiert und individuell angepasst werden muss.
:::

:::{admonition} Tipp 
:class: tip 
Die Verwendung des Laser-Tools zusammen mit dem speziellen Kalibrierungsgitter von ARS stellt die robusteste und präziseste Methode für die Installation des FlexiVision One-Systems dar
:::
---
(specifiche_griglia)=
## Kalibrierungsgitter

```{figure} ../../../../_shared/media/images/griglia800.JPG
:alt: Kalibrierungsgitter
:align: center
:width: 50%
```


Eine hervorragende Kalibrierung ist die Grundvoraussetzung für die Genauigkeit des FlexiVision One-Systems. Nur eine hochpräzise Kalibrierung gewährleistet, dass die von der Kamera erfassten Koordinaten (Pixel) genau in die tatsächlichen Koordinaten des Roboters (Millimeter) umgerechnet werden, wodurch der Erfolg des Picking-Vorgangs sichergestellt wird.

### *Technische Daten des Kalibrierungsgitters*

```{dropdown} Gitter für FlexiBowl® 200 
![Gitter 200](../../../../_shared/media/images/griglia200.JPG)

```

```{dropdown} Gitter für FlexiBowl® 350 
![Gitter 350](../../../../_shared/media/images/griglia350.JPG)
```

```{dropdown} Gitter für FlexiBowl® 500 
![Gitter 500](../../../../_shared/media/images/griglia500.JPG)
```

```{dropdown} Gitter für FlexiBowl® 650 
![Gitter 650](../../../../_shared/media/images/griglia650.JPG)
```

```{dropdown} Gitter für FlexiBowl® 800 
![Gitter 800](../../../../_shared/media/images/griglia800.JPG)
```

```{dropdown} Gitter für FlexiBowl® 1200 
![Gitter 1200](../../../../_shared/media/images/griglia1200.JPG)
```


Ausführliche Informationen zu Kalibrierungsverfahren finden Sie im Abschnitt [Kamerakalibrierung](../QUICKSTART/SETUP/14_calibrazione_camera.md).

---
## Übersicht über die Anschlüsse

![Panoramica Collegamenti](../../../../_shared/media/images/panoramicacollegamenti.png)

*Vollständischer Anschlussplan des FlexiVision One-Systems mit Roboter und FlexiBowl®*

```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **Von**
  - **Nach**
  - **Anschluss**

* - Stromnetz
  - FlexiBowl®
  - Stromversorgung 110/230 Vac

* - Stromnetz
  - Roboter
  - Stromversorgung gemäß den Spezifikationen des Roboters in Ihrem Besitz

* - Stromnetz
  - Kamera
  - 24 Vdc-Stromversorgung

* - Stromnetz
  - 1-Licht-Beleuchtung
  - 24 Vdc-Stromversorgung

* - Stromnetz
  - Trichtersteuerung
  - Stromversorgung 110/230 Vac

* - Trichtersteuerung
  - Trichter
  - Stromversorgung und Signal

* - Roboter
  - Trichtersteuerung
  - Digitale I/O

* - VisionController
  - Kamera
  - Ethernet TCP

* - VisionController
  - FlexiBowl®
  - Ethernet TCP

* - VisionController
  - Roboter
  - Ethernet TCP
```

Detaillierte Schaltpläne finden Sie im Abschnitt [Verkabelung und Anschlüsse](cablaggio).


---


## Optionale Komponenten

Separat erhältliche Zusatzkomponenten:


:::{card} Toplight
:link: toplight
:link-type: ref
:class-card: shadow
:::

:::{card} Toplight Stromkabel
:link: cavoalimtoplight
:link-type: ref
:class-card: shadow
:::

:::{card} Hintergrundbeleuchtung
:link: backlight
:link-type: ref
:class-card: shadow
:::

:::{card} Switch
:link: switch
:link-type: ref
:class-card: shadow
:::

:::{card} Display
:link: display
:link-type: ref
:class-card: shadow
:::


