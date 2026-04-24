(cablaggio)=
# **Verkabelung und Anschlüsse**
Übersichtsbild der elektrischen Anschlüsse 
Typ:  
![Pan Coll](../../../../_shared/media/images/panoramicacollegamenti.png)
```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **Von**
  - **Nach**
  - **Verbindung**

* - Stromnetz
  - FlexiBowl
  - Versorgung 110/220 Vdc

* - Stromnetz
  - Roboter
  - Versorgung gemäß den Spezifikationen des vorhandenen Roboters

* - Stromnetz
  - Kamera
  - Versorgung 24 Vdc

* - Stromnetz
  - Beleuchtung (Licht)
  - Versorgung 24 Vdc

* - Stromnetz
  - Hopper Controller
  - Versorgung 110/220 Vdc

* - Hopper Controller
  - Hopper
  - Versorgung und Signal

* - Roboter
  - Hopper Controller
  - Digitale I/O

* - VisionController
  - Kamera
  - Ethernet TCP

* - VisionController
  - FlexiBowl
  - Ethernet TCP

* - VisionController
  - Roboter
  - Ethernet TCP
```

## Geführtes Verkabelungsverfahren

```{list-table} 
:header-rows: 1

* - **Schritt**
  - **Aktion**
* - 1
  - Die Versorgung des FlexiBowl® anschließen.  
    [🔗 Für die Versorgungsspezifikationen das Handbuch heranziehen](http://link-al-manuale.com)
* - 2
  - Das [Hirose 24V Versorgungskabel](cavo) an die Kamera anschließen.
* - 3
  - Den FlexiBowl® mit einem Ethernet-Kabel an den VisionController anschließen.
* - 4
  - Die Kamera mit einem Ethernet-Kabel an den VisionController (PC) anschließen.
* - 5
  - Den Roboter mit einem Ethernet-Kabel an den VisionController anschließen.
* - 6
  - Die Druckluft an den FlexiBowl® anschließen.  
    [🔗 Für die Pneumatikspezifikationen das Handbuch heranziehen](http://link-al-manuale.com)
* - 7
  - Falls vorhanden, den Hopper an seinen Controller anschließen
* - 8
  - Falls vorhanden, den Roboter an den Hopper-Controller anschließen (Digitale I/O)
* - 9 
  - Falls vorhanden, den Hopper-Controller versorgen (110/220 V gemäß der beim Kauf der Hopper-Vibrationsbasis gewählten Option)
* - 10
  - Den AC-Schalter des FlexiBowl® einschalten (Position "I"). Die READY-LED ist **ON**.
* - 11
  - Alle anderen Geräte einschalten
```
(cablaggio_illuminatore)=
## Verkabelung der Beleuchtung

![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parameter
  - Anforderung / Aktion
* - **Spannung**
  - 24V DC (±10%). Mindestbetriebsspannung: 20V DC am Lichteingang.
* - **Steckverbinder**
  - M12 Male. 
    :::{note}
      Zum Anschließen des toplight kann auch das zugehörige [Versorgungskabel](cavoalimtoplight) erworben werden. 
    :::
* - **Steckerbelegung**
  - Pin 1: +24V (braun) — Pin 3: GND (blau) — Pin 4: STROBE PNP (schwarz)
* - **STROBE-Modus (PNP)**
  - Von 5V bis 24V für 100% Einschaltung. Von 0V bis 1V für 100% Ausschaltung.
* - **DAUERBETRIEB**
  - Pin 1 (+24V) und Pin 3 (GND) verbunden; Pin 4 (PNP) mit Pin 1 verbunden.
* - **Spannungsabfall (M12-Kabel, 10m)**
  - 1.15V @ 5A — 2.3V @ 10A — 3.5V @ 15A — 4.6V @ 20A (max 20A)
* - **Schirmung**
  - Geschirmte Kabel verwenden, um elektromagnetische Störungen (EMI) zu reduzieren.
```
```{warning}
**Elektrische Sicherheit**

- Die angegebenen Versorgungsspannungen und Anschlussklemmen einhalten.
- Das Produkt nicht verändern oder demontieren.
- Das Gerät nicht anschließen oder reinigen, wenn es unter Spannung steht.
- Nicht direkt in die Lichtquelle blicken.
```



