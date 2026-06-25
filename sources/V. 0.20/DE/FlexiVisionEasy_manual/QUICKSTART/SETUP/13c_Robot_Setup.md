(robotsetup)=
# **Roboter Setup** 

In diesem Abschnitt wird das Verfahren zur Konfiguration der TCP/IP-Kommunikation zwischen dem FlexiVision One-System und dem Industrieroboter beschrieben. Um den Austausch von Koordinaten und Befehlen zwischen den beiden Systemen zu ermöglichen, ist eine gute Kommunikation unerlässlich.

```{note}
**Voraussetzungen**

Stellen Sie vor dem Fortfahren Folgendes sicher:
- Der Roboter ist eingeschaltet und betriebsbereit
- Das Ethernet-Kabel zwischen VisionController und Roboter ist angeschlossen
- Der Roboter ist so konfiguriert, dass er TCP/IP-Verbindungen akzeptiert (siehe Roboterhandbuch)
- Der im Robotercode konfigurierte Kommunikationsport ist bekannt
```

---

## Zugriff auf die Roboterkonfiguration

```{list-table}

* - **1** 
  - Klicken Sie auf der Hauptseite der Software auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - Suchen Sie auf der SETUP-Seite das Symbol **Roboter Setup** und klicken Sie darauf
    ```{dropdown} Setup-Seite 
       ![Setup-Seite](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - Die Seite zur Konfiguration der Roboterkommunikation wird geöffnet
```

---

## Übersicht über die Benutzeroberfläche Roboter-Setup

Die Seite Roboter-Setup enthält mehrere Abschnitte zum Konfigurieren und Testen der Kommunikation:
![Seite Roboter-Setup](../../../../../_shared/media/images/pagina_robotsetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Abschnitt
  - Beschreibung
* - **Port**
  - TCP/IP-Port, über den der Roboter kommuniziert (auf der Robotersteuerung konfiguriert)
* - **Reconfigure Server**
  - Schaltfläche zum Neukonfigurieren des Kommunikationsservers mit neuen Parametern
* - **Server Online**
  - Statusanzeige des FlexiVision One Servers (grün = Server aktiv und erreichbar)
* - **Client Connect**
  - Statusanzeige des Roboter-Clients (grün = Roboter verbunden)
* - **Roboter-Flexivision-Meldungen**
  - Log-Fenster, die die zwischen Roboter und FlexiVision One ausgetauschten Meldungen anzeigen (wird zum Debuggen verwendet):
      - Das erste (kleinste) Fenster zeigt die Meldungen an, die FlexiVision One oder der Bediener senden
      - Das zweite Fenster zeigt die Meldungen an, die FlexiVision empfängt
```

---
## Konfigurationsverfahren

### *Schritt 1: Eingabe des Kommunikationsports*

Der TCP/IP-Port ist der entscheidende Parameter, der zwischen Roboter und FlexiVision One übereinstimmen muss:

```{list-table}
* - **4** 
  - Geben Sie im Feld **Port** die TCP/IP-Portnummer ein, mit der der Roboter kommunizieren soll.
```
```{note}
Standardwert: (Standard-Port FlexiVision One)  
Die Portnummer muss:
   - mit der im Roboterprogramm konfigurierten übereinstimmen
   - zwischen 1024 und 65535 liegen (Benutzerports)
   - keinen Konflikt mit anderen Diensten im Netzwerk verursachen
```

```{warning}

Es ist **wichtig,** dass die Portnummer auf beiden Seiten identisch ist:
- **FlexiVision One**: Auf dieser Seite konfigurierter Port
- **Roboter**: Im Roboterprogramm konfigurierter Port

Wenn die Nummern nicht übereinstimmen, schlägt die Verbindung immer fehl.

Beispiel:
- ❌ FALSCH: FlexiVision One Port 2000, Robot Port 2001 → Keine Kommunikation
- ✅ RICHTIG: FlexiVision One Port 2000, Robot Port 2000 → Kommunikation funktioniert
```

### *Schritt 2: Neukonfiguration des Servers*

Nach der Einstellung des richtigen Ports muss der Kommunikationsserver neu gestartet werden:

```{list-table}
* - **5** 
  - Klicken Sie auf die Schaltfläche **Reconfigure Server**
* - **6**
  - Bitte warten Sie einige Sekunden, bis die Neukonfiguration abgeschlossen ist.
```

```{note}

In den folgenden Fällen müssen Sie jedes Mal auf **Reconfigure Server** klicken:
- Die Portnummer wird geändert
- Der Server soll nach einem Fehler neu gestartet werden
- Die Netzwerkkonfiguration des VisionControllers wurde geändert
- Der Abbruch bestehender Verbindungen soll erzwungen werden

Der Server startet beim Öffnen der FlexiVision One-Software automatisch, muss jedoch nach Änderungen manuell neu konfiguriert werden.
```

### *Schritt 3: Serverstatus überprüfen*

Überprüfen Sie nach der Neukonfiguration, ob der Server aktiv ist:

```{list-table}

* - **7**
  - Beobachten Sie die Anzeige **„Server Online“**:
   - **Grün**: Server aktiv   
     **Rot**: Server nicht aktiv  
* - **8**
  - Nachdem Sie das Programm vom Roboter aus gestartet haben, beobachten Sie die Anzeige **Client Online**:
   - **Grün**: Roboter verbunden  
     **Rot**: Roboter nicht verbunden 

```
```{note}
Wenn die Anzeigen grün leuchten, ist das System ordnungsgemäß angeschlossen. 

Wenn eine der Anzeigen rot leuchtet, überprüfen Sie Folgendes:
   - Überprüfen Sie, ob das Programm auf dem Roboter gestartet wurde
   - Überprüfen Sie, ob sich die IP-Adressen im selben Subnetz befinden
   - Überprüfen Sie, ob der Port nicht bereits von einem anderen Programm verwendet wird
   - Überprüfen Sie die Systemprotokolle auf Fehlermeldungen
```
### *Schritt 4: Speichern und Abschluss*

```{list-table}
:header-rows: 0
:widths: 10 90

* - **9**
  - Überprüfen Sie, ob die Verbindung zwischen Roboter und FlexiVision One stabil ist

* - **10**
  - Die Kommunikationsparameter werden automatisch gespeichert

* - **11**
  - Kehren Sie zur **SETUP-**Hauptseite zurück
```

---

## Nächste Schritte

Sobald das Roboter-Setup abgeschlossen ist, fahren Sie fort mit:

- [Protocol Setup](protocol_setup)
- [Rezept speichern](ricettabase)


