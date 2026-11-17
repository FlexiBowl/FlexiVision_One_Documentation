# V. 0.23

## **Verbesserungen**

### Roboterintegration

- Der dedizierte TCP-Server für den Laser wurde entfernt: Alle Laser-Befehle und -Kommunikationen werden nun über den TCP-Client des Roboters geleitet.

## **Behobene Probleme**

### Wizard Test Air Blow und Test Flip

- Der Wizard für die Tests **Flip** und **Blow** wurde korrigiert: Die Prüfung des Motorstatus mit automatischer Aktivierung, eine anschließende Verifizierung und die Fehlerbehandlung für den Fall, dass die Aktivierung fehlschlägt, wurden hinzugefügt.
