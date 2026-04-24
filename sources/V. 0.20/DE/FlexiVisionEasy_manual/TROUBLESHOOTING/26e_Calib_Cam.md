(troubleshooting_calib_cam)=
# **Kamerakalibrierung**

## **Pattern nicht erkannt**

```{warning}
**Fehler: "Unable to detect calibration pattern"**

Ursache: Die Software kann das Muster des Gitters nicht identifizieren.

**Lösungen**:
- Kontrast erhöhen (Belichtung oder Beleuchtung anpassen)
- Prüfen, ob das gesamte Gitter im Bild sichtbar ist
- Fokussierung verbessern
- Oberfläche des Gitters reinigen (Staub oder Fingerabdrücke können stören)
- Prüfen, ob es sich um das korrekte Gitter handelt (Quadrate, keine Kreise oder andere Pattern)
```

## **Kalibrierung immer "Bad" oder "Acceptable"**

```{warning}
**Unzureichende Kalibrierqualität**

Wenn die Kalibrierung trotz Anpassungen unter "Excellent" bleibt:

1. Den Arbeitsabstand Kamera-FlexiBowl prüfen (muss dem berechneten Wert entsprechen)
2. Prüfen, ob die Kamera parallel zur Ebene des FlexiBowl ist (muss vollkommen horizontal sein)
3. Sicherstellen, dass die Kamera stabil ist (keine Vibrationen während der Aufnahme)
4. Prüfen, ob das Objektiv vollständig eingeschraubt ist 

Wenn das Problem weiterhin besteht, kann ein mechanisches Problem bei der Montage vorliegen. Siehe [Mechanische Installation]009_Installazione_Meccanica.md) zur Überprüfung.
```

## **Fehler nach Beleuchtungswechsel**

```{tip}
**Rekalibrierung nach Wechsel backlight/toplight**

Wenn von backlight auf toplight gewechselt wird (oder umgekehrt):

1. Die geometrische Kalibrierung bleibt gültig (sie muss nicht wiederholt werden)
2. Es ist nur erforderlich, die Kamerabelichtung für den neuen Beleuchtungstyp anzupassen
3. Ein Testbild aufnehmen, um zu prüfen, dass das Pattern weiterhin gut sichtbar ist

Im Allgemeinen ist es empfehlenswert, den zu verwendenden Beleuchtungstyp von Anfang an festzulegen und diese Konfiguration beizubehalten.
```
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Kalibrierung schlägt fehl (Softwarefehler)**
  - • Kalibriergitter nicht korrekt erkannt
    
    • Beleuchtung unzureichend/übermäßig
    
    • Kalibriergitter beschädigt oder verschmutzt
    
  - • Target eben und gut sichtbar positionieren
    
    • Kamerabelichtung einstellen, um das Target gut sichtbar zu machen
    
    • Sauberes und intaktes Kalibriergitter verwenden
    
* - **Kalibrierfehler zu hoch**
  - • Kamera nicht perfekt orthogonal zur Oberfläche
    
    • Kalibriergitter nicht eben
    
    • Übermäßige optische Verzerrung
    
  - • Orthogonalität der Kamera mit Wasserwaage prüfen (Toleranz ±1°)
    
    • Target auf einer steifen und ebenen Oberfläche positionieren
    
    • Optische Qualität des Objektivs prüfen, reinigen oder ersetzen
    
* - **Reale Koordinaten stimmen nicht mit den gemessenen überein**
  - • Falscher Skalierungsfaktor (falsche Tile Size)
    
    • Kamera nach der Kalibrierung verschoben
    
  - • Vollständige Kalibrierung wiederholen
    
    • Kamera fest fixieren, um Verschiebungen zu vermeiden
    
    • Abmessungen des Kalibriertargets gemäß Dokumentation prüfen
* - **Kalibrierung nur in Bildmitte gültig**
  - • Periphere optische Verzerrung
    
    • Kalibrierung mit zu wenigen Punkten
  - • Hochwertigeres Objektiv mit geringer Verzerrung verwenden
    
    • Prüfen, ob der Arbeitsabstand korrekt ist
```



