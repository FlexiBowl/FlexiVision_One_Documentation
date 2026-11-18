# Handbuch FlexiVision One

Diese Seite enthält die Revisionshistorie dieses Handbuchs und gibt an, mit welchen Versionen der Software FlexiVision One die jeweilige Revision kompatibel ist.

```{important}
Verwenden Sie stets die Handbuchversion, die mit der installierten Softwareversion kompatibel ist, um Zugriff auf die aktuellsten Informationen zu Funktionen, Sicherheit und Verfahren zu erhalten.
```

## Kompatibilität

| Handbuchversion | Kompatible Versionen der Software FlexiVision One |
|---|---|
| **1.02** (aktuell) | v0.23, v0.24 |
| **1.01** | v0.21, v0.22 |
| **1.00** | v0.20, v0.21, v0.22 |

## Revisionshistorie

### Version 1.02

Veröffentlichungsdatum: 17.11.2026

**Hinzugefügte Seiten**

- Neuer Abschnitt **Kontrollkameras** mit den Seiten:
  - [Kontrollkameras](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md): Überblick, Funktionsablauf, Verwendung über die HMI (Setup Camera Ctrl, Setup Tool Ctrl, View Runtime, Test Tool) und schneller Abnahmetest.
  - [Befehl `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md): Befehlsformat, Parameter, Antworten an den Roboter und Beispiele für den Datenaustausch.
  - [VisionPro-Skript](../TELECAMERE_CONTROLLO/35_Script_VisionPro.md): ToolBlock-Schnittstelle, Anpassung des Skripts und Anhang A mit dem vollständigen C#-Skript.
- Die Seite [Fehlerbehebung – Kontrollkameras](../TROUBLESHOOTING/26j_Telecamere_Controllo.md) mit den Meldungen `#Error_Control_…` und `#Error_Camera…` und den empfohlenen Maßnahmen wurde hinzugefügt.
- Alle Seiten des Abschnitts Kontrollkameras zeigen oben einen Hinweis, dass die **Control Camera** eine **Expert**-Funktion ist.

**Aktualisierte Seiten**

- [Kommunikationsprotokoll Roboter–Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): Der Unterabschnitt „Befehle für Kontrollkameras“ mit dem Befehl `start_control_<Parameter>` wurde hinzugefügt.
- [Fehlerbehebung](../TROUBLESHOOTING/26_trb_shooting_guide.md): Die Karte „Kontrollkameras“ wurde hinzugefügt.
- [Glossar](../27b_Glossario.md): Die Begriffe CogRecord, PMRedLine, Kontrollkamera, ToolBlock und VisionPro wurden hinzugefügt.
- Versionshinweise – Software: Die Versionen [V. 0.23](V.0.23.md) und [V. 0.24](V.0.24.md) wurden hinzugefügt und die Seite [Software FlexiVision One](Release_Notes_Software.md) wurde aktualisiert.
- Die Kompatibilitätstabelle wurde um die Softwareversionen v0.23 und v0.24 ergänzt.

### Version 1.01

Veröffentlichungsdatum: 04.09.2026

- Die Seite **Check Belt** (Bandüberwachung) wurde in den Quickstart aufgenommen, ebenso der zugehörige Eintrag auf der Setup-Seite der Oberflächenübersicht.
- Der Abschnitt Hopper Setup wurde um die geführten Abläufe **Wizard Steps** und **Wizard Time** erweitert.
- Der Abschnitt Histogramme wurde um die Auswahl des Regionstyps für die Clearances (Rectangle, Annulus Section, Circle) ergänzt.
- Der Abschnitt Mix-Anwendungen wurde um die Multi-Modell-Befehle `mix_Locator_<Modelle>` und den Schutz für bereits laufende Befehle ergänzt.
- Dem Kommunikationsprotokoll Roboter-Vision wurde der Unterabschnitt „Richtige Verwendung der Befehle Start und Mix“ hinzugefügt.
- Der Abschnitt FlexiBowl® Setup wurde aktualisiert: manuelle Eingabe der Parameter über die Tastatur und Warnhinweis bei nicht synchronisierten Parametern.
- Der Abschnitt Robot Pick wurde aktualisiert: Offset-Format mit dem Punkt als Dezimaltrennzeichen und Prüfung des Picking Offset, bevor mit **Next** fortgefahren werden kann.
- Dem Abschnitt Setup wurde der Hinweis zur Prüfung der Benutzerzugriffsebene hinzugefügt.
- Der Abschnitt Versionshinweise wurde neu organisiert: Die Hinweise zur Software FlexiVision One sind nun von denen zum Handbuch getrennt.

### Version 1.00

Veröffentlichungsdatum: 01.08.2026

- Erstausgabe des Handbuchs.
