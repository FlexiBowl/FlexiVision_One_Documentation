# **Erstellen von Rezepten und Vorlagen**

(troubleshooting_nuova_ricetta)=
## Fehlerbehebung für den Abschnitt Neues Rezept erstellen

```{warning}
**Fehler beim Speichern**

Wenn das Speichern des Rezepts fehlschlägt:
- Überprüfen Sie, ob genügend Speicherplatz auf der Festplatte vorhanden ist  
- Vergewissern Sie sich, dass der Name keine unzulässigen Zeichen enthält N`/ \ : * ? " < > |`)  
- Überprüfen Sie, ob bereits ein Rezept mit demselben Namen existiert  
- Überprüfen Sie, ob Sie Schreibrechte für den Software-Ordner haben  
```

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Neues Rezept kann nicht erstellt werden**
  - • Festplatte voll  
     
    • Rezeptname enthält unzulässige Zeichen  
  - • Speicherplatz auf der Festplatte freigeben  
    
    • Sonderzeichen im Namen vermeiden N`/ \ : * ? " < > |)  

* - **Rezept gespeichert, aber Einstellungen verloren**  
  - • Speichern nicht korrekt bestätigt  
    
    • Software wurde zwangsweise beendet  
    
    • Schreibfehler auf der Festplatte  
  - • Immer auf „Save Recipe“ klicken und auf Bestätigung warten  
    
    • Software ordnungsgemäß schließen  
    
    • Windows-Fehlerprotokoll überprüfen  
* - **Erstelltes Rezept kann nicht geladen werden**
  - • Rezeptdatei beschädigt  
    
    • Dateipfad geändert  
  - • Aus Backup wiederherstellen, falls verfügbar  
    
    • Pfad zum Rezeptordner in der Konfiguration überprüfen  
* - **Geladenes Rezept weist fehlerhafte Einstellungen auf**
  - • Falsches Rezept ausgewählt  
    
    • Änderungen zuvor nicht gespeichert  
    
    • Konflikt zwischen Rezepten mit ähnlichen Namen  
  - • Rezeptnamen in der oberen Leiste überprüfen  
    
    • Richtiges Rezept aus der Liste neu laden  
    
    • Eindeutige Namenskonventionen verwenden  
```

(troubleshooting_nuovo_modello)=
## Fehlerbehebung für den Abschnitt „Ein neues Modell erstellen“

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen

* - **Grab Train Image nimmt ein schwarzes Bild auf**
  - • Kamera nicht angeschlossen  
    
    • Toplight ausgeschaltet  

    • Hintergrundbeleuchtung ausgeschaltet  
    
    • Belichtung zu niedrig  
    
    • Objektiv mit Schutzkappe  
  - • Kameraverbindung in „Kamera-Setup“ überprüfen
    
    • Toplight einschalten und Stromversorgung überprüfen
  
    • Überprüfen, ob „Light on“ in der FlexiBowl®-Konfiguration angekreuzt ist  
     
    • Belichtung der Kamera erhöhen     
    
    • Objektivabdeckung entfernen  
* - **ROI verschiebt sich nicht oder lässt sich nicht in der Größe anpassen**
  - • Bild wurde nicht aufgenommen  
    
    • Software blockiert  
  - • Zuerst „Grab Train Image“ ausführen  
    
    • Software neu starten  

* - **Apply Train erzeugt kein Modell**
  - • ROI zu klein  
    
    • Bild ohne ausreichenden Kontrast  
  
  - • ROI vergrößern, um die gesamte Komponente einzubeziehen  
    
    • Kontrast/Beleuchtung verbessern  

* - **Erstelltes Modell enthält Oberflächenstruktur**
  - • Feature-Threshold zu niedrig  
    
    • Unzureichender Kontrast zwischen Komponente und Oberfläche  
  - • Feature Threshold Nes erhöhen: von 0.3 auf 0.6)  
    
    • Beleuchtung verbessern, um den Kontrast zu erhöhen  
* - **Das erstellte Modell hat zu wenige Linien**
  - • Feature Threshold zu hoch  
    
    • Unscharfes Bild  

    • Bild ohne ausreichenden Kontrast  
  - • Feature Threshold Nes verringern: von 0.8 auf 0.5)  
    
    • Kamerafokus überprüfen und gegebenenfalls korrigieren  

     • Kontrast/Beleuchtung verbessern  

* - **Modell enthält Lichtreflexe**
  - • Feature Threshold zu niedrig  
    
    • Beleuchtung ungleichmäßig  
    
  - • Feature Threshold erhöhen  
    
    • Position/Winkel des Toplights anpassen  
 

* - **Modell kann nicht benannt werden**
  - • Name enthält unzulässige Zeichen  
    
    • Name zu lang  
  - • Verwenden Sie nur Buchstaben, Zahlen, Unterstriche und Bindestriche  
    
    • Begrenzen Sie den Namen auf maximal 50 Zeichen  
```

(troubleshooting_modelli_roi)=
## Fehlerbehebung für den Abschnitt „ROI-Definition und Toleranzen“

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen

* - **Test erkennt keine Komponenten**
  - • Accept Threshold zu hoch  
    
    • Komponenten außerhalb der Region Search  
    
    • Falsches Modell  
    
    • Beleuchtung im Vergleich zum Training verändert  
  - • Accept Threshold Nes verringern: von 0.90 auf 0.75)  
    
    • Suchbereich erweitern, um Komponenten einzubeziehen  
    
    • Modelltraining wiederholen  
    
    • Beleuchtung stabilisieren  
* - **Test erkennt zu viele Fehlalarme**
  - • Accept Threshold zu niedrig  
    
    • Modell zu einfach/allgemein  
    
    • Es sind sehr ähnliche Komponenten vorhanden, die sich jedoch gleichzeitig stark unterscheiden  
  - • Accept Threshold Nes erhöhen: von 0.70 auf 0.85)  
    
    • Modell mit niedrigerem Feature Threshold (detaillierter)  
    
    • Bei Bedarf in verschiedene Modelle aufteilen  
* - **Test erkennt Komponenten, aber mit zu niedrigen Werten**  
  - • Variabilität der realen Komponenten im Vergleich zum Trainingsmodell  
    
    • Unterschiedliche Beleuchtung  
    
    • Verschmutzte/beschädigte Komponenten  
    
    • Modell zu detailliert  
  - • Qualität der Komponenten überprüfen und bei Bedarf reinigen  
    
    • Beleuchtung standardisieren  
    
    • Beschädigte Komponenten aussortieren  
    
    • Modell mit höherem Feature Threshold (weniger detailliert) neu erstellen  

* - **Ergebnistafel leer, obwohl Komponenten sichtbar sind**
  - • Keine Komponenten überschreiten den Accept Threshold  
    
    • Region Search enthält keine Komponenten   
    
    • Test nicht ausgeführt  
  - • Accept Threshold verringern  
    
    • Region Search überprüfen und erweitern  
    
    • Auf die Schaltfläche Test klicken  
* - **X-, Y- und Rotationskoordinaten sind falsch**
  - • Kamerakalibrierung nicht oder fehlerhaft durchgeführt  
    
    • Referenzsystem falsch  
    
    • Kamera nach Kalibrierung verschoben  
  - • Vollständige Kamerakalibrierung durchführen oder die aktuelle überprüfen  
    
    • Ursprung des Koordinatensystems überprüfen  
    
    • Kamerakalibrierung wiederholen  
```

(troubleshooting_istogrammi)=
## Fehlerbehebung für den Abschnitt „Histogramme“

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Histogramm kann nicht aktiviert werden**
  - • Modell nicht erkannt  
    
    • Höchstgrenze der Histogramme erreicht: N8 pro Modell)  
    
    • Steckplatz bereits belegt  
  - • Zuerst Modellkonfiguration abschließen  
    
    • Nicht verwendete Histogramme deaktivieren  
    
    • Freien Steckplatz auswählen  

* - **AUTO berechnet nicht korrekt**
  - • Histogrammbereich zu klein  
    
    • Histogramm außerhalb des Bildes  
    
    • Bild nicht geladen
  - • Histogrammbereich vergrößern  
    
    • Histogramm in den sichtbaren Bereich verschieben  
    
    • Neues Bild erfassen  
* - **Test immer ROT, auch bei freiem Bereich**  
  - • AUTO-Kalibrierung mit belegtem Bereich durchgeführt  
    
    • Schatten oder Reflexion im Bereich  
    
    • FlexiBowl®-Rand im Bereich enthalten  
    
    • Verschmutzung auf der Oberfläche  
  - • AUTO mit vollständig freiem Bereich wiederholen  
    
    • Bereiche mit Schatten/Reflexionen ausschließen  
    
    • Bereich durch Ausschluss der Ränder verkleinern  
    
    • FlexiBowl®-Oberfläche reinigen  
* - **Test immer GRÜN, auch bei belegtem Bereich**  
  - • AUTO-Kalibrierung mit bereits vorhandenen Komponenten durchgeführt  
    
    • Schwellenwerte falsch berechnet  
    
    • Unzureichender Kontrast  
  - • AUTO wiederholen und sicherstellen, dass der Bereich vollständig leer ist  
    
    • Kalibrierung bei stabiler Beleuchtung wiederholen  
    
    • Kontrast/Beleuchtung verbessern  
* - **Histogramm löst zufällig aus**  
  - • Zu großer Bereich umfasst variable Zonen  
    
    • Beleuchtung instabil  
    
    • Schwellenwert zu eng   
  - • Bereich auf das notwendige Minimum reduzieren  
    
    • Beleuchtung stabilisieren  
    
    • AUTO-Kalibrierung wiederholen  
* - **Histogramm löst nicht aus, wenn es sollte**  
  - • Zu kleiner Bereich umfasst kein Hindernis  
    
    • Schwellenwert zu großzügig  
    
  - • Histogrammbereich vergrößern  
    
    • AUTO-Kalibrierung mit höherem Kontrast wiederholen  
    
* - **Zweites Histogramm für Greifer kann nicht erstellt werden**
  - • Falscher Histogramm-Slot ausgewählt  
  - • Zur Liste zurückkehren und Histogramm 2 auswählen  
* - **Test mit mehreren Histogrammen funktioniert nicht**  
  - • Nicht alle Histogramme aktiviert  
    
    • Konfiguration unvollständig  
    
    • Konflikt zwischen Histogrammen  
  - • Überprüfen, ob alle erforderlichen Histogramme aktiviert sind  
    
    • AUTO-Konfiguration für jedes Histogramm abschließen  
    
    • Sicherstellen, dass sich die Bereiche nicht überlappen  
```

(troubleshooting_robot_pick)=
## Fehlerbehebung für den Abschnitt „Kalibrierung des Pick-Roboters“

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Mögliche Ursachen
  - Lösungen
* - **Robotkoordinaten nicht verfügbar (verloren/vergessen)**
  - • Bei der physischen Vorbereitung nicht notiert  
    
    • Notizblatt verloren  
    
    • Koordinaten überschrieben  
  - • **UNBEDINGT ERFORDERLICH**: Wiederholen Sie die gesamte physische Vorbereitung von Punkt 1 bis Punkt 9 von [Creazione Modello](../QUICKSTART/Nuovo_Modello/18_NuovoModello.md)  
    
    • Koordinaten nicht nur auf Papier, sondern auch in einer digitalen Datei speichern  
    
    • Display des Roboterpendants fotografieren  
* - **Find Object erkennt Komponente nicht**
  - • Referenzkomponente verschoben  
    
    • Accept Threshold zu hoch  
    
    • Komponenten außerhalb von Region Search  
  - • Referenzposition der Komponente überprüfen  
    
    • Accept Threshold vorübergehend senken  
    
    • Überprüfen, ob Region Search die Komponente enthält  
* - **Vision Result zeigt falsche Koordinaten an**  
  - • Kamerakalibrierung nicht durchgeführt  
    
    • Koordinatensystem nicht konfiguriert  
    
    • Kamera nach Kalibrierung verschoben  
  - • Kamerakalibrierung vor dem Pick-Robot durchführen  
    
    • Ursprung des Referenzsystems überprüfen  
    
    • Kamerakalibrierung wiederholen  
* - **Robotkoordinaten können nicht eingegeben werden**  
  - • Felder gesperrt  
    
    • Enable Robot Pick nicht aktiviert  
    
    • Falsches Zahlenformat  
  - • Zuerst auf „Enable Robot Pick“ klicken  
    
    • Felder durch Anklicken aktivieren  
    
    • Punkt als Dezimaltrennzeichen verwenden  
* - **Gripper Offset berechnet unsinnige Werte**  
  - • Falsch eingegebene Roboterkoordinaten  
    
    • X und Y vertauscht  
    
    • Falsches Vorzeichen (+/-)  
    
    • Falsche oder ungenaue Dezimalstellen  
  - • **KRITISCH**: Prüfen Sie jede Koordinate sorgfältig  
    
    • Reihenfolge von X, Y, RZ kontrollieren  
    
    • Vorzeichen der Koordinaten überprüfen  
     
    • Werte genau wie notiert kopieren, ohne Rundungen  
* - **Roboter greift nach der Kalibrierung an falschen Positionen**  
  - • Notierte Roboterkordinaten waren falsch  
    
    • Roboter-Frame/Tool nach der Notiz geändert  
    
    • Referenzkomponente wurde während der Notiz verschoben  
    
    • Gripper-Offset nicht gespeichert  
  - • Physische Vorbereitung wiederholen und dabei korrekten Frame/Tool überprüfen  
    
    • Sicherstellen, dass Frame/Tool für Notiz und Entnahme identisch sind   
    
    • Setup mit korrekt positioniertem Bauteil wiederholen  
    
    • Rezept nach Berechnung des Greifer-Offsets speichern  
* - **Roboter-Offset gilt nur für Referenzteil**  
  - • Hohe optische Verzerrung  
     
    • Kamerakalibrierung ungenau  
     
    • Region Search im Vergleich zur Kalibrierung zu groß  
  - • Kamerakalibrierung verbessern  
    
    • Objektiv mit geringer Verzerrung verwenden  
    
    • Region Search nach Möglichkeit verkleinern  
* - **Gripper-Offset kann nicht gespeichert werden**  
  - • Rezept nicht geladen   
    
    • Berechtigungen unzureichend  
    
    • Festplatte voll  
  - • Überprüfen, ob das Rezept korrekt geladen wurde  
    
    • Schreibberechtigungen überprüfen  
    
    • Speicherplatz auf der Festplatte freigeben  
* - **RZ-Rotation des Roboters immer falsch**  
  - • RZ des Roboters war während des Setups nicht auf 0° eingestellt  
    
    • Letzte Roboterachse nicht korrekt  
    
    • Koordinatensystem gedreht  
  - • Setup wiederholen und letzte Roboterachse auf RZ=0° bringen  
    
    • Überprüfen, ob das ausgewählte Tool korrekt ist  
    
    • Ausrichtung des Koordinatensystems überprüfen  
```



