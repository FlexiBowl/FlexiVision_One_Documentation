(camerasetup)=
# **Kamera Setup**

In diesem Abschnitt wird das Verfahren zum Konfigurieren und Testen der Industriekamera des FlexiVision One-Systems beschrieben. Die korrekte Konfiguration der Kamera ist für die Aufnahme hochwertiger Bilder von entscheidender Bedeutung.

```{note}
**Voraussetzungen**

Stellen Sie vor dem Fortfahren Folgendes sicher:
- Die Kamera wurde mechanisch im richtigen Abstand installiert
- Das Ethernet-Kabel der Kamera ist mit dem VisionController verbunden
- Die Kamera wird mit Strom versorgt (über PoE oder externes Netzteil)
- FlexiBowl® ist konfiguriert und die Hintergrundbeleuchtung funktioniert (für Testaufnahmen)
```

---

## Zugriff auf die Kamerakonfiguration

```{list-table}

* - **1** 
  - Klicken Sie auf der Hauptseite der Software auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Suchen Sie auf der SETUP-Seite das Symbol **Kamera Setup** und klicken Sie darauf
    ```{dropdown} Setup-Seite 
       ![Setup-Seite](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - Die Seite zur Konfiguration der Kamera wird geöffnet
```

---

## Übersicht über die Benutzeroberfläche des Kamera Setups

Die Seite Kamera-Setup enthält drei Hauptinformationsfelder und einen Konfigurationsbereich:
![Paagina Camera Setup](../../../../../_shared/media/images/pagina_camsetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Abschnitt
  - Beschreibung
* - **Selected Camera**
  - Zeigt die Kennung der aktuell ausgewählten Kamera an. Wird beim Start von FlexiVision One automatisch angezeigt.
* - **Camera Serial Number**
  - Zeigt die eindeutige Seriennummer der angeschlossenen Kamera an
* - **Status**
  - Zeigt den Verbindungsstatus an
* - **Calibration Result**
  - Zeigt das Ergebnis der Kamerakalibrierung an
* - **Config Camera**
  - Schaltfläche zum Öffnen der detaillierten Konfigurationsseite
```

---


:::{note}
Aus Gründen der Einfachheit und Einheitlichkeit wird empfohlen, die Kameranummer mit dem entsprechenden FlexiBowl® abzustimmen: 
 - ✅ Kamera über FlexiBowl® 1 installiert: CAM-CIC-5000-20G-12345 > Kamera 1 für FlexiBowl® 1 auswählen
:::

:::{warning}
Falls die Kamera beim ersten Start von FlexiVision nicht sichtbar ist, konsultieren Sie den Abschnitt [Troubleshooting für Kamera Setup](scelta_camera)
:::


---
## Nächste Schritte

Sobald die Einrichtung der Kamera abgeschlossen ist, fahren Sie mit fort:

- [Kamera-Kalibrierung](calibrazione)
- [FlexiBowl®-Setup](fbsetup)
- [Trichter-Setup](13b_Hopper_Setup.md)
- [Roboter-Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Rezept speichern](ricettabase)

