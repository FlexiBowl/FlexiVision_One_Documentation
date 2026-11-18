(telecamere_controllo)=
# **Kontrollkameras**

```{important}
**Expert-Funktion**

Die Verwaltung der Kontrollkameras (**Control Camera**) ist eine **Expert**-Funktion: Sie erfordert Kenntnisse in Cognex VisionPro und C#-Skripten und richtet sich an erfahrene Anwender. Informationen zum Expert-Modus finden Sie unter [Worum es sich handelt und wann es benötigt wird](../EXPERT/32_Expert.md).
```

```{note}
**Verfügbar ab Softwareversion v0.24**

Die in diesem Abschnitt beschriebenen Funktionen wurden mit FlexiVision One v0.24 eingeführt. Siehe [Versionshinweise – V. 0.24](../APPENDICI/V.0.24.md).
```

Zusätzlich zur Vision-Kamera, die für das Greifen verwendet wird, verwaltet FlexiVision One **3 unabhängige Kontrollkameras**, die jeweils **FLB1**, **FLB2** und **FLB3** zugeordnet sind. Mit den Kontrollkameras kann auf Anforderung des Roboters eine **Sichtprüfung** durchgeführt werden, zum Beispiel die Kontrolle eines gegriffenen Teils, und das Prüfergebnis an den Roboter zurückgegeben werden.

## Wozu es dient

Mit dem Befehl `start_control_` kann der Roboter bei FlexiVision eine Prüfung mit einer Kontrollkamera anfordern. Der Roboter kann nach dem Unterstrich (`_`) einen **Textparameter** anhängen: FlexiVision leitet den Parameter an das **VisionPro-Skript** weiter, das entscheidet, welche Tools ausgeführt und welche Ergebnisse zurückgegeben werden.

```{important}
**Funktionsprinzip**

Die HMI-Konfiguration bleibt unverändert: Der Kunde kann die Prüfregeln und das Ergebnisformat anpassen, indem er sein eigenes **VisionPro-Skript** bearbeitet, ohne die Oberfläche von FlexiVision One zu ändern.
```

## Funktionsablauf

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - #
  - Akteur
  - Aktion
* - 1
  - **Roboter**
  - Sendet `start_control_` oder `start_control_<Parameter>`.
* - 2
  - **FlexiVision**
  - Nimmt das Bild mit der zugeordneten Kontrollkamera auf und startet das VisionPro-Skript.
* - 3
  - **VisionPro**
  - Führt die ausgewählten Tools aus und erstellt eine Textantwort und einen Grafikdatensatz.
* - 4
  - **FlexiVision**
  - Zeigt Bild und Zeichenfolge in der HMI an; sendet die Zeichenfolge **nur bei bestehender Verbindung** an den Roboter.
```

Für jede Prüfung verwaltet FlexiVision einen eigenen **Main Task** für die Kontrollkamera, mit Fehlerbehandlung, Logging und Übermittlung der Ergebnisse an den Roboter.

## Verwendung über die HMI

Die HMI-Seiten der Kontrollkameras werden von den Geräten **gemeinsam genutzt**: Wählen Sie im Bereich **Control FlexiBowl®** das gewünschte Gerät aus.

```{list-table}
:header-rows: 1
:widths: 25 75

* - Seite
  - Funktion
* - **Setup Camera Ctrl**
  - Konfiguration der Kontrollkamera.
* - **Setup Tool Ctrl**
  - VisionPro-Konfiguration: ermöglicht Eingriffe in die Tools und in das VisionPro-Skript (siehe [VisionPro-Skript](35_Script_VisionPro.md)).
* - **View Runtime**
  - Anzeige von Bild und Prüfergebnis.
* - **Test Tool**
  - Startet eine lokale Prüfung, auch ohne angeschlossenen Roboter.
```

```{note}
Mit dem Befehl **Test Tool** wird die Prüfung auch **ohne verbundenen Roboter** ausgeführt: In diesem Fall wird das Ergebnis in der HMI angezeigt, aber **nicht über TCP übertragen**.
```

## Schneller Abnahmetest

Führen Sie nach der Installation oder Änderung des VisionPro-Skripts die folgenden Prüfungen durch:

- ☐ `start_control_1` senden und Textergebnis sowie Bild von PMRedLine 1 prüfen.
- ☐ `start_control_2` senden und Textergebnis sowie Bild von PMRedLine 2 prüfen.
- ☐ `start_control_` senden und prüfen, dass die Zeichenfolge beide Ergebnisse enthält.
- ☐ `start_control_ABC` senden und den Fehler `INVALID_CONTROL` des Beispielskripts prüfen.
- ☐ **Test Tool** bei getrenntem Roboter ausführen und prüfen, dass HMI und VisionPro betriebsbereit bleiben.

## Weiterführende Informationen

- [Befehl `start_control_`](34_Comando_start_control.md): Befehlsformat, Parameter, Antworten und Beispiele für den Datenaustausch.
- [VisionPro-Skript](35_Script_VisionPro.md): Skriptschnittstelle, Anpassung und vollständiger Beispielcode.
- [Fehlerbehebung – Kontrollkameras](../TROUBLESHOOTING/26j_Telecamere_Controllo.md): Fehlermeldungen und empfohlene Maßnahmen.
- [Kommunikationsprotokoll Roboter–Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): vollständige Liste der Roboterbefehle.
