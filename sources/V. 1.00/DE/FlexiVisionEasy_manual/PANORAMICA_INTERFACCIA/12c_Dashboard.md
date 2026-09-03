# **DashBoard Seite**
Die Benutzeroberfläche von FlexiVision One ist in Funktionsbereiche unterteilt, die den Benutzer von der Erstkonfiguration bis zur operativen Verwaltung des Systems führen.
Jede Seite liefert Echtzeitinformationen zu Maschinenstatus, Verbindungen, Leistung und Prozessparametern und bietet direkten Zugriff auf die wichtigsten Funktionen.
Die Navigation ist so konzipiert, dass sie eine einfache Bedienung, eine sofortige Kontrolle der Abläufe und eine kontinuierliche Überwachung der Leistung der Bildverarbeitung, der Zuführung und des Roboters gewährleistet.


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
    * **Camera/Locator processing time (Verarbeitungszeit von Kamera/Locator)**: Einzelzeiten für die Bildaufnahme und die Erkennung der Komponenten.
    * **Total vision processing Time (Gesamte Bildverarbeitungszeit)**: Summe der Zeiten für Kamera und Locator
    * **FlexiBowl®/Robot-time (Gesamtzeit für FlexiBowl® / Roboter)**: Zeit für eine Bewegungssequenz des FB und für einen einzelnen Pick & Place-Vorgang des Roboters.
    * **Total processing time (Gesamtbearbeitungszeit)**: Gesamtverarbeitungszeit: Gesamtzeit des Prozesses (Vision + FB + Roboter).
    * **Fill hopper (Trichterbefüllung)**: Verlauf der Entleerungen des Trichters auf die Scheibe des FlexiBowl®.
    * **Vision - FlexiBowl® - Robot**: Vergleichsdiagramm der drei Funktionen, um den Einfluss jedes einzelnen Prozesses auf die Gesamtzeit zu verstehen
* - 6
  - **Leistungs- und Verlaufsdiagramme**
    * **Liste der erfassten Modelle**: Tabelle mit Koordinaten (**X**, **Y**), Drehung (**Rot**) des Bauteils und dem **Score** (Ähnlichkeitsgrad des erkannten Objekts im Vergleich zum Referenzmodell).
    * **Parts per minute (Teile pro Minute)**: Diagramm der durchschnittlich entnommenen Teile pro Minute.
```
