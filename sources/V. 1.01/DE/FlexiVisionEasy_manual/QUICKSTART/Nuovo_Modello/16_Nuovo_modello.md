# **Erstellen von Rezepten und Modellen - Überbsicht**

Dieser Abschnitt führt den Benutzer durch den gesamten Prozess der Erstellung eines Anwendungsrezepts und der für die Erkennung und das robotergestützte Picking erforderlichen Werkstückmodelle.

```{note}
**Voraussetzungen**

Bevor Sie mit der Erstellung von Rezepten und Modellen fortfahren, stellen Sie sicher, dass:
- Alle Hardware-Einstellungen sind abgeschlossen ([Component Setup](setupcomponenti))
- Die Kamerakalibrierung wurde erfolgreich durchgeführt ([Camera Calibration](calibrazione))
- Die Roboterkalibrierung ist abgeschlossen
- Die zu erkennenden physischen Teile sind verfügbar
```

---

## Rezept vs. Modell: Grundlegende Unterschiede

Bevor wir beginnen, ist es wichtig, den Unterschied zwischen **Rezept** und **Modell** zu verstehen:

```{list-table}
   :widths: 50 50
   :header-rows: 1

   * - Was ist ein Rezept?
     - Was ist ein Modell?
   * - Der übergeordnete Sammelbegriff für die gesamte Picking-Anwendung.
     - Die spezifische Definition einer einzelnen anzuerkennenden Komponente.
   * - Beinhaltet bis zu 8 Modelle, FlexiBowl®-Parameter, Trichter und Kommunikationslogiken.
     - Umfasst Trainingsbilder, ROIs, visuelle Merkmale, Filter und Roboter-Offsets.
   * - Verwaltet Hardware-Parameter (Vibrationen, Geschwindigkeit) und Netzwerkparameter (TCP/IP-Port, Timeout).
     - Verwaltet Bildverarbeitungsparameter (Schwellenwert, Mindestwert) und Entnahmekoordinaten (Greifer).
   * - Kann mehrere Teiletypen gleichzeitig verwalten (Multi-Modell).
     - Konzentriert sich auf ein spezifisches visuelles Muster.
```


```{tip}
Ein Rezept kann bis zu 8 verschiedene Modelle enthalten, sodass der Roboter verschiedene Arten von Teilen aus derselben Anwendung erkennen und entnehmen kann, ohne die Konfiguration zu ändern.
```


---

## VÜberblick über den gesamten Prozess

Der Prozess zur Erstellung eines vollständigen und funktionsfähigen Rezepts gliedert sich in mehrere aufeinanderfolgende Phasen:

```{figure} ../../../../../_shared/media/images/newmodel4.jpg
:alt: Workflow creazione ricetta e modelli
:width: 100%
:align: center

Vollständiges Schema des Prozesses zur Rezept- und Modellerstellung
```

### *Hauptphasen*

```{list-table}
:header-rows: 1
:widths: 10 30 60

* - Phase
  - Name
  - Beschreibung
* - **1**
  - Rezepterstellung
  - Definition des Anwendungsrezepts mit Name, Typ und verwendetem FlexiBowl®
* - **2**
  - Phaysische Vorbereitung
  - Positionierung des Referenzteils im Sichtfeld
* - **3**
  - Modelltraining
  - Bildaufnahme und Erstellung des Erkennungsmusters
* - **4**
  - ROI-Definition
  - Festlegung des Suchbereichs, in dem nach den Teilen gesucht werden soll
* - **5**
  - Filtereinstellung
  - Konfiguration akzeptieren Schwellenwert und Erkennungstoleranzen
* - **6**
  - Physische Vorbereitung 
  - Picking-Simulation mit dem Roboter, um die Objekte zu positionieren, die den Platzbedarf des Greifers simulieren sollen 
* - **7**
  - Speichern der Koordinaten 
  - Speichern der Roboterkoordinaten an der Picking-Position des Referenzbauteils 
* - **8**
  - Erstellen von Freiräumen
  - Definition von Bereichen, die frei bleiben müssen (Greiferbereich, Hindernisse)
* - **9**
  - Roboterkoordinaten
  - Berechnung des Greifer-Offsets für die korrekte Entnahme
* - **10**
  - Test und Validierung
  - Überprüfung der vollständigen Funktionsweise und Speichern des Rezepts
```

---

## Leitfaden zur Navigation durch die detaillierten Abschnitte

Ausführliche Informationen zu jedem Prozessschritt finden Sie in den entsprechenden Abschnitten:

- **[Neues Rezept erstellen](nuovaricetta)** - So erstellen und konfigurieren Sie ein neues Rezept
- **[Modelltraining](nuovomodello)** - Bildaufnahme und Mustererstellung
- **[ROI-Definition und Toleranzen](roitest)** - Konfiguration des Suchbereichs und der Toleranzen
- **[Erstellen von Freiräumen](istogrammi)** - Definition der Bereiche, die frei bleiben müssen 
- **[Roboter-Pick-Kalibrierung](robotpick)** - Berechnung des Greifer-Offsets 

---

## Praktische Tipps vor dem Start

### *Materialvorbereitung*

```{tip}
**Checkliste zur Vorbereitung**

Bevor Sie mit der Erstellung von Modellen beginnen, bereiten Sie Folgendes vor:

-  Mindestens 10–20 Teile des zu erkennenden Typs (zum Testen)
-  Saubere und in gutem Zustand befindliche Teile (repräsentativ für die Produktion)
-  Simulatoren für den Platzbedarf des Greifers (es dürfen KEINE Teile desselben Typs sein, da es wichtig ist, diese nicht mit dem Referenzteil zu verwechseln.)
-  Blatt zum Notieren der Roboterkoordinaten (X, Y, RZ)
-  Leerer und sauberer FlexiBowl®
-  Hintergrundbeleuchtung/Toplight eingeschaltet
```

### *Optimale Umgebung*

```{note}
**Ideale Bedingungen für das Training**

- Stabile Beleuchtung (direktes, wechselndes Sonnenlicht vermeiden)
- FlexiBowl® stillstehend 
- Roboter in sicherer Position (darf die Aufnahme nicht stören)
- FlexiVision One-Software geöffnet und Basisrezept geladen
```

### *Häufige Fehler, die es zu vermeiden gilt*

```{error}
**Vermeiden Sie diese häufigen Fehler**

❌ **Roboterkordinaten** werden während der physischen Vorbereitung **nicht gespeichert** → Greifer-Offset kann nicht berechnet werden 

❌ **Das Teil** wird nach dem Speichern der Koordinaten **verschoben** → falscher Offset

❌ **Feature-Schwellenwert zu niedrig** → Modell zu detailliert, erkennt Oberflächenstruktur

❌ **ROI zu engl** → Teile an den Rändern werden nicht erkannt

❌ **Abstände zu klein** → Kollisionen des Greifers mit benachbarten Teilen

❌ **Nicht mit mehreren Teilen testen** → Probleme werden erst in der Produktion erkannt

Befolgen Sie die in den folgenden Abschnitten beschriebenen Schritte genau, um diese Probleme zu vermeiden.
```

---

## Unterstützung und weitere Ressourcen

```{note}
**INFO-Schaltfläche**  
In jedem der Arbeitsbereiche befindet sich oben rechts eine INFO-Schaltfläche.
Über diese Schaltfläche wird eine Schritt-für-Schritt-Anleitung aufgerufen, die auch im Video-Tutorial zu sehen ist.

- [**Umfassende Video-Tutorials**](vidtutcompleti) 
- **Technische Unterstützung**: [support@arsautomation.com](mailto:support@arsautomation.com) für Unterstützung

Bei spezifischen Problemen beim Erstellen von Vorlagen lesen Sie bitte den Abschnitt [Troubleshooting](troubleshooting).
```

---

## Nächste Schritte

Sobald Sie den Überblick über den Prozess gewonnen haben, fahren Sie mit der eigentlichen Erstellung fort:

**→ [Start: Neues Rezept erstellen](nuovaricetta)**


```{toctree}
:hidden:
17_NuovaRicetta.md
18_NuovoModello.md
19_ROI_TEST.md
20_Istogrammi.md
21_RobotPick.md
```
