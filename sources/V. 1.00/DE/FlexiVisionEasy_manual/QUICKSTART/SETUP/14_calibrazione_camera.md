(calibrazione)=
# **Kalibrierung von Kamera und Roboter**

Die Kalibrierung ist der entscheidende Schritt, der die exakte geometrische Beziehung zwischen der realen Welt (Koordinaten in Millimetern) und dem von der Kamera aufgenommenen Bild (Pixel) herstellt. Ohne eine genaue Kalibrierung ist die Genauigkeit des Picking-Systems beeinträchtigt, was die gesamte Anwendung unzuverlässig macht.


:::{tip}
Eine erneute Kalibrierung ist nicht erforderlich, wenn die Position des FlexiBowl® verändert wird.
:::
---

## Warum ist eine Kalibrierung notwendig?

Die Kalibrierung ist notwendig, weil jede Kombination von Sensor und Objektiv spezifische Veränderungen im Bild hervorruft. Ihr Hauptziel ist es, diese Verzerrungen zu korrigieren.

### *Arten von optischen Verzerrungen*

```{figure} ../../../../../_shared/media/images/distorsioni_new.png
:alt: Arten optischer Verzerrungen
:width: 80%
:align: center

Beispiele für optische Verzerrungen: keine Verzerrung (links), tonnenförmige Verzerrung (Mitte), kissenförmige Verzerrung (rechts)
```

---


## Schritt 1: Das Kalibrierungsgitter

:::{error}
Stellen Sie sicher, dass Folgendes gegeben ist: 
- Backlight eingeschaltet (SETUP > FlexiBowl®-Setup > Config FlexiBowl® > Light ON aktiv)
- Toplight aus
:::

:::{video} ../../../../../_shared/media/videos/Step1_calib.mp4
    :width: 100%
    :align: center
:::

Das spezielle ARS-Kalibrierungsgitter muss auf dem FlexiBowl® gelegt werden:

````{list-table}
:widths: 10 50 40
:header-rows: 1

* - Step
  - Vorgang
  - Bild
* - **0**
  - Falls vorhanden, entfernen Sie die am FlexiBowl® montierten Ablenkplatten.
  - ```{image} ../../../../../_shared/media/images/rimuoveredeviatori.jpg
      
    ```
* - **1**
  - **Lösen Sie die vier Schrauben** des mittleren Flansches des FlexiBowl®.
  - ```{image} ../../../../../_shared/media/images/rimuovereflangia.jpg
      
    ```
* - **2**
  - **Drehen Sie den mittleren Flansch** leicht gegen den Uhrzeigersinn und **nehmen Sie ihn ab**.
  - 
* - **3**
  - Vorsichtig **anheben** und **die Oberfläche entfernen**.
  - ```{image} ../../../../../_shared/media/images/rimuoveredisco.jpg
      
    ```
* - **4**
  - Bringen Sie bei Bedarf magnetische Abstandshalter an den vier Seiten des Gitters an.
  - ```{image} ../../../../../_shared/media/images/aggiungerespacer.jpg
      
    ```
* - **5**
  - Positionieren Sie **das ARS-Gitter** auf dem FlexiBowl® und richten Sie dabei die Positionierungsstifte an den vorgegebenen Löchern am Rand des Backlights aus.
  - ```{image} ../../../../../_shared/media/images/posizionaregriglia.jpg
      
    ```
````

```{figure} ../../../../../_shared/media/images/griglia_su_flexibowl.png
:alt: Positionierung Kalibrierungsgitter
:width: 60%
:align: center

Korrekte Positionierung des ARS-Kalibrierungsgitters auf der FlexiBowl®
```
:::{attention} 
 Das Kalibrierungsgitter muss auf **derselben Höhe wie das in der Anwendung verwendete Objekt** positioniert werden.
 
   Aus diesem Grund wird es mit **Abstandshaltern** geliefert, die vor der Installation auf dem FlexiBowl® in die Stifte des Gitters eingesetzt werden müssen.
   Die Abstandshalter dienen dazu, das **Gitter** auf die Höhe des Teils **anzuheben** und so eine genaue Kalibrierung zu gewährleisten.
  ![Abstandshalter](../../../../../_shared/media/images/distanziali_griglia.JPG)
  
  ```{figure} ../../../../../_shared/media/images/altezzacalibrazione.png
    :width: 100%
    :align: center
  ```
:::

## Schritt 2: Grundlegende Einstellungen

```{list-table}

* - **5**
  - Rufen Sie den Abschnitt Camera SETUP im Menü SETUP auf 
* - **6**
  - Klicken Sie auf die Schaltfläche Config Camera der entsprechenden Kamera 
* - **7**
  - Klicken Sie auf der Seite Camera FLB auf EXPERT 
* - **8**
  - **Versetzen Sie die Kamera in den Modus „Live Display“**
      Aktivieren Sie vor dem Einstellen der Blende den kontinuierlichen Anzeigemodus:
      :::{figure} ../../../../../_shared/media/images/livedisplay.jpg
    :width: 100%
    :align: center
    :::
* - **9**
  - **Stellen Sie die Blendenöffnung ein**
    - Lösen Sie die Schraube am oberen Kameraring leicht
    - Drehen Sie den Ring, während Sie das Live-Bild beobachten, bis die richtige Lichtmenge in die Kamera eintritt
    - Ziehen Sie die Schraube am oberen Kameraring fest

    :::{figure} ../../../../../_shared/media/images/Esp_Corretta.png
    :width: 100%
    :align: center
    :::
* - **10**
  - **Stellen Sie den Fokus der Kamera manuell ein**
    - Lösen Sie die Schraube am unteren Ring der Kamera leicht
    - Drehen Sie den Ring langsam, während Sie das Live-Bild beobachten
    - Wenn das Muster scharf erscheint, ist der Fokus korrekt
    - Ziehen Sie die Schraube am unteren Ring der Kamera fest
    - Schließen Sie den Bildschirm
    :::{figure} ../../../../../_shared/media/images/Fuoco_Corretto.png
    :width: 100%
    :align: center
    :::
* - **11**
  - Klicken Sie auf Zurück 
```

```{warning}
**Achtung zur Schärfentiefe**

Die Fokussierung muss eine Schärfe über die **gesamte Oberfläche** des FlexiBowl® gewährleisten, nicht nur in der Mitte.

Wenn die Mitte scharf, die Ränder jedoch unscharf sind:
- Überprüfen Sie, ob die Optik sauber ist
- Überprüfen Sie, ob der Arbeitsabstand korrekt ist
- Überprüfen Sie, ob die Kamera perfekt parallel zur Arbeitsfläche des FlexiBowl® ausgerichtet ist
- Schließen Sie die Blende leicht, um die Schärfentiefe zu erhöhen

Wenn das Problem weiterhin besteht, muss möglicherweise die mechanische Montage der Kamera überprüft werden.
```
:::{video} ../../../../../_shared/media/videos/Step2b_calib.mp4
    :width: 100%
    :align: center
:::

:::{error}
Wenn beim mehrfachen Drücken der RUN-Taste auch nur einmal ein vollständig blauer Bildschirm erscheint, siehe [Troubleshooting Kamera-Setup](schermo_blu)
:::


```{list-table}
* - **12** 
  - **Stellen Sie die Belichtung der Kamera ein**
    - Rufen Sie auf der Seite **Camera FLB x** den Parameter **Cam Exposure** (Kamerabelichtung) auf:
    - Stellen Sie den Parameter „Cam Exposure“ ein und klicken Sie auf <img src="../../../../../_shared/media/images/tasto_TEST.png" class="inline-icon">. Wiederholen Sie diesen Schritt, bis die richtige Belichtung für das Bild gefunden ist: 
   		- Gittermuster deutlich sichtbar (schwarz auf weiß oder umgekehrt)
   		- Hoher Kontrast zwischen weißen und schwarzen Quadraten
   		- Keine Überbelichtung (vollständig weiße „ausgebrannte“ Bereiche)
   		- Keine Unterbelichtung (Bild zu dunkel)
* - **13** 
  - Klicken Sie auf NEXT
```

```{figure} ../../../../../_shared/media/images/Esposizioni.png
:alt: Beispiel korrekte Belichtung
:width: 60%
:align: center

Beispiel für eine korrekte Belichtung: hoher Kontrast, gut definiertes Muster, keine überbelichteten Bereiche
```

```{tip}
**Optimierung der Belichtung**

**Je länger die Belichtungszeit, desto mehr Licht fällt in das Objektiv**

- **Zu kurze Belichtungszeit**: Dunkles Bild, Muster kaum sichtbar
- **Zu lange Belichtungszeit**: Überbelichtetes Bild, Verlust von Details
- **Optimale Belichtungszeit**: Maximaler Kontrast ohne Übersättigung
```
:::{tip}
Wenn Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO**-Taste auf der aktuellen Seite.
:::


## Schritt 3: Kamerakalibrierung

:::{video} ../../../../../_shared/media/videos/Step3_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
:widths: 5 95

* - **14**
  - Vergewissern Sie sich, dass das Gitter zentriert, scharf und vollständig sichtbar ist, bevor Sie das Kalibrierungsbild aufnehmen.
* - **15**
  - Klicken Sie auf „Grab Image“, um ein Foto des Kalibrierungsgitters aufzunehmen.
    
    Überprüfen Sie Folgendes visuell:
    - Das gesamte Gitter ist sichtbar
    - Das Muster ist scharf
    - Es gibt keine Schatten oder Reflexionen

* - **16**
  - Stellen Sie die Werte „Tile Size X“ und „Tile Size Y“ für alle Modelle von FlexiBowl® 500 bis 1200 auf 10 ein.  
     **Bei den Modellen FlexiBowl® 200 und FlexiBowl® 350 hingegen stellen Sie die Tile Sizes auf 2,5 ein.**

* - **17**
  - Klicken Sie auf „Calibrate“, um die Kalibrierung durchzuführen

* - **18**
  - **Bewertung der Kalibrierungsqualität**
    
    Der Parameter „Result Calibration“ gibt einen Wert zurück:
    
    🟢 **Excellent (Grün)**: Hervorragende Kalibrierung, optimale Genauigkeit. 
    
    🟠 **Acceptable (Orange)**: Akzeptable Kalibrierung, gute, aber nicht optimale Genauigkeit.
    
    🔴 **Bad (Rot)**: Schlechte Kalibrierung, unzureichende Genauigkeit. Muss unbedingt wiederholt werden.
    
    :::{important}
    Akzeptieren Sie nur ausgezeichnete Kalibrierungen 🟢; andere Ergebnisse beeinträchtigen den Betrieb der gesamten Anwendung.
    :::

```

```{note}
**Akzeptanzkriterium**

Ein zufriedenstellendes Ergebnis umfasst die Einstellung der Blende, die Fokussierung und die für die Anwendung optimale Belichtungseinstellung.

```

```{warning}
**Fehler während der Berechnung**

Wenn die Kalibrierungsberechnung fehlschlägt:

**Mögliche Ursachen**:
- Muster nicht erkannt (Bild zu dunkel oder überbelichtet)
- Rasterquadrate teilweise verdeckt
- Übermäßige Verzerrung (Kamera zu nah oder zu weit weg)
- Falsche Tile Size eingegeben

**Lösung**:
- Prüfen und verbessern Sie die Qualität des aufgenommenen Bildes
- Stellen Sie sicher, dass das gesamte Raster sichtbar und gut ausgeleuchtet ist
- Prüfen Sie den Wert für die Tile Size
- Wiederholen Sie die Bildaufnahme (Grab Image) und versuchen Sie es erneut
```

:::{tip}
Wenn Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO**-Taste auf der aktuellen Seite.
:::



---

### *Wann muss die Kalibrierung wiederholt werden*
```{list-table}
:widths: 50 50
:header-rows: 0

* - **Kalibrieren Sie in folgenden Fällen neu:**
  - Bei der ersten Einrichtung des Systems (obligatorisch). Nach einer Änderung der Kameraposition. Nach einer Verschiebung des Roboters. Wenn systematische Fehler beim Greifen auftreten.

* - **Eine Neukalibrierung ist in folgenden Fällen nicht erforderlich:**
  - Bei einem Wechsel des Teiltyps unter Beibehaltung des FlexiBowl® und der Kamera. Bei einer Änderung des Fokus oder der Blende des Objektivs. Wenn das Software-Rezept geändert wird. Wenn Erkennungsparameter angepasst werden. Wenn die Roboterprogramme aktualisiert werden.
```

---
# **Roboter-Kalibrierung**

## Schritt 4: Laser-Montage

:::{video} ../../../../../_shared/media/videos/Step4_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **19** 
  - Sobald eine Kalibrierung von ausgezeichneter Qualität erreicht wurde, klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon icon-small">.  
  
    Es erscheint ein Fenster, das eine Roboter-Kalibrierung vor dem Fortfahren anfordert. Klicken Sie **NICHT** auf „Ja“ und folgen Sie den nächsten Schritten
* - **20** 
  - Montieren Sie das Laser Tool mit seinem individuellen Halter 
    :::{important}
    Die Halterung zum Anbringen des Laser-Tools anstelle des Robotergreifers wird **NICHT** mitgeliefert, da sie für jeden Roboter variiert und angepasst werden muss.
    :::
    :::{figure} ../../../../../_shared/media/images/step1calrobot.jpg
    :width: 30%
    :align: center
    :::
* - **21**
  - Positionieren Sie den Spacer Bracket (**A**) unter dem Laser 
    :::{figure} ../../../../../_shared/media/images/step2calrobot.jpg
    :width: 30%
    :align: center
    :::
* - **22**
  - Senken Sie den Laser auf die Höhe des Spacers (**A**) ab, sodass der Laser genau 3 cm über dem Kalibrierungsgitter liegt
    :::{image} ../../../../../_shared/media/images/spacerbracket.png
    :align: center 
    :width: 75%
    :::
* - **23**
  - Entfernen Sie den Spacer Bracket 
    :::{figure} ../../../../../_shared/media/images/step3calrobot.jpg
    :width: 30%
    :align: center
    :::
* - **24**
  - Schalten Sie den Laser ein 
    :::{figure} ../../../../../_shared/media/images/step4calrobot.jpg
    :width: 30%
    :align: center
    :::
```

:::{tip}
Wenn Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO**-Taste auf der aktuellen Seite.
:::


## Schritt 5: Zeichnen einer 3-Punkt-Ebene

:::{video} ../../../../../_shared/media/videos/Step5_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **25**
  - Führen Sie den Laser zum Ursprungspunkt 
  - :::{figure} ../../../../../_shared/media/images/origine.jpg
    :width: 100%
    :align: center
    :::
* - **26**
  - Führen Sie den Laser zum Endpunkt der X-Achse
  - :::{figure} ../../../../../_shared/media/images/assex.jpg
    :width: 100%
    :align: center
    :::
* - **27**
  - Führen Sie den Laser zum Endpunkt der Y-Achse 
  - :::{figure} ../../../../../_shared/media/images/assey.jpg
    :width: 100%
    :align: center
    :::
```

:::{tip}
Wenn Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO**-Taste auf der aktuellen Seite.
:::


## Schritt 6: Überprüfung der Roboterbahn

:::{video} ../../../../../_shared/media/videos/Step6_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **28** 
  - Führen Sie den Laser zurück zum Ursprungspunkt
* - **29**
  - Bewegen Sie den Roboter über seine Teach Pendant entlang der X- und Y-Achsen. 
* - **30**
  - Überprüfen Sie, ob die korrekte Trajektorie eingehalten wird: Der Roboter muss sich ausschließlich entlang der X- und Y-Achsen bewegen und dabei korrekt den Linien des Gitters folgen 
* - **31**
  - Klicken Sie auf „YES“
    :::{figure} ../../../../../_shared/media/images/clickyes.jpg
    :width: 50%
    :align: center
    :::
```
:::{tip}
Wenn Sie während der Konfiguration Zweifel haben, konsultieren Sie bitte die **INFO**-Taste auf der aktuellen Seite.
:::


## Schritt 7: Speichern des Basisrezepts
```{list-table}
:header-rows: 0
:widths: 10 90

* - **32**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">

* - **33**
  - Vergewissern Sie sich, dass Sie das Rezept mit allen Einstellungen und der Kalibrierung im Menü links ausgewählt haben, und klicken Sie auf <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon">

* - **34**
  - Dadurch werden alle bisher durchgeführten Schritte separat gespeichert, sodass Sie eine Grundlage für alle zukünftigen Rezepte haben, die die verschiedenen Modelle für das kalibrierte System enthalten

* - **35**
  - Um mit der Erstellung der Modelle fortzufahren, duplizieren Sie das Basisrezept, benennen Sie es nach Belieben um und klicken Sie auf <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">: Es wird eine Seite mit der Liste aller verfügbaren Modelle geöffnet
```
---

# **Häufige Probleme bei der Kalibrierung**

## Muster nicht erkannt

```{warning}
**Fehler: „Unable to detect calibration pattern“**

Ursache: Die Software kann das Gittermuster nicht erkennen.

**Lösungen**:
- Erhöhen Sie den Kontrast (passen Sie die Belichtung oder Beleuchtung an)
- Stellen Sie sicher, dass das gesamte Gitter im Bild sichtbar ist
- Verbessern Sie die Schärfe
- Reinigen Sie die Oberfläche des Gitters (Staub oder Fingerabdrücke können stören)
```

## Kalibrierung immer „Bad“ oder „Acceptable“

```{warning}
**Unzureichende Kalibrierungsqualität**

Wenn die Kalibrierung trotz Anpassungen unter „Excellent“ bleibt:

1. Überprüfen Sie den Arbeitsabstand zwischen Kamera und FlexiBowl® (er muss dem berechneten Wert entsprechen)
2. Stellen Sie sicher, dass die Kamera parallel zur Ebene des FlexiBowl® ausgerichtet ist (sie muss perfekt horizontal sein)
3. Stellen Sie sicher, dass die Kamera stabil ist (keine Vibrationen während der Aufnahme)
4. Überprüfen Sie, ob das Objektiv vollständig festgeschraubt ist 

Wenn das Problem weiterhin besteht, liegt möglicherweise ein mechanisches Problem bei der Montage vor. Siehe [Mechanische Installation](../../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md) zur Überprüfung.
```
---

## Nächste Schritte

Sobald die Kalibrierung der Kamera und des Roboters abgeschlossen ist, fahren Sie mit fort:

- [FlexiBowl®-Setup](fbsetup)
- [Trichter-Setup](13b_Hopper_Setup.md)
- [Roboter-Setup](13c_Robot_Setup.md)
- [Protocol Setup](protocol_setup)
- [Rezept speichern](ricettabase)








