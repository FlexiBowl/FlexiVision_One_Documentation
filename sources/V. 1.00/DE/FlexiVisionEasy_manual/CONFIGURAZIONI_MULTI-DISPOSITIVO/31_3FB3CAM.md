# **3 FlexiBowl® und 3 Kameras**

Dieser Abschnitt beschreibt die verfügbaren Konfigurationen für den Betrieb mit **drei FlexiBowl®** und **drei Kameras** innerhalb derselben Picking-Insel, die von einem einzigen VisionController FlexiVision One gesteuert werden.

---

## Überblick über die Konfiguration

In einer Konfiguration **mit 3 FlexiBowl® + 3 Kameras** umfasst das System drei unabhängige Versorgungs- und Bildverarbeitungsstationen, die alle vom selben VisionController gesteuert werden. Jede Station besteht aus:

* 1 FlexiBowl®
* 1 Kamera mit spezieller Optik
* 1 Trichter (optional, falls vorhanden)

Die drei Stationen kommunizieren über einen **Netzwerk-Switch** mit dem VisionController.
```{important}
Der **Switch** ist eine **obligatorische** Komponente in allen Konfigurationen mit mehreren Geräten. Ohne ihn ist es nicht möglich, mehrere FlexiBowl®-Einheiten und mehrere Kameras gleichzeitig an den VisionController anzuschließen. Technische Daten und Bestellnummern finden Sie im Abschnitt [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Diese Konfiguration unterstützt drei Betriebsvarianten, je nach Anzahl der in der Anlage verfügbaren Roboter:

| | **Variante A** | **Variante B** | **Variante C** |
|---|---|---|---|
| **Roboter** | 1 | 2 | 3 |
| **FlexiBowl®** | 3 | 3 | 3 |
| **Kameras** | 3 | 3 | 3 |
| **Betriebslogik** | Der Roboter bedient alle drei Stationen | Erster Roboter an einem FlexiBowl®, zweiter Roboter an zwei FlexiBowl® | Jeder Roboter ist einer Station zugeordnet |
| **Switch erforderlich** | Ja | Ja | Ja |
---

## Variante A — 1 Roboter, 3 FlexiBowl®

![Systemübersicht 3FB3CAM1Roboter](../../../../_shared/media/images/3FB3CAM1R.png)

Ein **einziger Roboter** bedient alle drei Stationen. Der Roboter muss so positioniert werden, dass er den Picking-Bereich jedes FlexiBowl® erreichen kann. Der VisionController verwaltet die drei Stationen unabhängig voneinander, jede mit ihrem eigenen Rezept und TCP/IP-Kommunikationskanal.

Jede Station unterstützt **Standard-** oder **Mix-Anwendungen**.

| Parameter | Wert |
|---|---|
| FlexiBowl® | 3 |
| Kameras | 3 |
| Roboter | 1 |
| Switch erforderlich | **Ja** |


```{important}
**Basisrezept und Rezeptverwaltung**

Wie bei der Einzelkonfiguration beginnt auch bei einer 3FB + 3CAM-Konfiguration der Prozess mit der Erstellung eines **einzigen Basisrezepts**, das die Hardware-Setups und die Kamerakalibrierung für das gesamte System enthält. Dieses Basisrezept wird dann für jede Station **dupliziert**: Jedes Duplikat bildet das Betriebsrezept dieser Station, in dem die Werkstückmodelle (bis zu 8 pro Station) erstellt werden.

Daher ist es unerlässlich, dass die Zuordnung zwischen den Geräten von Anfang an korrekt konfiguriert wird:

* **Kamera 1** → FlexiBowl® 1 (+ Trichter 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Trichter 2, falls vorhanden)
* **Kamera 3** → FlexiBowl® 3 (+ Trichter 3, falls vorhanden)

Eine fehlerhafte Zuordnung während der Einrichtung würde sich auf alle abgeleiteten Rezepte auswirken und die Teileerkennung sowie den korrekten Betrieb des gesamten Systems beeinträchtigen.
```
---

## Variante B — 2 Roboter, 3 FlexiBowl®

![Systemübersicht 3FB3CAM2Roboter](../../../../_shared/media/images/3FB3CAM2R.png)

In dieser Variante teilen sich **zwei Roboter** die drei Stationen. Der erste Roboter übernimmt das Picking an einem einzigen FlexiBowl®, der zweite an den beiden anderen FlexiBowl®. Die Lastverteilung zwischen den Robotern wird durch die Logik des Roboterprogramms und den physischen Aufbau der Anlage bestimmt. 

Jede Station unterstützt **Standard-** oder **Mix-Anwendungen**.

| Parameter | Wert |
|---|---|
| FlexiBowl® | 3 |
| Kameras | 3 |
| Roboter | 2 |
| Switch erforderlich | **Ja** |

```{important}
**Basisrezept und Rezeptverwaltung**

Wie bei der Einzelkonfiguration beginnt auch bei einer 3FB + 3CAM-Konfiguration der Prozess mit der Erstellung eines **einzigen Basisrezepts**, das die Hardware-Setups und die Kamerakalibrierung für das gesamte System enthält. Dieses Basisrezept wird dann für jede Station **dupliziert**: Jedes Duplikat bildet das Betriebsrezept dieser Station, in dem die Werkstückmodelle (bis zu 8 pro Station) erstellt werden.

Daher ist es unerlässlich, dass die Zuordnung zwischen den Geräten von Anfang an korrekt konfiguriert wird:

* **Kamera 1** → FlexiBowl® 1 (+ Trichter 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Trichter 2, falls vorhanden)
* **Kamera 3** → FlexiBowl® 3 (+ Trichter 3, falls vorhanden)

Eine fehlerhafte Zuordnung während der Einrichtung würde sich auf alle abgeleiteten Rezepte auswirken und die Teileerkennung sowie den korrekten Betrieb des gesamten Systems beeinträchtigen.
```
---

## Variante C — 3 Roboter, 3 FlexiBowl®

![Systemübersicht 3FB3CAM3Roboter](../../../../_shared/media/images/3FB3CAM3R.png)

Jeder Roboter ist einer einzelnen Station zugeordnet: maximale Produktivität durch drei Zellen, die parallel und völlig unabhängig voneinander arbeiten.

Jede Station unterstützt **Standard-** oder **Mix-Anwendungen**.

| Parameter | Wert |
|---|---|
| FlexiBowl® | 3 |
| Kameras | 3 |
| Roboter | 3 |
| Switch erforderlich | **Ja** |

```{tip}
Die Variante C bietet die besten Gesamtleistungen. Jede Zelle ist völlig autonom und nicht von der Verfügbarkeit der anderen abhängig.
```
```{important}
**Basisrezept und Rezeptverwaltung**

Wie bei der Einzelkonfiguration beginnt auch bei einer 3FB + 3CAM-Konfiguration der Prozess mit der Erstellung eines **einzigen Basisrezepts**, das die Hardware-Setups und die Kamerakalibrierung für das gesamte System enthält. Dieses Basisrezept wird dann für jede Station **dupliziert**: Jedes Duplikat bildet das Betriebsrezept dieser Station, in dem die Werkstückmodelle (bis zu 8 pro Station) erstellt werden.

Daher ist es unerlässlich, dass die Zuordnung zwischen den Geräten von Anfang an korrekt konfiguriert wird:

* **Kamera 1** → FlexiBowl® 1 (+ Trichter 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Trichter 2, falls vorhanden)
* **Kamera 3** → FlexiBowl® 3 (+ Trichter 3, falls vorhanden)

Eine fehlerhafte Zuordnung während der Einrichtung würde sich auf alle abgeleiteten Rezepte auswirken und die Teileerkennung sowie den korrekten Betrieb des gesamten Systems beeinträchtigen.
```
---

## Erforderliche Komponenten

### *FlexiVision One-Basisset*

 Das **FlexiVision One-Basis-Set** (im Lieferumfang des Systems enthalten) enthält bereits alles Notwendige für die **erste Station** (Kamera, Optik, Kabel, Kalibrierungsgitter), einschließlich des VisionControllers. Für die zusätzlichen Stationen muss kein zweites Komplettset gekauft werden.

### *Zusätzliches Kamera-Set (× 2)*

Für die Stationen 2 und 3 müssen **zwei zusätzliche Kamera-Sets** erworben werden, eines für jede Station, wobei die Artikelnummer ausgewählt werden muss, die der Größe des FlexiBowl® der jeweiligen Station entspricht. Das Set enthält:

* 1 Kamera
* 1 für die FlexiBowl®-Größe bestimmte Optik
* 1 Kalibrierungsgitter
* 1 Kameranetzkabel
* 2 Ethernet-Kabel

Wählen Sie das Set entsprechend der Größe des FlexiBowl® jeder zusätzlichen Station aus:

| FlexiBowl®-Größe | Artikelnummer des zusätzlichen Kamera-Sets | Inklusive Optik |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optic |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optic |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optic |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optic |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optic |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optic |

```{note}
Falls an den zusätzlichen Stationen FlexiBowl® anderer Größen verwendet werden, sollten Sie für jede Größe ein Set erwerben.  
 Bei einer Konfiguration mit FB500 + FB650 + FB800 deckt das Basisset beispielsweise die erste Station ab, während für die zweite und dritte Station jeweils die Artikelnummern GM002004 und GM002006 bestellt werden müssen.
```

### *Switch*

In Konfigurationen mit mehreren Geräten ist der Switch immer erforderlich. Artikelnummern, elektrische und physikalische Spezifikationen finden Sie im entsprechenden Abschnitt:

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Verkabelung

In **Variante A** (1 Roboter) werden alle Feldgeräte (FlexiBowl®, Kameras, Roboter) an den **Switch** angeschlossen, und der Switch wird über einen einzigen Ethernet-Anschluss mit dem **VisionController** verbunden. Die Gesamtzahl der Verbindungen liegt innerhalb der 8 verfügbaren Anschlüsse am Switch.

Ab **Variante B** übersteigt die Gesamtzahl der Geräte die Anzahl der am Switch verfügbaren Anschlüsse.   
In diesen Fällen wird ein Port des VisionControllers für die Verbindung zum Switch genutzt, während die verbleibenden freien Ports des VisionControllers die Geräte aufnehmen, für die am Switch kein Platz ist:

- In **Variante B** (2 Roboter) wird der **FlexiBowl® 3** direkt an einen freien Port des VisionControllers angeschlossen.
- In **Variante C** (3 Roboter) werden der **FlexiBowl® 3** und die **Kamera 3** direkt an die freien Anschlüsse des VisionControllers angeschlossen.

```{important}
Der Switch verfügt über **8 Ethernet**-Anschlüsse. Ab Variante B ist es nicht mehr möglich, alle Geräte ausschließlich über den Switch anzuschließen: Die überschüssigen Geräte müssen direkt an die freien Ethernet-Anschlüsse des VisionControllers angeschlossen werden, wie in den folgenden Tabellen angegeben.
```
:::{note}
Man kann frei entscheiden, welche Geräte an den VisionController angeschlossen werden sollen. Wichtig ist, immer einen freien Anschluss frei zu halten, um den VisionController an den Switch anzuschließen
:::

### *Anschlussplan*

| Gerät | Variante A (1 Roboter) | Variante B (2 Roboter) | Variante C (3 Roboter) |
|---|---|---|---|
| FlexiBowl® 1 | → Switch | → Switch | → Switch |
| FlexiBowl® 2 | → Switch | → Switch | → Switch |
| FlexiBowl® 3 | → Switch | **→ VisionController (freier Anschluss)** | **→ VisionController (freier Anschluss)** |
| Kamera 1 | → Switch | → Switch | → Switch |
| Kamera 2 | → Switch | → Switch | → Switch |
| Kamera 3 | → Switch | → Switch | **→ VisionController (freier Anschluss)** |
| Roboter 1 | → Switch | → Switch | → Switch |
| Roboter 2 | — | → Switch | → Switch |
| Roboter 3 | — | — | → Switch |
| **Switch** | **→ VisionController** | **→ VisionController** | **→ VisionController** |

:::{note}
Man kann frei entscheiden, welche Geräte an den VisionController angeschlossen werden sollen. Wichtig ist, immer einen freien Anschluss frei zu halten, um den VisionController an den Switch anzuschließen
:::

```{tip}
Stellen Sie sicher, dass jedem Gerät eine eindeutige IP-Adresse im selben Subnetz zugewiesen ist.  
Die vom VisionController für die drei Stationen verwendeten TCP/IP-Ports sind konfigurierbar: standardmäßig **FB1 → 4001**, **FB2 → 4002**, **FB3 → 4003**.  
Weitere Informationen finden Sie im Abschnitt [Kommunikationsprotokoll zwischen Roboter und Bildverarbeitungssystem](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md).
```
### *Belegte Switch-Ports nach Variante*

| Switch-Anschluss | Variante A (1 Roboter) | Variante B (2 Roboter) | Variante C (3 Roboter) |
|---|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | FlexiBowl® 3 | Kamera 1 | Kamera 1 |
| 4 | Kamera 1 | Kamera 2 | Kamera 2 |
| 5 | Kamera 2 | Kamera 3 | Roboter 1 |
| 6 | Kamera 3 | Roboter 1 | Roboter 2 |
| 7 | Roboter 1 | Roboter 2 | Roboter 3 |
| 8 | VisionController | VisionController | VisionController |

### *Belegte VisionController-Ports nach Variante*

| VisionController-Port | Variante A (1 Roboter) | Variante B (2 Roboter) | Variante C (3 Roboter) |
|---|---|---|---|
| 1 | Switch | Switch | Switch |
| 2 | — | FlexiBowl® 3 | FlexiBowl® 3 |
| 3 | — | — | Kamera 3 |

:::{note}
Man kann frei entscheiden, welche Geräte an den VisionController angeschlossen werden sollen. Wichtig ist, immer einen freien Anschluss frei zu halten, um den VisionController an den Switch anzuschließen.
:::

```{note}
In **Variante B** sind alle Anschlüsse des Switches belegt (7 Geräte + VisionController): Der FlexiBowl® 2 wird direkt an den VisionController angeschlossen. In der **Variante C** wird auch die Kamera 3 direkt an den VisionController angeschlossen und belegt dabei den dritten verfügbaren Anschluss.
```
```{note}
**Verdrahtung der einzelnen Komponenten**

Die Verfahren zum Anschluss der einzelnen Komponenten (FlexiBowl®, Kamera, Trichter, Roboter) sind im Abschnitt [Verdrahtung und Anschlüsse](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md) ausführlich beschrieben.  
 In einer 3FB + 3CAM-Konfiguration müssen dieselben Vorgänge einfach **dreimal** ausgeführt werden - einmal für jede Station - mit dem einzigen Unterschied, dass jedes Gerät an den **Switch** und nicht direkt an den VisionController angeschlossen wird, mit Ausnahme von **FlexiBowl® 2** (Varianten B und C) und **Kamera 3** (Variante C), die direkt an die freien Ethernet-Anschlüsse des VisionControllers angeschlossen werden.
```
```{important}
**Gerätezuordnung in der Software**

FlexiVision One kann alle Stationen gleichzeitig verwalten, jedoch ist es unerlässlich, dass die Zuordnung zwischen den Geräten in der Software korrekt konfiguriert ist. Stellen Sie sicher, dass Sie folgende Zuordnungen vornehmen:

* **Kamera 1** → FlexiBowl® 1 (+ Trichter 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Trichter 2, falls vorhanden)
* **Kamera 3** → FlexiBowl® 3 (+ Trichter 3, falls vorhanden)

Eine falsche Zuordnung würde die Erkennung der Teile und den korrekten Betrieb des gesamten Systems beeinträchtigen.
```

**→ [Erstkonfiguration des Systems](../QUICKSTART/SETUP/13_setup.md)**

