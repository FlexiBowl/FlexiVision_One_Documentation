

# **DashBoard-Seite** 
<img src="../../../../_shared/media/images/pagina_dashboardW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_dashboardB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Beschreibung der Dashboard-Seite
:header-rows: 1
:widths: 10 90

* - **#**
  - **Beschreibung**

* - 1
  - **Bereich Bildverarbeitung und Erkennung**
    * **Erkannte Bildverarbeitungsteile mit Grafik**: Anzahl der im aktuellen Bild erkannten Komponenten und zeitlicher Verlauf (30 s).
    

* - 2
  - **Betriebsstatus**
    * **In run (In Betrieb)**: Leuchtanzeige, die anzeigt, ob das System in Betrieb oder im Stillstand ist.
    * **In run time (Betriebszeit)**: Stoppuhr, die die Gesamtbetriebszeit des Systems anzeigt.

* - 3
  - **Steuerung und Auswahl**
    * **FlexiBowl®-Dropdown-Menü**: Hier können Sie das FlexiBowl®-Gerät auswählen, mit dem Sie arbeiten möchten.
    * **Test Locator**: Startet zyklische Bewegungen von FlexiBowl® und Trichter, solange sich Komponenten im Sichtbereich befinden.

* - 4
  - **Verbindungsstatus**
    * **FlexiBowl®**: Zeigt den Status der Echtzeitverbindung mit dem FlexiBowl® an.
    * **Roboter**: Zeigt den Status der Echtzeitverbindung mit dem Roboter an.

* - 5
  - **Analyse der Zykluszeiten (Timings)**
    * **Camera/Locator processing time** **(Verarbeitungszeit von Kamera/Locator)**: Einzelzeiten für die Bildaufnahme und die Erkennung der Komponenten.
    * **Total vision processing Time (Gesamte Bildverarbeitungszeit)**: Summe der Zeiten für Kamera und Locator
    * **Total FlexiBowl® / Robot time (Gesamtzeit für FlexiBowl® / Roboter)**: Zeit für eine Bewegungssequenz des FB und für einen einzelnen Pick & Place-Vorgang des Roboters.
    * **Total processing time (Gesamtbearbeitungszeit)**: Gesamtzeit des Prozesses (Vision + FB + Roboter).
    * **Fill hopper** **(Trichterbefüllung)**: Verlauf der Entleerungen des Trichters auf die Scheibe des FlexiBowl®.
    * **Vision - FlexiBowl® - Robot**: Vergleichsdiagramm der drei Funktionen, um den Einfluss jedes einzelnen Prozesses auf die Gesamtzeit zu verstehen
* - 6
  - **Leistungs- und Verlaufsdiagramme**
    * **Liste der erfassten Modelle**: Tabelle mit Koordinaten (**X**, **Y**), Drehung (**Rot**) des Bauteils und dem **Score** (Ähnlichkeitsgrad des erkannten Objekts im Vergleich zum Referenzmodell).
    * **Parts per minute (Teile pro Minute)**: Diagramm der durchschnittlich entnommenen Teile pro Minute.
```
(recipes)=
# **Seite Recipes (Rezepte)** 
<img src="../../../../_shared/media/images/pagina_recipesW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_recipesB.png" class="only-dark" style="width: 20%; height: auto;">

```{list-table} Beschreibung Seite Rezepte
:header-rows: 1
:widths: 10 90

* - **#**
  - **Beschreibung**

* - 1
  - **Rezeptdatenbank-Verwaltung**
    * **Backup**: Erstellt eine Sicherung aller Rezepte in einer einzigen XML-Datei, die an einem beliebigen Speicherort gespeichert werden kann.
    * **Import backup (Backup importieren)**: Ermöglicht den Import einer beliebigen zuvor mit FlexiVision One erstellten Sicherung.
    * **Load recipe (Rezept laden)**: Lädt das in der obigen Liste ausgewählte Rezept, um es aktiv zu machen.
    * **Delete recipe** **(Rezept löschen):** Löscht das ausgewählte Rezept endgültig aus der Liste.

* - 2
  - **Erstellen und Speichern**
    * **New recipe (Neues Rezept)**: Startet die Erstellung eines neuen Rezepts. Nachdem Sie den Namen und den FlexiBowl® ausgewählt haben, mit dem Sie arbeiten, öffnet sich direkt das Menü zur Erstellung der Vorlage. 
      :::{note}
        Das Rezept muss anschließend durch Klicken auf „Save“ gespeichert werden. 
      :::
    * **Save recipe (Rezept speichern)**: Speichert das aktuelle Rezept, wobei die geänderten Parameter überschrieben werden, oder erstellt eine neue Datei, falls diese noch nicht existiert.

* - 3
  - **Rezept bearbeiten**
    * **Edit recipe**: Direkte Schaltfläche, die zum Menü für die Konfiguration und Erstellung des Modells für das aktuell ausgewählte Rezept führt.
```

# **Setup-Seite** 
<img src="../../../../_shared/media/images/pagina_setupW.png" class="only-light" style="width: 20%; height: auto;">
<img src="../../../../_shared/media/images/pagina_setupB.png" class="only-dark" style="width: 20%; height: auto;">


```{list-table} Beschreibung der Setup-Seite
:header-rows: 1
:widths: 10 90

* - **#**
  - **Beschreibung**

* - 1
  - **Statusinformationen**
     - **Current selected recipe** **(Aktuell ausgewähltes Rezept)**: Zeigt den Namen des derzeit verwendeten Rezepts an.
     - **Current user name (Aktueller Benutzername)**: Zeigt den angemeldeten Benutzer und dessen Zugriffsebene an.
     - **In Run**: Zeigt an, ob die Anwendung aktiv ist.

* - 2
  - **Anmeldebereich**
     - **Name**: Feld zur Eingabe des Benutzernamens.
     - **Login** (**Anmeldung)**: Schaltfläche zum Bestätigen der Anmeldedaten und zum Anmelden im System.

* - 3
  - **Camera setup (Kameraeinstellungen)**: Bereich für die Konfiguration der Kameraparameter.
* - 4
  - **FlexiBowl®-Setup**: Bereich zur Einstellung der Bewegungs- und Steuerungsparameter des FlexiBowl®.
     
* - 5
  - **Hopper setup (Trichtereinstellung)**: Konfiguration der Trichterparameter (Vibration und Entleerung).
     
* - 6
  - **Roboter-Setup**: Bereich zur Konfiguration der Roboterkommunikation.

* - 7
  - **Protocol setup (Protokolleinrichtung)**: Seite zur Konfiguration der Parameter, die festlegen, wie viele Objekte die Bildverarbeitung in jedem Zyklus zurückgeben muss oder kann, in welcher Reihenfolge sie priorisiert werden und welche statistischen Werte basierend auf der Anzahl der Robotergriffe und der maximalen Bearbeitungszeit für jede Komponente verwendet werden sollen.
     
* - 8
  - **Account setup (Kontoeinrichtung)**: Ermöglicht die Konfiguration der verschiedenen Benutzerkonten entsprechend den Zugriffsebenen.

* - 9
  - **Laserpointer**: Ermöglicht die Verwendung eines Lasers, um eine Entnahme (Pick) ohne Roboter zu simulieren.
* - 10
  - **Evaluate PPM (PPM-Schätzung)**: Ermöglicht die Schätzung der Stückzahl pro Minute (PPM) bei Verwendung des Laserpointers.

* - 11
  - **Softwarelizenz**: Seite zur Aktivierung der Softwarelizenz.
```
# **INFO-Schaltflächen**
In jedem der Arbeitsbereiche befindet sich oben rechts eine INFO-Schaltfläche.
Über diese Schaltfläche wird eine Schritt-für-Schritt-Anleitung aufgerufen, die auch im Video-Tutorial zu sehen ist.
```{dropdown} Info-Schaltfläche auf der Seite [Camera FLB](cameraFLB)

   :::{video} ../../../../_shared/media/videos/TastoInfo_CameraFLB_1280x720.mp4
   :width: 100%
   :align: center
   :::

```

```{dropdown} Info-Schaltfläche auf der Seite [Calibration](calibrazione)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Calibration_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Train Model](modello)

   :::{video} ../../../../_shared/media/videos/TastoInfo_TrainModel_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Define Robot Picking Area](robotarea)

   :::{video} ../../../../_shared/media/videos/TastoInfo_DefineRobotArea_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Locator Model](locator)

   :::{video} ../../../../_shared/media/videos/TastiInfo_LocatorModel_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Clearances](clearances)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Clearances_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Clearance 1](clearance1)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Clearance1_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Picking Offset](pickingoffset)

   :::{video} ../../../../_shared/media/videos/TastoInfo_PickingOffset_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Define Hopper Area](definehopperarea)

   :::{video} ../../../../_shared/media/videos/TastoInfo_AreaHopper_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
```{dropdown} Info-Schaltfläche auf der Seite [Define Value Hopper](definevaluehopper)

   :::{video} ../../../../_shared/media/videos/TastoInfo_Hopper_1280x720.mp4
   :width: 100%
   :align: center
   :::

```
