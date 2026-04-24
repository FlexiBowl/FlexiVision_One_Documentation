# **FlexiVision One Handbuch**

## **Willkommen im FlexiVision One Handbuch!**  
test Wir freuen uns, Sie bei Ihrer neuen FlexiVision One Anleitung begrüßen zu dürfen!
Dieses Handbuch wurde eigens erstellt, um Ihnen als klare und zuverlässige Referenz zu dienen. Wir hoffen, dass Sie durch seine Nutzung alle Vorteile unseres Systems vollständig ausschöpfen können.
Ihre Meinung ist für uns sehr wichtig: Zögern Sie nicht, uns Ihr Feedback zu geben, indem Sie [uns kontaktieren](https://www.flexibowl.it/contatti)! 

*- Das Team von Ars Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Was ist FlexiVision One?**  
FlexiVision One ist unsere auf VisionController basierende Bildverarbeitungslösung, die zur Führung des Roboters entwickelt wurde und als Zusatzkomponente für FlexiBowl® Systeme erhältlich ist.
Unter Beibehaltung aller leistungsstarken Funktionen der vorherigen Version, wodurch das Entladen, Trennen, Erkennen und Entnehmen loser Teile auf der Oberfläche des Zuführsystems ermöglicht wird, revolutioniert FlexiVision One die Benutzererfahrung.
Dank einer vollständigen Schritt-für-Schritt-Anleitung und intuitiver Werkzeuge haben wir den Prozess stark vereinfacht, sodass Programmierung und Nutzung für jeden zugänglich und verwendbar sind, unabhängig vom Erfahrungsniveau.

## **Systemübersicht** 
Beispielhaftes Systemschema mit Verbindungen für bis zu drei FlexiBowl, drei Kameras und drei Hopper.

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Beispielhaftes Schema des FlexiVision One Systems
```
## **So lesen Sie das Handbuch**  
Dieses Handbuch wurde entwickelt, um sowohl die Phase der Systemplanung und -integration als auch die Installation und Inbetriebnahme im Feld zu unterstützen. 
Aus diesem Grund ist es in Makroabschnitte mit unterschiedlichen Zielgruppen und Zwecken gegliedert.
  
## **Welchen Abschnitt suchen Sie?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Wenn Sie...
  - Die Information befindet sich in...

* - Abmessungen, Gewichte, elektrische Anforderungen und Kommunikationsprotokolle prüfen müssen
  - [**TECHNISCHE REFERENZ UND SPEZIFIKATIONEN**](specifiche_tecniche)

* - Komponenten installieren, das System verkabeln, das Netzwerk konfigurieren oder Kamera/Roboter kalibrieren müssen
  - [**SYSTEMINSTALLATION**](Installazione_Meccanica) und [**QUICKSTART**](quickstart)

* - Ein neues Teilemodell programmieren oder das Zuführsystem konfigurieren müssen
  - [**QUICKSTART**](quickstart)

* - Probleme beheben oder Unterstützung anfordern müssen
  - [**FEHLERSUCHE**](troubleshooting) und [**SUPPORT**](support)
```
## **Arbeitsgruppen und Verantwortlichkeiten**

Die korrekte Implementierung von FlexiVision One erfordert die Zusammenarbeit verschiedener Fachrollen. Diese Tabelle erläutert Rollen und Verantwortlichkeiten:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Fachrolle
  - Hauptverantwortlichkeiten
  - Referenzabschnitte des Handbuchs

* - **Systemintegrator**
  - Layoutplanung, Dimensionierung der Komponenten, Prüfung der technischen Anforderungen
  - Technische Referenz und Spezifikationen, Optionen

* - **Installationstechniker**
  - Mechanische Montage, elektrische Verdrahtung, Netzwerkkonfiguration
  - Systeminstallation, Verkabelung und Anschlüsse

* - **Roboterprogrammierer**
  - Kamera-Roboter-Kalibrierung, Plugin-Integration, Programmierung der Entnahmelogiken
  - Quickstart, Protocol Setup, Kalibrierung

* - **Linienbediener**
  - Erstellung neuer Teilemodelle, Konfiguration der FlexiBowl-Parameter, Leistungsüberwachung
  - Prüfung der Run-Time-Ergebnisse

* - **Wartungstechniker**
  - Problemdiagnose, Austausch von Komponenten, Softwareaktualisierungen
  - Neues Modell, FlexiBowl-Konfiguration, Fehlersuche, Support
```

## **Verwendete Konventionen und Symbole**

Im gesamten Handbuch werden Informationsbanner verwendet, um wichtige Inhalte hervorzuheben:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Typ
  - Bedeutung

* - ```{warning}
    Warnung
    ```
  - Weist auf eine potenziell gefährliche Situation oder ein kritisches Verfahren hin, das bei nicht korrekter Ausführung zu Schäden an der Ausrüstung oder zu schwerwiegenden Systemstörungen führen kann.

* - ```{important}
    Wichtig
    ```
  - Hebt grundlegende Informationen hervor, die nicht ignoriert werden dürfen, um den ordnungsgemäßen Betrieb des Systems oder die Sicherheit des Vorgangs zu gewährleisten.

* - ```{note}
    Informationshinweis
    ```
  - Liefert wesentliche Informationen für die korrekte Durchführung des Verfahrens, technische Erläuterungen oder Verweise auf verwandte Kapitel.

* - ```{tip}
    Hinweis
    ```
  - Empfiehlt eine bewährte Vorgehensweise, eine Alternative oder einen Rat, der die Installation vereinfachen oder die Systemleistung verbessern kann.

* - ```{error}
    Fehler
    ```
  - Weist auf einen kritischen Fehler oder einen Störungszustand hin, der sofortiges Eingreifen erfordert. Kennzeichnet Situationen, die den Systembetrieb beeinträchtigen und Korrekturmaßnahmen erfordern.
```







```{toctree}
:hidden:
:caption: VOR DEM START 

FlexiVisionEasy_manual/01_informazioni_preliminari.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/02_informazioni_sicurezza.md
```  
```{toctree}
:hidden:
FlexiVisionEasy_manual/03_Unboxing_Contenuto.md
```    
```{toctree} 
:hidden:
FlexiVisionEasy_manual/27_Support.md

```
```{toctree} 
:hidden:
FlexiVisionEasy_manual/27b_Glossario.md

```

```{toctree}
:hidden:
:caption: TECHNISCHE REFERENZ UND SPEZIFIKATIONEN 

FlexiVisionEasy_manual/rif_tecnico_specifiche/04_Specifiche_FlexiVision.md
```    

```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md
```   

```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md
```    
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/integrazione_software/06_PlugIn.md
```    
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/integrazione_software/07_Backup_management.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/rif_tecnico_specifiche/08_Opzioni.md
```   
```{toctree}
:hidden:
:caption: SYSTEMINSTALLATION

FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md
```     
  
```{toctree}
:hidden:
:caption: QUICKSTART

FlexiVisionEasy_manual/QUICKSTART/12_Panoramica_Interfaccia.md
```     
```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/SETUP/13_setup.md
``` 


```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/24_Verifica_Risultati.md
```

```{toctree}
:hidden:
:caption: MIX-ANWENDUNGEN

FlexiVisionEasy_manual/APPLICAZIONI_MIX/28_Panoramica_Mix.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/APPLICAZIONI_MIX/29_Comandi_Mix.md
```  

```{toctree}
:hidden:
:caption: MEHRGERÄTE-KONFIGURATIONEN

FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/30_2FB2CAM.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/31_3FB3CAM.md
```  


```{toctree}  
:hidden:
:caption: GARANTIE 

FlexiVisionEasy_manual/25_Garanzia.md
```

```{toctree}  
:hidden:
:caption: FEHLERSUCHE

FlexiVisionEasy_manual/TROUBLESHOOTING/26_trb_shooting_guide.md
```






