# **Bandüberwachung: Check Belt**

Dieser Abschnitt beschreibt das Verfahren zur Überprüfung des Verschleiß- und Sauberkeitszustands des FlexiBowl®-Bands mithilfe der Funktion **Belt Check**.

**Was ist der Belt Check?**
Der **Belt Check** ist ein Werkzeug, das das aktuelle Bild des Bands mit einem Referenzbild des sauberen Bands (**Clean Reference**) vergleicht und dabei einen Ähnlichkeitsindex berechnet. Dadurch lässt sich der Verschmutzungs- oder Verschleißgrad des Bands im Laufe der Zeit überwachen und der Wartungsbedarf frühzeitig erkennen.

:::{note}
**Voraussetzungen**

Stellen Sie vor dem Fortfahren sicher, dass:

- Der FlexiBowl® angeschlossen und konfiguriert ist ([FlexiBowl® Setup](../QUICKSTART/SETUP/13a_FB_Setup.md))
- Das Band sichtbar und korrekt beleuchtet ist
:::

---

## Zugriff auf die Seite Check Belt

| **1** | Klicken Sie auf der Hauptseite der Software auf **Setup** |
| ----- | ------------------------------------------------------------ |
| **2** | Suchen und klicken Sie auf der Seite SETUP auf das Symbol **Check Belt** |
| **3** | Die Seite zur Bandkontrolle wird geöffnet, mit einem Block für jedes vom System verwaltete FlexiBowl® |

---

## Übersicht der Check-Belt-Oberfläche

:::{image} ../../../_shared/media/images/beltcheck.png
:width: 100%
:align: center
:::

Die Seite ist in einen Block für jedes verbundene FlexiBowl® unterteilt, der jeweils aus zwei Bereichen besteht:

| Element | Beschreibung |
| --- | --- |
| **Flb X Connected** | Verbindungsstatusanzeige des entsprechenden FlexiBowl® (🟢 Grün = verbunden, 🔴 Rot = nicht verbunden) |
| **Save Clean Reference** | Erfasst und speichert das aktuelle Bild des Bands als „sauberes" Referenzbild, das bei nachfolgenden Kontrollen als Vergleichsgrundlage dient |
| **Delete Clean Reference** | Löscht das zuvor gespeicherte Referenzbild, um ein neues erfassen zu können |
| **Kameravorschau (vorher/nachher)** | Die beiden Miniaturansichten zeigen jeweils das gespeicherte Referenzbild und das aktuelle Bild des Bands zum Zeitpunkt des Tests |
| **Run Belt Check** | Startet den Vergleich zwischen Referenzbild und aktuellem Bild und berechnet den Zustand des Bands |
| **Belt Health Result** | Panel mit dem Ergebnis des Vergleichs: abgestufte Leiste Clean → Dirty, farbige Anzeige, Textstatus und Datum der letzten Kontrolle |

---

## Vorgehensweise

### Schritt 1: Erfassung der sauberen Referenz

:::{important}
Führen Sie diesen Schritt **nur bei tatsächlich sauberem Band** durch. Die Genauigkeit aller zukünftigen Kontrollen hängt von der Qualität dieses Referenzbilds ab.
:::

| **1** | Stellen Sie sicher, dass das Band sauber und frei von Bauteilen oder Rückständen im erfassten Bereich ist |
| **2** | Klicken Sie auf **Save Clean Reference** |
| **3** | Das Bild wird erfasst und als Referenz gespeichert; es erscheint in der linken Miniaturansicht |

:::{tip}
Wenn das Band ausgetauscht oder gründlich gereinigt wird, wiederholen Sie diesen Schritt, um die Referenz zu aktualisieren.
:::

### Schritt 2: Durchführung des Belt Check

| **4** | Klicken Sie auf **Run Belt Check** |
| **5** | Das System erfasst das aktuelle Bild des Bands (sichtbar in der rechten Miniaturansicht) und vergleicht es mit der gespeicherten Referenz |
| **6** | Das Ergebnis wird im Panel **Belt Health Result** angezeigt |

---

## Interpretation der Ergebnisse

Das Panel **Belt Health Result** zeigt:

| Element | Bedeutung |
| --- | --- |
| **Abgestufte Leiste** | Visuelle Darstellung der Position des gemessenen Werts zwischen den beiden Extremen Clean (sauber) und Dirty (schmutzig) |
| **Farbige Anzeige und Text** | Zusammenfassender Zustand des Bands: |

| Farbe | Text | Bedeutung |
| --- | --- | --- |
| 🟢 Grün | **Good** | Band in gutem Zustand |
| 🟡 Gelb | **Warning** | Band muss beobachtet werden, möglicherweise bald Reinigung erforderlich |
| 🔴 Rot | **Poor** | Band verschmutzt oder verschlissen, Reinigung/Wartung wird empfohlen |



:::{note}
*Noch zu bestätigen*: die genauen Prozentschwellen, die den Übergang von Good zu Warning zu Poor bestimmen.
:::

---