(troubleshooting_conf_tramoggia)=
# **Trichter-Konfiguration** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen

* - **Kontrollbereich nicht definierbar**
  - • Bild nicht erfasst
    
    • Falscher Abschnitt
  - • Testbild erfassen
    
    • Zugriff über Config Hopper X


* - **AUTO berechnet Mittelwert und Standardabweichung nicht korrekt**
  - • CAPTURE nicht ausgeführt
    
    • CAPTURE-Reihenfolge vertauscht
    
    • Kontrollbereich zu klein
  - • Leeren CAPTURE ausführen, dann vollen CAPTURE
    
    • In der richtigen Reihenfolge wiederholen
    
    • Kontrollbereich vergrößern
* - **TEST immer GRÜN (Trichter wird nie aktiviert)**
  - • Schwellenwert zu großzügig
    
    • Voller CAPTURE mit zu vielen Komponenten
    
    • Mean falsch berechnet
  - • Voller CAPTURE mit korrekter Mindestanzahl wiederholen
    
    • Überprüfen, ob AUTO korrekt neu berechnet
    
    • Schwellenwert bei Bedarf manuell anpassen
* - **TEST immer ROT (Trichter wird immer aktiviert)**
  - • Schwellenwert zu restriktiv
    
    • Leerer CAPTURE mit vorhandenen Komponenten
    
  - • Leeren CAPTURE mit vollständig gereinigtem Bereich wiederholen
    
    • AUTO wiederholen

* - **Vibrationszeit erzeugt nicht den gewünschten Effekt**
  - • Wert zu niedrig
    
    • Wert zu hoch
    
    • Variabler Trichterfüllstand
  - • Start mit 500ms
    
    • Um ±100 ms erhöhen, um den Durchfluss anzupassen
    
    • **KRITISCH**: Konstante Beladung im Behälter aufrechterhalten

* - **Trichter entleert zu falschen Zeitpunkten**
  - • Steps nicht korrekt

    • Hardware der Trichter-Steuerung nicht korrekt konfiguriert

  - • Steps neu berechnen

    • Konfigurationsspezifikationen im [Handbuch für den Trichter]() überprüfen
```

