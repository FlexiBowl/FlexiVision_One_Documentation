(fbsetup)=
# **FlexiBowl® Setup**

In diesem Abschnitt wird beschrieben, wie Sie den FlexiBowl® an das FlexiVision One-System anschließen und konfigurieren.

```{note}
**Voraussetzungen**

Stellen Sie Folgendes sicher:
- Die mechanische Installation aller Komponenten ist abgeschlossen ([Mechanische Installation](Installazione_Meccanica))
- Alle Kabel sind korrekt angeschlossen ([Verkabelung und Anschlüsse](cablaggio)) 
```

---

## Zugriff auf die FlexiBowl®-Konfiguration
```{list-table}
* - **1** 
  - Klicken Sie auf der Startseite der Software auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Suchen Sie auf der SETUP-Seite das Symbol **FlexiBowl® Setup** und klicken Sie darauf
    ```{dropdown} Setup-Seite 
       ![Setup-Seite](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - Der Konfigurationsbildschirm für den FlexiBowl® wird geöffnet
```
![FlexiBowl® Setup-Seite](../../../../../_shared/media/images/pagina_FBsetup.png)
---

## Verbindungsvorgang

### *Schritt 1: Konfiguration der Netzwerkadresse*

```{list-table}
* - **4**
  - Stellen Sie sicher, dass sich die Adresse im selben Subnetz wie der VisionController befindet.
  
* - **5**
  - Geben Sie im Feld **FlexiBowl® IP** die IP-Adresse des FlexiBowl® ein
      - Format: `192.168.1.XXX` (oder abhängig von Ihrer Netzwerkkonfiguration)
```
:::{tip}
Der Einfachheit und der Einheitlichkeit halber beginnen Sie bitte mit dem ersten verfügbaren FlexiBowl®.
:::
:::{note}
Der FlexiBowl® wird mit einer Standard-IP-Adresse ausgeliefert. `192.168.1.10`
:::
:::{important}
Anweisungen zum Ändern der IP-Adresse des FlexiBowl® finden Sie im Handbuch, das im [Downloads](https://www.flexibowl.co.uk/downloads)-Bereich verfügbar ist.
:::

### *Schritt 2: Verbindungstest*

```{list-table}
:widths: 5 95

* - **6**
  - Klicken Sie nach Eingabe der IP auf die Schaltfläche **Connection Test**

* - **7**
  - Das System führt einen Kommunikationstest (Ping) mit der FlexiBowl® durch

* - **8**
  - Beobachten Sie die **Statusanzeige**:
    - 🟢 **Grün**: Verbindung erfolgreich hergestellt
    - 🔴 **Rot:** Verbindung fehlgeschlagen (IP-Adresse und Verkabelung prüfen)
```

```{warning}
**Verbindung fehlgeschlagen**

Wenn die Anzeige rot bleibt oder eine Fehlermeldung erscheint:

0. Überprüfen Sie, ob der FlexiBowl® eingeschaltet ist
1. Überprüfen Sie, ob die eingegebene IP-Adresse korrekt ist
2. Überprüfen Sie das Ethernet-Kabel auf physische Fehler (es muss vollständig eingesteckt sein)
3. Falls vorhanden, überprüfen Sie, ob der Netzwerk-Switch/Router eingeschaltet ist
4. Stellen Sie sicher, dass sich FlexiBowl® und VisionController im selben Subnetz befinden
5. Versuchen Sie, den FlexiBowl® von einem Windows-Terminal aus anzupingen:
   - Öffnen Sie die Eingabeaufforderung
   - Geben Sie ein: `ping 192.168.1.XXX` (durch tatsächliche IP-Adresse ersetzen)
   - Wenn der Ping fehlschlägt, liegt ein Netzwerkproblem vor

Wenn das Problem weiterhin besteht, lesen Sie den Abschnitt [Troubleshooting](troubleshooting).
```

---

## Konfiguration der FlexiBowl®-Parameter

Sobald die Verbindung hergestellt ist, fahren Sie mit der Konfiguration der Betriebsparameter fort.

### *Schritt 3: Zugriff auf die Konfiguration*

```{list-table}
* - **9** 
  - Klicken Sie auf die Schaltfläche <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **10**
  - Es öffnet sich ein Fenster mit den konfigurierbaren Parametern des FlexiBowl®.
```


### *Schritt 4: Parametersynchronisierung*

```{list-table}

* - **12**
  - Klicken Sie auf **Synchronize Parameters**
* - **13**
  - Kehren Sie zur SETUP-Hauptseite zurück, um mit der nächsten Einstellung fortzufahren 
```
:::{important}
I parametri possono essere regolati tramite slider oppure inseriti manualmente da tastiera nel relativo campo numerico.
:::

```{warning}
**Die Synchronisierung nicht auslassen**

Es ist wichtig, nach jeder Änderung auf **Synchronize Parameters** zu klicken. Ohne diesen Schritt:
- werden die Änderungen nicht auf den FlexiBowl® angewendet
- kann das System unvorhersehbar reagieren
- werden die Einstellungen nicht gespeichert 
```
---
(configfb)=
# **Konfigurationsassistent: FlexiBowl® Wizard**


Die Benutzeroberfläche des **FlexiBowl®-Wizard** ist ein interaktives Tool, das den Benutzer bei der Konfiguration der Zuführparameter entsprechend der jeweiligen Produktfamilie, die verwaltet werden soll, unterstützt.

## Schritt 1: Zugriff auf den Wizard

So starten Sie den Vorgang:
```{list-table}
:widths: 5 95

* - **1**
  - Gehen Sie auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon"> in der FlexiVision One Software

* - **2**
  - Klicken Sie auf die Schaltfläche **FlexiBowl® Setup**. Es öffnet sich eine Seite mit allen FlexiBowl®-Geräten, die mit FlexiVision One verwaltet werden können

    :::{dropdown} FlexiBowl®-Setup-Seite  
    ![FlexiBowl® Setup-Seite](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **3**
  - Klicken Sie auf die Schaltfläche <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl">. Es öffnet sich eine Seite mit allen für den ausgewählten FlexiBowl verfügbaren Bewegungsabläufen

    :::{dropdown} Seite Konfiguration FlexiBowl®  
    ![Seite FlexiBowl® Konfig](../../../../../_shared/media/images/pagina_FBsetup.png)
    :::

* - **4**
  - Klicken Sie auf die Schaltfläche **FlexiBowl® X Wizard**; es öffnet sich eine Willkommensseite des Assistenten

* - **5**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small">
    
    :::{note}
    Klicken Sie <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small"> auf jeder Seite des Assistenten, um in der geführten Einrichtung fortzufahren.
    :::
```

## Schritt 2: Auswahl von Modell und Drehung

In dieser Phase werden die Hardware-Eigenschaften des Systems festgelegt:
```{list-table}
* - **6**
  - Wählen Sie die Größe des Geräts aus (z. B. 200, 350, 500, usw.).
* - **7**
  - Bestimmen Sie die Drehrichtung der Scheibe (**Clockwise** oder **CounterClockwise**).
```
## Schritt 3: Charakterisierung der Komponente

Das System benötigt Informationen zur Morphologie der Teile, um die Trennung zu optimieren.
````{list-table}
* - **8**
  - Wählen Sie die Größe der Komponente:**

    **Für FlexiBowl-Modelle 200, 350, 500, 650:**

    :::{card}
    <= 150mm
    :::

    :::{card}
    &gt; 150mm
    :::

    **Für die FlexiBowl-Modelle 800 und 1200:**

    :::{card}
    <= 250mm
    :::

    :::{card}
    &gt; 250mm
    :::

* - **9**
  - Wählen Sie die Geometrie aus, die das Teil am besten beschreibt:
      * **FLAT**: Flache Komponenten.
      * **CYLINDRICAL**: Zylindrische Komponenten.
      * **COMPLEX**: Komplizierte oder unregelmäßige Geometrien

      ![Flat Cylindrical or Complex](../../../../../_shared/media/images/flatorcomplex.png)

      *Beispiele für Geometrien: Flat, Cylindrical und Complex.*

* - **10**
  - Legen Sie fest, wie die Teile auf der Oberfläche miteinander interagieren:
      * **Overlapping**: Die Teile neigen dazu, sich zu überlappen.
      * **Not Overlapping**: Die Teile überschneiden sich nicht.
      * **Tangling / Stacking**: Die Teile neigen dazu, sich zu verhaken oder zu stapeln.
      * **Not Tangling / Not Stacking**: Die Teile bleiben getrennt und verhaken sich nicht.

      ![Overlapping](../../../../../_shared/media/videos/overlapping.gif)

      *Not Overlapping: Die Teile überschneiden sich nicht auf der Oberfläche.*

      ::::{grid} 2
      :::{grid-item}
      ![Stacking](../../../../../_shared/media/videos/stacking.gif)

      *Stacking: Die Teile stapeln sich.*
      :::
      :::{grid-item}
      ![Tangling](../../../../../_shared/media/videos/tangling.gif)

      *Tangling: Die Teile verhaken sich ineinander.*
      :::
      ::::
````
## Schritt 4: Zubehörtest
```{list-table}
* - **11**
  - Wählen Sie aus dem Dropdown-Menü, ob die FlexiBowl® mit dem **Air-blow-Modul** ausgestattet ist.
* - **12**
  - Klicken Sie auf **TEST Air-blow**, um den Betrieb zu überprüfen.
* - **13**
  - Wählen Sie **USE**, um es in der aktuellen Anwendung zu aktivieren, andernfalls klicken Sie auf **DON'T USE**.
* - **14**
  - Klicken Sie auf **TEST FLIP**, um die tatsächliche Aktivierung des Stößels zu überprüfen.
      Der "Flip" ist die Einheit, die den mechanischen Impuls zum Wenden der Teile erzeugt; sie ist für das Trennen, Entwirren oder Wenden der Teile während des Zuführzyklus unerlässlich.
 
      :::{important}
      Wenn der Impuls nicht spürbar ist, überprüfen Sie, ob die Druckluft angeschlossen ist, und stellen Sie am mechanischen Druckregler am Bedienfeld ein.
      :::
* - **15**
  - Am Ende des Assistenten berechnet das System nach einem Klick auf **FINISH** automatisch die Parameter: 
    - Bewegungsparameter (Geschwindigkeit, Beschleunigung, Winkel)
    - Rüttelparameter (Shake)
    - Zubehör-Zeitsteuerungen (Flip, Blow)
* - **16**
  - Anschließend können diese in der Übersichts-Dashboard fein abgestimmt werden.
```
```{list-table} Panoramica Parametri
   :widths: 20 30 50
   :header-rows: 1

   * - Gruppe
     - Parameter
     - Beschreibung
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Parameter für die Hauptbewegung der Scheibe.
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Verwaltung der Auslösezeiten des Zubehörs.
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Parameter der Rüttelbewegung (Trennung).
```

## Schritt 5: Validierung der Sequenz

Verwenden Sie die Funktion **Test Sequence**, um zu prüfen, ob der Zyklus die folgenden Effizienzkriterien erfüllt:
```{list-table}
:widths: 5 95
:header-rows: 0

* - **Synchronisation**
  - Der Flip-Impuls muss genau in dem Moment enden, in dem die Bewegung (*Move*) endet. Passen Sie die Werte für *Flip Count* und *Delay* an, um sie aufeinander abzustimmen.

* - **Bildstabilität**
  - Die Komponenten müssen stillstehen, wenn die Kamera ausgelöst wird.
    - Wenn sich die Teile bewegen, verringern Sie Geschwindigkeit/Beschleunigung oder fügen Sie eine Pause ein (z. B. `pause 200ms`).

* - **Positionierung der Teile während der Sequenz**
  - Während der Bewegung müssen die Teile zur Mitte des FlexiBowl®-Radius befördert werden, um die Wirksamkeit des Flip zu maximieren. Am Ende der Sequenz sollten die Stücke ungefähr in der Mitte des Sichtfeldes angeordnet sein.
```

:::{warning}
Klicken Sie nach jeder manuellen Änderung immer auf **Synchronize Parameters**, damit die Änderungen im Controller wirksam werden.
:::
:::{important}
Nel caso in cui i parametri venissero modificati ma non sincronizzati, apparirà un messaggio di avviso. 
:::

## Übersicht über die FlexiBowl®-Parameter
```{list-table}
:header-rows: 1
:widths: 5 25 70

* - ID
  - Element
  - Beschreibung
* - 1
  - MOVE – Beschleunigung
  - Beschleunigungswert, der bei jedem MOVE-Befehl verwendet wird
* - 2
  - MOVE – Verzögerung
  - Verzögerungswert, der bei jedem MOVE-Befehl verwendet wird
* - 3
  - MOVE – Geschwindigkeit
  - Geschwindigkeitswert (U/min), der bei jedem MOVE-Befehl verwendet wird
* - 4
  - MOVE – Winkel
  - Winkel, in dem sich der FlexiBowl® bei jedem MOVE-Befehl bewegt
* - 5
  - SHAKE – Beschleunigung
  - Beschleunigungswert, der bei jedem SHAKE-Befehl verwendet wird
* - 6
  - SHAKE – Verzögerung
  - Verzögerungswert, der bei jedem SHAKE-Befehl verwendet wird
* - 7
  - MOVE – Geschwindigkeit
  - Geschwindigkeitswert (U/min), der bei jedem SHAKE-Befehl verwendet wird
* - 8
  - MOVE – CW-Winkel
  - Winkel im Uhrzeigersinn, in dem sich der FlexiBowl® bei jedem SHAKE-Befehl bewegt
* - 9
  - MOVE – CCW-Winkel
  - Winkel entgegen dem Uhrzeigersinn, in dem sich der FlexiBowl® bei jedem SHAKE-Befehl bewegt
* - 10
  - OPTION – Flip-Zählung
  - Anzahl der Flip-Aktivierungen, die durchgeführt werden
* - 11
  - OPTION – Flip-Verzögerung
  - Zeit (in Millisekunden) zwischen einer Aktivierung und einer Deaktivierung des Flips
* - 12
  - OPTION – Blow-Zeit
  - Zeit (in Millisekunden) für die Aktivierung des Blows
* - 13
  - OPTION – Licht ein
  - Drücken, um die Hintergrundbeleuchtung zu aktivieren/deaktivieren
```

```{tip}
**Produktionstest**

Vor dem Einsatz in der Produktion:
1. Führen Sie 50-100 Testzyklen durch, um die Konsistenz zu prüfen
2. Überwachen Sie die Füllrate der Scheibe (sie muss konstant sein)
3. Stellen Sie sicher, dass keine ungewöhnlichen Ansammlungen oder anhaltende leere Bereiche vorhanden sind
4. Schrittweise Erhöhung der Produktionsgeschwindigkeit

Die optimale Konfiguration kann 2-3 Feinabstimmungs-Sitzungen mit dem tatsächlichen Teil in nennenswerter Stückzahl erfordern.
```

## Nächste Schritte

Nach Abschluss des FlexiBowl®-Setups fahren Sie fort mit:

- [Trichter-Setup](13b_Hopper_Setup.md)
- [Roboter-Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Rezept speichern](ricettabase)




