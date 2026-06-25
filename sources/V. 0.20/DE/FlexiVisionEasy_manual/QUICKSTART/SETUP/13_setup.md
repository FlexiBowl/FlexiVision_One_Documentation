(setupcomponenti)=
# **Erstkonfiguration des Systems**

Dieser Abschnitt führt den Benutzer durch die vollständige Konfiguration der Hardware- und Softwarekomponenten des FlexiVision One-Systems. Es ist unbedingt erforderlich, die Schritte in der angegebenen Reihenfolge zu befolgen, um den ordnungsgemäßen Betrieb des Systems zu gewährleisten.

```{note}
**Voraussetzungen**

Bevor Sie mit der Softwarekonfiguration beginnen, müssen Sie Folgendes sicherstellen:
- Die mechanische Installation aller Komponenten ist abgeschlossen ([Mechanische Installation](Installazione_Meccanica))
- Alle Kabel sind korrekt angeschlossen ([Verkabelung und Anschlüsse](cablaggio)) 
```
![WorkFlow](../../../../../_shared/media/images/workflow.png)
---

## Überblick über den Einrichtungsprozess

Der anfängliche Konfigurationsprozess besteht aus sieben Hauptschritten:

0. **Eingabe des** im Kit enthaltenen **Lizenzschlüssels**
1. **Login** - Zugriff auf die Software mit den Benutzerdaten
2. Falls vorhanden: Backlight-Beleuchtung: **Konfiguration der FlexiBowl®-IP-Adresse** und **Einschalten des Backlights** 
3. **Kamera Setup** - Konfiguration der Kamera
4. **FlexiBowl Setup** - Anschluss und Konfiguration des FlexiBowl®
5. **Trichter-Setup**  - Konfiguration des Trichters 
6. **Roboter-Setup** - Konfiguration der Kommunikation mit dem Roboter
7. **Protocol Setup** - Konfiguration der Protokollparameter
8. **Umbenennen und Speichern des Grundrezepts** - Konfiguration des Anwendungsprofils



```{warning}
**Reihenfolge der Schritte**

Die Reihenfolge der Einstellungen ist wichtig! Überspringen Sie keine Schritte und ändern Sie die Reihenfolge nicht, da einige Konfigurationen von den vorherigen abhängen.
```

---

## Vorbereitende Schritte

:::{important}
Der erste Schritt vor dem Start der FlexiVision One-Software ist die Eingabe des mit dem Kit gelieferten Lizenzschlüssels. 
:::

### *Anmeldung am System*

Beim Start der FlexiVision One-Software wird die Startseite angezeigt. 
```{list-table} 
   :widths: 10 90
   :header-rows: 0
   * - **0**
     - Klicken Sie auf Setup 
   * - **1**
     - **Wählen Sie den Benutzer ENGINEER** aus dem Dropdown-Menü oben rechts aus.
   * - **2**
     - **Geben Sie das Passwort** '3' ein.
   * - **3**
     - Klicken Sie auf die Schaltfläche **LOGIN** , um auf die Benutzeroberfläche zuzugreifen.
```

```{tip}
**Benutzerverwaltung**

FlexiVision One unterstützt mehrere Benutzerprofile mit unterschiedlichen Berechtigungsstufen:
- **ARS**
- **Engineer**
- **Technician**
- **Operator**
```

---

### *Backlight einschalten, falls vorhanden*

Wenn nach der ersten Anmeldung die FlexiVision One-Lizenz aktiviert werden muss, befolgen Sie diese Schritte: 

```{list-table}
* - **4** 
  - Klicken Sie auf der Hauptseite der Software auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **5**
  - Auf der Seite „SETUP“ das Symbol **FlexiBowl®-Setup** identifizieren und anklicken
    ```{dropdown} Setup-Seite 
       ![Setup-Seite](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **6**
  - Die Seite zur Konfiguration des FlexiBowl® öffnet sich
* - **7**
  - Geben Sie die IP-Adresse des FlexiBowl® ein (Standard: `192.168.1.10` )
* - **8**
  - Klicken Sie nach Eingabe der IP-Adresse auf die Schaltfläche **Connection Test**
* - **9**
  - Das System führt einen Kommunikationstest (Ping) mit dem FlexiBowl® durch.
* - **10**
  - Beachten Sie die **Statusanzeige**:
    - 🟢 **Grün**: Verbindung erfolgreich hergestellt
    - 🔴 **Rot:** Verbindung fehlgeschlagen (IP-Adresse und Verkabelung prüfen)
* - **11** 
  - Klicken Sie auf die Schaltfläche <img src="../../../../../_shared/media/images/FB_config1.png" class="inline-icon icon-xl" >
* - **12**
  - Es öffnet sich ein Fenster mit den konfigurierbaren Parametern des FlexiBowl®.
* - **13**
  - Schalten Sie das Backlight ein, indem Sie das Kontrollkästchen „Light ON“ aktivieren.
```

---

## Konfiguration der Hardwarekomponenten

Sobald die vorbereitenden Schritte abgeschlossen sind, fahren Sie mit der Konfiguration der Hardwarekomponenten in der folgenden Reihenfolge fort.

Alle Hardware-Einstellungen sind über die zentrale **SETUP-Seite** der Software zugänglich.


```{list-table} 
* - **14** 
  - Klicken Sie im Hauptmenü auf <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **15** 
  - Es werden Symbole für die verschiedenen zu konfigurierenden Komponenten angezeigt.
* - **16**
  - Klicken Sie auf das Symbol der gewünschten Komponente, um auf deren spezifische Konfiguration zuzugreifen.
```

---

```{toctree}
:hidden:
13d_Camera_Setup.md
14_calibrazione_camera.md
13a_FB_Setup.md
13b_Hopper_Setup.md
13c_Robot_Setup.md
15_Protocol_Setup.md
15b_SaveRecipe.md
```

