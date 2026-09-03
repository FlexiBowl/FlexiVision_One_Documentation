(nuovomodello)=
# **Ein Neues Modell erstellen**

Auf dieser Seite erfahren Sie, wie Sie ein Referenzmodell für die Erkennung von Teilen erstellen.


## Schritt 1: Vorbereiten der physischen Einrichtung
Falls noch nicht geschehen, führen Sie die folgenden Schritte aus:
````{list-table}
* - **1**
  - Demontieren Sie das Kalibriergitter und stellen Sie das ursprüngliche Layout wieder her:
    - Positionieren Sie die Oberfläche neu
    - Positionieren Sie den mittleren Flansch neu
    - Befestigen Sie den mittleren Flansch mit seinen vier Schrauben
* - **2**
  - Platzieren Sie ein Objekt in der Mitte des Sichtfelds
````
---

## Schritt 2: Zugriff auf das Modell

Nach Abschluss der physischen Vorbereitung fahren Sie mit der Bildaufnahme und der Erstellung des Modells fort
````{list-table}
* - **3**
  - Klicken Sie nach Auswahl des richtigen Rezepts auf der Seite „Recipes“ auf <img src="../../../../../_shared/media/images/tasto_edit_recipes.png" class="inline-icon">
* - **4**
  - Wählen Sie den FlexiBowl® aus, mit dem Sie arbeiten
    :::{dropdown} **Auswahl des FlexiBowl®**
    ![FB-Auswahl](../../../../../_shared/media/images/scelta_FB.png)
    :::
* - **5**
  - Die verfügbaren Modellplätze werden angezeigt (bis zu 8 Modelle pro Rezept)
* - **6**
  - Klicken Sie auf **Modell 1** , um die Seite „Train Model 1 Cam 1“ aufzurufen
````

### *Übersicht über die Benutzeroberfläche „Train Model“*

![Seite „Train Model“](../../../../../_shared/media/images/pagina_trainmodel.png)
````{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Funktion
* - **Enable Model**
  - Aktiviert diesen Modell-Slot, um ihn nutzbar zu machen
* - **Grab Train Image**
  - Nimmt ein Foto der Referenzkomponente für das Training auf
* - **Score Threshold**
  - Passt den Detaillierungsgrad des Modells an (von 0 = maximale Detailgenauigkeit bis 1 = minimale Detailgenauigkeit)
* - **Train**
  - Erzeugt das Modell durch Verarbeitung des aufgenommenen Bildes
* - **Model Name**
  - Textfeld, um dem Modell einen beschreibenden Namen zu geben
````
````{tip}
**Verwaltung mehrerer Modelle**

In dieser Phase wird nur das erste Modell aktiviert. Nach dessen Fertigstellung wird dies möglich sein:
- Aktivieren zusätzlicher Slots (Modell 2, Modell 3 usw.) für verschiedene Teile im selben Rezept
- Bearbeiten bestehender Modelle
- Deaktivieren nicht mehr benötigter Modelle

Konzentrieren Sie sich zunächst auf die Fertigstellung des ersten Modells.
````
---

## Schritt 3: Trainingsverfahren
````{video} ../../../../../_shared/media/videos/TastoInfo_TrainModel_1280x720.mp4
:width: 100%
:align: center 
````
````{list-table}
:widths: 5 95

* - **7**
  - Klicken Sie auf „**Enable Model**“, um dieses Modell zu aktivieren. Das Modell ist nun aktiv und bereit für die Konfiguration.

* - **8**
  - Klicken Sie auf **"Grab Train Image"** , um ein Foto des Referenzteils aufzunehmen, das wir auf dem FlexiBowl® positioniert haben
    
    :::{warning}
    Das Referenzteil muss während des gesamten Prozesses der Anwendungserstellung an dieser Stelle stillstehen.
    :::

* - **9**
  - Verschieben Sie die **ROI-Rahmen**, um das Teil vollständig einzurahmen

* - **10**
  - Verschieben Sie den **Ursprung** (Referenzpunkt) in die Mitte des Rahmenbereichs
    
    :::{tip}
    **Wo soll der Ursprung positioniert werden?**
    
    Der Ursprung wird automatisch in der Mitte des Bauteils positioniert.  
    Wenn der Greifpunkt nicht mit dem geometrischen Mittelpunkt übereinstimmt, verschieben Sie den Ursprung zum:
    - **Greifpunkt**: Bei asymmetrischen Teilen dort positionieren, wo die Greifzange greift
    
    *Der Ursprung definiert den Punkt (0,0) des Koordinatensystems des Modells.*
    :::

* - **11**
  - Verwenden Sie **Score Threshold**, um den gewünschten Detaillierungsgrad einzustellen
    
    ::::{note}
    **Score Threshold**
     
      ![Modellvergleich Score Threshold](../../../../../_shared/media/images/confrontomodello.png)
    
    **Wert nahe 0** → Erkennt MEHR Details (präziseres Modell)
    
    **Wert nahe 1** → Erkennt WENIGER Details (einfacheres Modell)
    ::::
    
    :::{tip}
    **Wie wählt man den optimalen Score Threshold?**
    
    **Niedrigen Wert (0.1–0.3) verwenden, wenn:**
    - Das Teil viele charakteristische Details aufweist (Gravuren, Logos, Texturen)
    - Die Teile immer sehr ähnlich sind (enge Toleranzen)
    - Maximale Präzision auch bei schwierigen Orientierungen gewünscht ist
    
    **Hohen Wert (0.4–0.6) verwenden, wenn:**
    - Das Teil eine charakteristische, aber einfache Form hat
    - Ein Gleichgewicht zwischen Präzision und Toleranz gewünscht ist
    - Es sich um die erste Konfiguration eines Modells handelt (Ausgangspunkt)
    
    **Sehr hohen Wert (0.7–0.9) verwenden, wenn:**
    - Es signifikante Variationen zwischen den Teilen gibt (weite Toleranzen)
    - Die Oberfläche des Teils sehr reflektierend oder variabel ist
    :::

* - **12**
  - Klicken Sie auf **Train**
````
:::{tip}
Bei Fragen während der Konfiguration klicken Sie bitte auf die Schaltfläche „**INFO**“ auf der aktuellen Seite.
:::
---

## Schritt 4: Visuelle Überprüfung

Nachdem das Modell erstellt wurde, ist es wichtig, vor dem Fortfahren seine Qualität zu überprüfen.
````{list-table}

* - **13**
  - **Zoomen** Sie das Bild, um die Details des erstellten Modells zu begutachten und sicherzustellen, dass das Modell korrekt ist
    
    :::{tip}
      **Merkmale eines gültigen Modells**  
      ✓ Genügend Linien zur Erkennung des Bauteils  
      ✓ Keine Textur der Hintergrundfläche einschließen  
      ✓ Lichtreflexionen vermeiden  
    :::

    ![Modellvergleich](../../../../../_shared/media/images/confrontomodello2.png)
````
````{attention}
Wenn das Modell nicht zufriedenstellend ist:
- Ändern Sie den **Score Threshold**
- Klicken Sie erneut auf **Train**
- Wiederholen Sie den Vorgang, bis Sie ein optimales Modell erhalten haben
````
````{tip}
**Optimierungsstrategie**

**Problem: Das Modell enthält eine Oberflächentextur**  
→ Lösung: Erhöhen Sie den Score Threshold oder den Wert „Cam Exposure“ (SETUP > Kamera-Setup > Cam Exposure)

**Problem: Das Modell hat zu wenige Linien, ist nicht unterscheidbar**  
→ Lösung: Verringern Sie den Score Threshold 

**Problem: Das Modell enthält Reflexionen**  
→ Lösung: Score Threshold erhöhen oder Kameraexposition anpassen

Nehmen Sie schrittweise Änderungen vor (in Schritten von 0,1-0,2) und testen Sie jedes Mal.
````
---

## Schritt 5: Speicherung
````{list-table}
* - **14**
  - Benennen Sie das Modell mit einem beschreibenden Namen  
    :::{tip}
    **Vermeiden Sie allgemeine Namen**

    ❌ Zu vermeidende Namen:
    - `Test`, `Prova`, `Modello1`, `Nuovo_Modello`

    ✓ Empfohlene Namen:
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    Ein eindeutiger Name erleichtert die Verwaltung, wenn Sie viele verschiedene Modelle haben.
    :::
* - **15**
  - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_next.png" class="inline-icon"> → die Seite **Define Robot Pick Area** wird geöffnet  
````
````{seealso}
Fahren Sie mit [ROI-Definition](roitest) fort, um die Konfiguration fortzusetzen.
````

