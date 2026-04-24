# **2 FlexiBowl® und 2 Kameras**

Dieser Abschnitt beschreibt die verfügbaren Konfigurationen, wenn mit **zwei FlexiBowl®** und **zwei Kameras** gearbeitet werden soll, die von einem einzigen FlexiVision One VisionController verwaltet werden.

---

## Konfigurationsübersicht

In einer Konfiguration **2 FlexiBowl® + 2 Kameras** umfasst das System zwei unabhängige Zuführ- und Bildverarbeitungsstationen, die beide vom selben VisionController verwaltet werden. Jede Station besteht aus:

* 1 FlexiBowl®
* 1 Kamera mit dedizierter Optik
* 1 Hopper (optional, falls vorhanden)

Die beiden Stationen kommunizieren mit dem VisionController über einen **Netzwerk-Switch**.

```{important}
Der **Switch** ist in allen Mehrgeräte-Konfigurationen eine **obligatorische** Komponente. Ohne ihn können nicht mehrere FlexiBowl® und mehrere Kameras gleichzeitig mit dem VisionController verbunden werden. Für technische Spezifikationen und Bestellcodes siehe Abschnitt [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Diese Konfiguration unterstützt zwei Betriebsvarianten, abhängig von der Anzahl der in der Anlage verfügbaren Roboter:
| | **Variante A** | **Variante B** |
|---|---|---|
| **Roboter** | 1 | 2 |
| **FlexiBowl®** | 2 | 2 |
| **Kameras** | 2 | 2 |
| **Betriebslogik** | Der Roboter erreicht beide Stationen | Jeder Roboter ist einer Station zugeordnet |
| **Switch erforderlich** | Ja | Ja |


---

## Variante A — 1 Roboter, 2 FlexiBowl®

![Systemübersicht 2FB2CAM1Robot](../../../../_shared/media/images/2FB2CAM1R.png)

In dieser Variante arbeitet ein **einzelner Roboter** an beiden Stationen. Der Roboter ist so positioniert, dass er den Picking-Bereich jedes FlexiBowl® erreichen kann und die Entnahme zwischen den beiden Stationen anhand der empfangenen Befehle abwechselt.

Jede Station verwaltet ihre eigene unabhängige Rezeptur. Auf jeder Station kann eine Anwendung vom Typ **Standard** oder **Mix** konfiguriert werden, mit Modellen unterschiedlicher Komponenten innerhalb derselben Rezeptur.

| Parameter | Wert |
|---|---|
| FlexiBowl® | 2 |
| Kameras | 2 |
| Roboter | 1 |
| Switch erforderlich | **Ja** |

```{important}
**Basisrezeptur und Rezeptverwaltung**

Wie bei der Einzelkonfiguration beginnt auch bei einer 2FB + 2CAM Konfiguration der Prozess mit der Erstellung einer **einzigen Basisrezeptur**, die die Hardware-Setups und die Kamerakalibrierung für das gesamte System enthält. Diese Basisrezeptur wird anschließend für jede Station **dupliziert**: Jedes Duplikat bildet die Betriebsrezeptur dieser Station, in der die Teilemodelle erstellt werden (bis zu 8 pro Station).

Daher ist es entscheidend, dass die Zuordnung zwischen den Geräten von Anfang an korrekt konfiguriert wird:

* **Kamera 1** → FlexiBowl® 1 (+ Hopper 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Hopper 2, falls vorhanden)

Eine falsche Zuordnung während des Setups würde sich auf alle abgeleiteten Rezepturen auswirken und die Teileerkennung sowie den korrekten Betrieb des gesamten Systems beeinträchtigen.
```
---

## Variante B — 2 Roboter, 2 FlexiBowl®

![Systemübersicht 2FB2CAM2Robot](../../../../_shared/media/images/2FB2CAM2R.png)

In dieser Variante ist jeder Roboter einer einzelnen Station zugeordnet: **Roboter 1** führt das Picking auf FlexiBowl® 1 aus, **Roboter 2** führt das Picking auf FlexiBowl® 2 aus. Die beiden Zellen sind unabhängig und überschneiden sich nicht.

Auch in dieser Variante unterstützt jede Station Anwendungen sowohl vom Typ **Standard** als auch **Mix**.

| Parameter | Wert |
|---|---|
| FlexiBowl® | 2 |
| Kameras | 2 |
| Roboter | 2 |
| Switch erforderlich | **Ja** |

```{tip}
Diese Variante gewährleistet maximale Produktivität, wobei die beiden Zellen parallel und vollständig autonom arbeiten.
```

```{important}
**Basisrezeptur und Rezeptverwaltung**

Wie bei der Einzelkonfiguration beginnt auch bei einer 2FB + 2CAM Konfiguration der Prozess mit der Erstellung einer **einzigen Basisrezeptur**, die die Hardware-Setups und die Kamerakalibrierung für das gesamte System enthält. Diese Basisrezeptur wird anschließend für jede Station **dupliziert**: Jedes Duplikat bildet die Betriebsrezeptur dieser Station, in der die Teilemodelle erstellt werden (bis zu 8 pro Station).

Daher ist es entscheidend, dass die Zuordnung zwischen den Geräten von Anfang an korrekt konfiguriert wird:

* **Kamera 1** → FlexiBowl® 1 (+ Hopper 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Hopper 2, falls vorhanden)

Eine falsche Zuordnung während des Setups würde sich auf alle abgeleiteten Rezepturen auswirken und die Teileerkennung sowie den korrekten Betrieb des gesamten Systems beeinträchtigen.
```

---

## Erforderliche Komponenten

### FlexiVision One Basiskit

Das **FlexiVision One Basiskit** (mit dem System geliefert) enthält bereits alles, was für die **erste Station** erforderlich ist (Kamera, Optik, Kabel, Kalibriergitter). Es ist nicht erforderlich, ein zweites vollständiges Kit für die zweite Station zu erwerben.

### Zusätzliches Kamerakit

Für die zweite Station reicht es aus, das **Zusätzliche Kamerakit** zu erwerben, das in einer spezifischen Version für jede FlexiBowl®-Größe verfügbar ist. Das Kit enthält:

* 1 Kamera
* 1 Optik, dediziert für die FlexiBowl®-Größe
* 1 Kalibriergitter
* 1 Kameraversorgungskabel
* 2 Ethernet-Kabel

Das Kit entsprechend der Größe des **zweiten** FlexiBowl® auswählen:

| FlexiBowl®-Größe | Code Zusätzliches Kamerakit | Enthaltene Optik |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optic |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optic |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optic |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optic |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optic |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optic |
```{note}
Wenn die beiden Stationen FlexiBowl® in **unterschiedlichen Größen** verwenden, muss das Zusätzliche Kamerakit entsprechend der Größe des FlexiBowl® der zweiten Station ausgewählt werden. Die erste Station ist bereits durch das Basiskit abgedeckt.
```

### Switch

Der Switch ist in Mehrgeräte-Konfigurationen immer erforderlich. Für Code, elektrische Spezifikationen und physische Spezifikationen siehe den entsprechenden Abschnitt:

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Verkabelung

Das Verkabelungsschema ist für beide Varianten identisch: Alle Feldgeräte (FlexiBowl®, Kameras, Roboter) werden mit dem **Switch** verbunden, und der Switch wird über einen einzelnen Ethernet-Port mit dem **VisionController** verbunden. Der Unterschied zwischen Variante A und Variante B betrifft ausschließlich die Anzahl der mit dem Switch verbundenen Roboter.
```{important}
Der Switch verfügt über **8 Ethernet-Ports**. Prüfen, dass die Gesamtzahl der anzuschließenden Geräte die verfügbare Kapazität nicht überschreitet, unter Berücksichtigung aller vorhandenen FlexiBowl®, Kameras und Roboter.
```

### Verbindungsschema

| Gerät | Verbindung |
|---|---|
| FlexiBowl® 1 | Ethernet-Port → Switch |
| FlexiBowl® 2 | Ethernet-Port → Switch |
| Kamera 1 | Ethernet-Kabel → Switch |
| Kamera 2 | Ethernet-Kabel → Switch |
| Roboter 1 | Ethernet-Port → Switch |
| Roboter 2 *(nur Variante B)* | Ethernet-Port → Switch |
| **Switch** | **Ethernet-Port → VisionController** |
```{tip}
Prüfen, dass jedem Gerät eine eindeutige IP-Adresse in derselben Subnet zugewiesen ist. Die vom VisionController für die beiden Stationen verwendeten TCP/IP-Ports sind konfigurierbar: standardmäßig **FB1 → 4001**, **FB2 → 4002**. Siehe Abschnitt [Kommunikationsprotokoll Roboter-Bildverarbeitung](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) für Details.
```

### Belegte Switch-Ports nach Variante

| Switch-Port | Variante A (1 Roboter) | Variante B (2 Roboter) |
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
**Verkabelung der einzelnen Komponenten**

Die physischen Anschlussverfahren für jede Komponente (FlexiBowl®, Kamera, Hopper, Roboter) sind vollständig im Abschnitt [Verkabelung und Anschlüsse](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md) beschrieben. In einer 2FB + 2CAM Konfiguration werden dieselben Vorgänge einfach **zweimal** ausgeführt — einmal für jede Station — mit dem einzigen Unterschied, dass jedes Gerät mit dem **Switch** statt direkt mit dem VisionController verbunden wird.
```
```{important}
**Gerätezuordnung in der Software**

FlexiVision One kann alle Stationen gleichzeitig verwalten, aber es ist entscheidend, dass die Zuordnung zwischen den Geräten in der Software korrekt konfiguriert wird. Stellen Sie sicher, dass folgende Zuordnung erfolgt:

* **Kamera 1** → FlexiBowl® 1 (+ Hopper 1, falls vorhanden)
* **Kamera 2** → FlexiBowl® 2 (+ Hopper 2, falls vorhanden)

Eine falsche Zuordnung würde die Teilelokalisierung und den korrekten Betrieb des gesamten Systems beeinträchtigen.
```

**→ [Initiale Systemkonfiguration](../QUICKSTART/SETUP/13_setup.md)**

