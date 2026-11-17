# V. 0.24

## **Neue Funktionen**

### Kontrollkameras

- Die Verwaltung von **3 unabhängigen Kontrollkameras** wurde hinzugefügt, die FLB1, FLB2 bzw. FLB3 zugeordnet sind.
- Der Roboterbefehl `start_control_` wurde implementiert, mit Unterstützung benutzerdefinierter Parameter, die an die VisionPro-Skripte weitergeleitet werden.
- Die Verwaltung anpassbarer VisionPro-Skripte wurde hinzugefügt, mit Textausgabe und `CogRecord`-Bildern einschließlich der grafischen Ergebnisse.
- Es wurden eigene Main Tasks für die Kontrollkameras implementiert, mit Fehlerbehandlung, Logging und Übermittlung der Ergebnisse an den Roboter.
- Die Ausführung der Kontrollen wurde auch ohne verbundenen Roboter ermöglicht, um lokale Tests über die HMI durchzuführen.
- Gemeinsame HMI-Seiten für die Kamerakonfiguration, die VisionPro-Konfiguration und die Runtime-Anzeige der drei Kontrollkameras wurden hinzugefügt.

## **Verbesserungen**

### Clearances (Histogramme)

- Die Regionsverwaltung für alle 8 Modelle, 8 Histogramme und 3 Kameras wurde aktualisiert; Position, Größe und Geometrie der gespeicherten ROIs bleiben dabei erhalten.

## **Behobene Probleme**

### Rezepte

- Das Zurücksetzen der ROIs der Histogramme beim Rezeptwechsel wurde behoben.
