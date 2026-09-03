# **2 FlexiBowl® und 2 Kameras**

Dieser Abschnitt beschreibt die verfügbaren Konfigurationen für den Betrieb mit **zwei FlexiBowl®** und **zwei Kameras**, die von einem einzigen VisionController FlexiVision One gesteuert werden.

---

## Überblick über die Konfiguration

In einer Konfiguration **mit 2 FlexiBowl® + 2 Kameras** umfasst das System zwei unabhängige Versorgungs- und Bildverarbeitungsstationen, die beide vom selben VisionController gesteuert werden. Jede Station besteht aus:

* 1 FlexiBowl®
* 1 Kamera mit spezieller Optik
* 1 Trichter (optional, falls vorhanden)

Die beiden Stationen kommunizieren über einen **Netzwerk-Switch** mit dem VisionController.

```{important}
Der **Switch** ist eine **obligatorische** Komponente in allen Konfigurationen mit mehreren Geräten. Ohne ihn ist es nicht möglich, mehrere FlexiBowl®-Einheiten und mehrere Kameras gleichzeitig an den VisionController anzuschließen. Technische Daten und Bestellnummern finden Sie im Abschnitt [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Diese Konfiguration unterstützt zwei Betriebsvarianten, je nach Anzahl der in der Anlage verfügbaren Roboter:
| | **Variante A** | **Variante B** |
|---|---|---|
| **Roboter** | 1 | 2 |
| **FlexiBowl®** | 2 | 2 |
| **Kameras** | 2 | 2 |
| **Betriebslogik** | Der Roboter erreicht beide Stationen | Jeder Roboter ist einer Station zugeordnet |
| **Switch erforderlich** | Ja | Ja |


---

## Variante A — 1 Roboter, 2 FlexiBowl®

![Systemübersicht 2FB2CAM1Roboter](../../../../_shared/media/images/2FB2CAM1R.png)

Bei dieser Variante arbeitet ein **einziger Roboter** an beiden Stationen. Der Roboter ist so positioniert, dass er den Picking-Bereich jedes FlexiBowl® erreichen kann, wobei er die Aufnahme zwischen den beiden Stationen je nach den empfangenen Befehlen wechselt.

Jede Station verwaltet ein eigenes, unabhängiges Rezept. Auf jeder Station kann eine **Standard-** oder **Mix-Anwendung** mit verschiedenen Komponentenmodellen innerhalb desselben Rezepts konfiguriert werden.

| Parameter | Wert |
|---|---|
| FlexiBowl® | 2 |
| Kameras | 2 |
| Roboter | 1 |
| Switch erforderlich | **Ja** |

```{important}
**Basisrezept und Rezeptverwaltung**

Wie bei der Einzelkonfiguration beginnt auch bei einer 2FB + 2CAM-Konfiguration der Prozess mit der Erstellung eines **einzigen Basisrezepts**, das die Hardware-Setups und die Kamerakalibrierung für das gesamte System enthält. Dieses Basisrezept wird dann für jede Station **dupliziert**: Jedes Duplikat bildet das Betriebsrezept dieser Station, in dem die Werkstückmodelle (bis zu 8 pro Station) erstellt werden.

Daher ist es unerlässlich, dass die Zuordnung zwischen den Geräten von Anfang an korrekt konfiguriert wird:

* **Kamera 1** → FlexiBowl® 1 (+ Trichter 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Trichter 2, falls vorhanden)

Eine fehlerhafte Zuordnung während der Einrichtung würde sich auf alle abgeleiteten Rezepte auswirken und die Teileerkennung sowie den korrekten Betrieb des gesamten Systems beeinträchtigen.
```
---

## Variante B — 2 Roboter, 2 FlexiBowl®

![Systemübersicht 2FB2CAM2Roboter](../../../../_shared/media/images/2FB2CAM2R.png)

In dieser Variante ist jeder Roboter einer einzelnen Station zugeordnet: **Roboter 1** führt die Kommissionierung am FlexiBowl® 1 durch, **Roboter 2** führt das Picking am FlexiBowl® 2 durch. Die beiden Zellen sind unabhängig voneinander und überschneiden sich nicht.

Auch bei dieser Variante unterstützt jede Station sowohl **Standard-** als auch **Mix-Anwendungen**.

| Parameter | Wert |
|---|---|
| FlexiBowl® | 2 |
| Kameras | 2 |
| Roboter | 2 |
| Switch erforderlich | **Ja** |

```{tip}
Diese Variante gewährleistet maximale Produktivität, da die beiden Zellen parallel und völlig autonom arbeiten.
```

```{important}
**Basisrezept und Rezeptverwaltung**

Wie bei der Einzelkonfiguration beginnt auch bei einer 2FB + 2CAM-Konfiguration der Prozess mit der Erstellung eines **einzigen Basisrezepts**, das die Hardware-Setups und die Kamerakalibrierung für das gesamte System enthält. Dieses Basisrezept wird dann für jede Station **dupliziert**: Jedes Duplikat bildet das Betriebsrezept dieser Station, in dem die Werkstückmodelle (bis zu 8 pro Station) erstellt werden.

Daher ist es unerlässlich, dass die Zuordnung zwischen den Geräten von Anfang an korrekt konfiguriert wird:

* **Kamera 1** → FlexiBowl® 1 (+ Trichter 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Trichter 2, falls vorhanden)

Eine fehlerhafte Zuordnung während der Einrichtung würde sich auf alle abgeleiteten Rezepte auswirken und die Teileerkennung sowie den ordnungsgemäßen Betrieb des gesamten Systems beeinträchtigen.
```

---

## Erforderliche Komponenten

### *FlexiVision One-Basis-Set*

Das **FlexiVision One-Basis-Set** (im Lieferumfang des Systems enthalten) enthält bereits alles Notwendige für die **erste Station** (Kamera, Optik, Kabel, Kalibrierungsgitter). Für die zweite Station muss kein zweites Komplettset gekauft werden.

### *Zusätzliches Kamera-Set*

Für die zweite Station reicht es aus, das **zusätzliche Kamera-Set** zu kaufen, das in einer spezifischen Version für jede FlexiBowl®-Größe erhältlich ist. Das Set enthält:

* 1 Kamera
* 1 für die FlexiBowl®-Größe bestimmte Optik
* 1 Kalibrierungsgitter
* 1 Kameranetzkabel
* 2 Ethernet-Kabel

Wählen Sie das Set entsprechend der Größe der **zweiten** FlexiBowl® aus:

| Größe FlexiBowl® | Artikelnummer zusätzliches Kamera-Set | Enthaltene Optik |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optic |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optic |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optic |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optic |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optic |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optic |
```{note}
Wenn die beiden Stationen **unterschiedliche FlexiBowl®-Größen** verwenden, muss das zusätzliche Kamera-Set entsprechend der Größe der FlexiBowl® der zweiten Station ausgewählt werden. Die erste Station ist bereits in dem Basis-Set enthalten.
```

### *Switch*

In Konfigurationen mit mehreren Geräten ist der Switch immer erforderlich. Artikelnummern, elektrische und physikalische Spezifikationen finden Sie im entsprechenden Abschnitt:

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Verkabelung

Der Verkabelungsplan ist für beide Varianten identisch: Alle Feldgeräte (FlexiBowl®, Kameras, Roboter) werden an den **Switch** angeschlossen, und der Switch wird über einen einzigen Ethernet-Anschluss mit dem **VisionController** verbunden. Der Unterschied zwischen Variante A und Variante B betrifft ausschließlich die Anzahl der an den Switch angeschlossenen Roboter.
```{important}
Der Switch verfügt über **8 Ethernet-Anschlüsse**. Stellen Sie sicher, dass die Gesamtzahl der anzuschließenden Geräte die verfügbare Kapazität nicht überschreitet, wobei alle vorhandenen FlexiBowl®-Geräte, Kameras und Roboter zu berücksichtigen sind.
```

### *Anschlussplan*

| Gerät | Verbindung |
|---|---|
| FlexiBowl® 1 | Ethernet-Anschluss → Switch |
| FlexiBowl® 2 | Ethernet-Anschluss → Switch |
| Kamera 1 | Ethernet-Kabel → Switch |
| Kamera 2 | Ethernet-Kabel → Switch |
| Roboter 1 | Ethernet-Anschluss → Switch |
| Roboter 2 *(nur Variante B)* | Ethernet-Anschluss → Switch |
| **Switch** | **Ethernet-Anschluss → VisionController** |
```{tip}
Stellen Sie sicher, dass jedem Gerät eine eindeutige IP-Adresse im gleichen Subnetz zugewiesen wird. Die vom VisionController für die beiden Stationen verwendeten TCP/IP-Ports sind konfigurierbar: standardmäßig **FB1 → 4001**, **FB2 → 4002**. Weitere Informationen finden Sie im Abschnitt [Kommunikationsprotokoll zwischen Roboter und Bildverarbeitungssystem](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md).
```

### *Belegte Switch-Ports nach Variante*

| Switch-Anschluss | Variante A (1 Roboter) | Variante B (2 Roboter) |
|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | Kamera 1 | Kamera 1 |
| 4 | Kamera 2 | Kamera 2 |
| 5 | Roboter 1 | Roboter 1 |
| 6 | VisionController | Roboter 2 |
| 7 | — | VisionController |
| 8 | — | — |

```{note}
**Verdrahtung der einzelnen Komponenten**

Die Verfahren zum Anschluss der einzelnen Komponenten (FlexiBowl®, Kamera, Trichter, Roboter) sind im Abschnitt [Verdrahtung und Anschlüsse](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md) ausführlich beschrieben. In einer 2FB + 2CAM-Konfiguration müssen dieselben Schritte einfach **zweimal** durchgeführt werden — einmal für jede Station — mit dem einzigen Unterschied, dass jedes Gerät an den **Switch** statt direkt an den VisionController angeschlossen wird.
```
```{important}
**Gerätezuordnung in der Software**

FlexiVision One kann alle Stationen gleichzeitig verwalten, jedoch ist es unerlässlich, dass die Zuordnung zwischen den Geräten in der Software korrekt konfiguriert ist. Stellen Sie sicher, dass Sie folgende Zuordnungen vornehmen:

* **Kamera 1** → FlexiBowl® 1 (+ Trichter 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Trichter 2, falls vorhanden)

Eine falsche Zuordnung würde die Erkennung der Teile und den korrekten Betrieb des gesamten Systems beeinträchtigen.
```

**→ [Erstkonfiguration des Systems](../QUICKSTART/SETUP/13_setup.md)**

