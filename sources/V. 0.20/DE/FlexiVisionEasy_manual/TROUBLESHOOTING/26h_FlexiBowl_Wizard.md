(troubleshooting_fb_wizard)=
# **FlexiBowl Wizard**

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Wizard startet nicht**
  - • Rezeptur nicht geladen
    
    • FlexiBowl nicht verbunden
    
    • Initiales Setup nicht abgeschlossen
  - • Zuerst Rezeptur laden oder erstellen
    
    • FlexiBowl-Verbindung prüfen
    
    • Grundkonfiguration des Systems abschließen

* - **Eingestellte Drehrichtung stimmt nicht überein**
  - • Fehler bei der Auswahl CW/CCW
    
  - • Tatsächliche Drehrichtung visuell prüfen
    
    • Auswahl im Wizard korrigieren
    
* - **Air-blow Test funktioniert nicht**
  - • Druckluft nicht angeschlossen
    
    • Druck unzureichend
    
    • Modul physisch nicht vorhanden
  - • Druckluftanschluss prüfen
    
    • Druck auf 5-6 bar erhöhen
    
    • "FlexiBowl NOT equipped" auswählen, wenn das Modul fehlt
* - **Flip Test nicht wahrnehmbar**
  - • Druckluft nicht angeschlossen/unzureichend
    
    • Druckregler geschlossen
    
    • Leckagen im Pneumatikkreis
  - • Prüfen, ob Druckluft angeschlossen ist
    
    • Regler am Bedienfeld öffnen
    
    • Druck 5-6 bar prüfen
    
    • Anschlüsse auf Leckagen prüfen
* - **Berechnete Parameter nicht optimal**
  - • Falsche Komponentencharakterisierung
    
    • Wizard verwendet generische Werte
  - • Ausgewählte Geometrie und Verhalten überprüfen
    
    • Wizard-Parameter als Ausgangspunkt akzeptieren
    
    • Manuell im Übersichts-Dashboard verfeinern

* - **Komponenten bewegen sich während der Aufnahme**
  - • Geschwindigkeit/Beschleunigung zu hoch
    
    • Stabilisierungspausen fehlen
    
    • Grip-Oberfläche nicht geeignet
  - • Speed und Accel verringern
    
    • Pausen von 200-500ms einfügen
    
    • Grip-Oberfläche durch eine haftfähigere ersetzen
* - **Luftstoß nicht wirksam**
  - • Luftdruck unzureichend/übermäßig
    
    • Düsen verstopft
  - • Druck 5-6 bar prüfen
    
    • Air-blow-Düsen reinigen

* - **Parameteränderungen werden nicht angewendet**
  - • "Synchronize Parameters" nicht gedrückt
    
    • Rezeptur nicht gespeichert
  - • Nach Änderungen **IMMER** Synchronize Parameters klicken
    
    • Rezeptur speichern, um Änderungen dauerhaft zu machen
* - **Turn FLB funktioniert während des Setups nicht**
  - • FlexiBowl nicht verbunden
    
    • Befehl nicht konfiguriert
    
    • FlexiBowl in Fehlerzustand
  - • FlexiBowl-Verbindung prüfen
    
    • FlexiBowl Setup Konfiguration prüfen
    
    • FlexiBowl READY-LED prüfen
```
