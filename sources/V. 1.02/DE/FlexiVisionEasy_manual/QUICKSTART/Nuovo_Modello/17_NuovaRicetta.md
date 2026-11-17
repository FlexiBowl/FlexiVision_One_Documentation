(nuovaricetta)=  
# **Ein Neues Rezept erstellen**

Dieser Abschnitt beschreibt, wie Sie in FlexiVision One ein neues Anwendungsrezept erstellen. Ein Rezept ist der Hauptcontainer, der alle Teilemodelle, FlexiBowl®-/Trichter-Konfigurationen und Roboterparameter enthält, die für eine vollständige Picking-Anwendung erforderlich sind.
```{note}
**Erstellen Sie ein neues Rezept, wenn:**

- Sie mit einem **völlig anderen Teiletyp** arbeiten
- Sie die **Anwendung** wechseln

**Es ist NICHT erforderlich, ein neues Rezept zu erstellen, wenn:**
- Sie eine Seite desselben Teils hinzufügen (erstellen Sie ein neues Modell im selben Rezept für dasselbe Teil an verschiedenen Positionen)
- Sie kleine Anpassungen an bestehenden Parametern vornehmen (Cam Exposure)
- Sie nur den Accept Threshold, Score Threshold usw. ändern
```

---

## Übersicht über die Benutzeroberfläche

Bevor Sie mit dem Training des Modells fortfahren, machen Sie sich mit der Benutzeroberfläche [Recipes](recipes) vertraut.

![Seite „Rezepte“](../../../../../_shared/media/images/pagina_recipesNEW.png)

## Speichern des Basisrezepts

Bevor Sie fortfahren, stellen Sie sicher, dass Sie das bei der Ersteinrichtung erstellte Basisrezept gespeichert haben:
:::{list-table}
  * - **1**
    - Klicken Sie auf der Hauptseite auf <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">
  * - **2**
    - Vergewissern Sie sich, dass das aktuelle Rezept das Basisrezept ist (z. B.: „Basisrezept“, das bei der Ersteinrichtung erstellt wurde)
  * - **3**
    - Klicken Sie auf <img src="../../../../../_shared/media/images/tasto_save_recipes.png" class="inline-icon">
  * - **4**
    - Behalten Sie den gleichen Namen im Speicherfeld bei (Sie überschreiben das Rezept mit den aktualisierten Konfigurationen)
  * - **5**
    - Bestätigen Sie die Speicherung
:::
```{important}

**Warum das Basisrezept speichern?**

Das Basisrezept enthält alle während der Einrichtung vorgenommenen Hardware-Konfigurationen:
- FlexiBowl®-Verbindung (IP, Parameter)
- Trichterverbindung
- Roboterverbindung (TCP/IP-Port)
- Kamerakalibrierung

Ein bereits vorbereitetes Basisrezept ermöglicht es, all diese Konfigurationen wiederzuverwenden, ohne sie erneut vornehmen zu müssen.
```

---
## Schritt 1: Duplizieren Sie das Basisrezept

Um mit der Erstellung des ersten Modells und damit mit der Konfiguration einer neuen Anwendung zu beginnen, empfiehlt es sich immer, das soeben gespeicherte Basisrezept zu duplizieren.
Dies ist nützlich, da so alle soeben konfigurierten Einstellungen separat gespeichert bleiben. Und das ist aus zwei Gründen von Vorteil:
- Um eine neue Anwendung mit demselben System zu starten, müssen Sie nicht alle bisher durchgeführten Schritte wiederholen
- Wenn sich nur ein Element in der Konfiguration ändert, können die Einstellungen aller anderen Komponenten beibehalten werden
```{list-table}
* - **6**
  - Klicken Sie auf der Hauptseite der Software FlexiVision One auf <img src="../../../../../_shared/media/images/tasto_recipes.png" class="inline-icon">
* - **7**
  - Es öffnet sich die Seite zur Rezeptverwaltung mit der Liste aller vorhandenen Rezepte
* - **8**
  - Wählen Sie das Basisrezept aus
* - **9**
  - Duplizieren Sie das Basisrezept
* - **10**
  - Klicken Sie auf „Load Recipe“ (Rezept laden)
* - **11**
  - Überprüfen Sie in der oberen Leiste, ob der angezeigte Name dem des neuen Rezepts entspricht
    :::{warning}
    **Arbeiten Sie immer mit dem richtigen Rezept**

    Wenn mehrere Rezepte vorhanden sind, überprüfen Sie immer, ob das richtige ausgewählt ist, bevor Sie Änderungen vornehmen. Änderungen, die am falschen Rezept vorgenommen werden, erfordern eine Neuausführung der Arbeit.
    :::
```
## Schritt 2: Benennung des Rezepts

Bevor Sie auf „Save Recipe“ (Rezept speichern) klicken, wählen Sie einen aussagekräftigen Namen.
```{list-table}
* - **12**
  - Das duplizierte Rezept umbenennen
    **Empfohlene Vorgehensweisen:**
    - Namen, die das Teil oder die Anwendung eindeutig identifizieren
    - Keine Leerzeichen (verwenden Sie `_` oder `-`)
    - Geben Sie relevante Informationen an (Art des Teils, Größe, Anwendung)
    
    :::{tip}
    **Vermeiden Sie allgemeine Namen**

    ❌ Zu vermeidende Namen:
    - `Test`, `Prova`, `Ricetta1`, `Nuova_Ricetta`

    ✓ Empfohlene Namen:
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    **Empfohlenes Format**: `[LINEA]_[PRODOTTO]_[VARIANTE]_[GG_MM_AAAA]`

    Ein eindeutiger Name erleichtert die Verwaltung, wenn Sie viele verschiedene Rezepte haben.
    :::
```
```{warning}
**Backup von Rezepten**

Nachdem Sie ein Rezept erstellt und konfiguriert haben:
- Nutzen Sie die Backup-Funktion der Software ([Backup Management](backup))
- Exportieren Sie die Rezepte regelmäßig auf einen externen Datenträger
- Dokumentieren Sie kritische Parameter in Papierform/digital

Ein gut konfiguriertes Rezept entspricht vielen Arbeitsstunden. Durch angemessenen Schutz beugen Sie Datenverlusten vor.
```

---

## Nächste Schritte

- **[Modell erstellen](18_NuovoModello.md)**
- **[ROI-Definition](roitest)**
- **[Konfiguration der Clearances](istogrammi)**
- **[Roboter-Pick-Kalibrierung](robotpick)**

```{tip}
**Was Sie für den nächsten Schritt benötigen**

- Zu erkennende physische Teile (mindestens 10-15 Teile)
- Leerer und sauberer FlexiBowl®
- Wenn das verwendete Roboterwerkzeug eine Greifzange ist, benötigen wir zusätzlich zwei Objekte, die sich von den Teilen unterscheiden, für die das Modell erstellt werden soll, um als Simulatoren für den Platzbedarf des Werkzeugs zu dienen.
- Blatt zum Notieren der Roboterkoordinaten (X, Y, RZ)
```
