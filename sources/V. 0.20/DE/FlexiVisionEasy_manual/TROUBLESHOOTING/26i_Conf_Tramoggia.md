(troubleshooting_conf_tramoggia)=
# **Hopper-Konfiguration** 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen

* - **Kontrollbereich nicht definierbar**
  - • Bild nicht aufgenommen
    
    • Falscher Abschnitt
  - • Testbild aufnehmen
    
    • Über Config Hopper X zugreifen


* - **AUTO berechnet Mean und Std Dev nicht korrekt**
  - • CAPTURE nicht ausgeführt
    
    • CAPTURE-Reihenfolge vertauscht
    
    • Kontrollbereich zu klein
  - • Zuerst leeren CAPTURE, dann vollen CAPTURE ausführen
    
    • In der korrekten Reihenfolge wiederholen
    
    • Kontrollbereich vergrößern
* - **TEST immer GRÜN (Hopper wird nie aktiviert)**
  - • Schwelle zu permissiv
    
    • Voller CAPTURE mit zu vielen Komponenten
    
    • Mean falsch berechnet
  - • Vollen CAPTURE mit korrekter Mindestanzahl wiederholen
    
    • Prüfen, ob AUTO korrekt neu berechnet
    
    • Schwelle bei Bedarf manuell anpassen
* - **TEST immer ROT (Hopper wird immer aktiviert)**
  - • Schwelle zu restriktiv
    
    • Leerer CAPTURE mit vorhandenen Komponenten
    
  - • Leeren CAPTURE mit vollständig sauberem Bereich wiederholen
    
    • AUTO wiederholen

* - **Vibrationszeit erzeugt nicht die gewünschte Wirkung**
  - • Wert zu niedrig
    
    • Wert zu hoch 
    
    • Variabler Füllstand der Hopper-Schale
  - • Mit 500ms beginnen
    
    • In Schritten von ±100ms erhöhen, um den Fluss einzustellen
    
    • **KRITISCH**: Konstante Beladung in der Schale beibehalten

* - **Hopper entlädt zu falschen Zeitpunkten**
  - • Steps nicht korrekt

    • Hardware des Hopper Controllers nicht korrekt konfiguriert 

  - • Steps neu berechnen

    • Die Konfigurationsspezifikationen im [dedizierten Hopper-Handbuch]() prüfen 
```

