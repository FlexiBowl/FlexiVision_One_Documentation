# **FlexiVision One Handbuch**

## **Willkommen im Handbuch zu FlexiVision One!**  
Wir freuen uns, Sie bei Ihrem neuen FlexiVision One-Handbuch willkommen zu heißen!
Dieses Handbuch wurde speziell als klarer und zuverlässiger Leitfaden für Sie erstellt. Wir hoffen, dass Sie durch die Nutzung dieses Handbuchs alle Vorteile unseres Systems voll ausschöpfen können.
Ihre Meinung ist uns wichtig: Zögern Sie nicht, uns Ihr Feedback mitzuteilen, [indem Sie uns kontaktieren](https://www.flexibowl.it/contatti)! 

*- Das Team von ARS Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Was ist FlexiVision One?**  
FlexiVision One ist unsere auf dem VisionController basierende Bildverarbeitungslösung, die zur Steuerung des Roboters entwickelt wurde und als Zusatzkomponente für FlexiBowl®-Systeme erhältlich ist.
FlexiVision One behält alle leistungsstarken Funktionen der Vorgängerversion bei und ermöglicht somit das Entladen, Trennen, Erkennen und Entnehmen von Schüttgut auf der Oberfläche des Zuführers. Gleichzeitig revolutioniert es die Benutzererfahrung.
Dank einer umfassenden Schritt-für-Schritt-Anleitung und intuitiver Werkzeuge haben wir den Prozess extrem vereinfacht, sodass die Programmierung und Nutzung für jeden zugänglich und nutzbar ist, unabhängig vom Erfahrungsniveau.

## **Systemübersicht** 

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Beispieldiagramm des FlexiVision One-Systems
```
## **Hinweise zum Lesen des Handbuchs**  
Dieses Handbuch soll sowohl die Planungs- und Systemintegrationsphase als auch die Installation und Inbetriebnahme vor Ort unterstützen. 
Aus diesem Grund ist es in Makroabschnitte mit unterschiedlichen Zielgruppen und Schwerpunkten unterteilt.
  
## **Welchen Abschnitt suchen Sie?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Wenn Sie...
  - finden Sie die Informationen unter...

* - Abmessungen, Gewichte, elektrische Anforderungen und Kommunikationsprotokolle überprüfen möchten
  - [**TECHNISCHE HINWEISE UND SPEZIFIKATIONEN**](specifiche_tecniche)

* - Komponenten installieren, das System verkabeln, das Netzwerk konfigurieren oder Kamera/Roboter kalibrieren möchten
  - [**SYSTEMINSTALLATION**](Installazione_Meccanica) und [**QUICKSTART**](setupcomponenti)

* - Ein neues Werkstückmodell programmieren oder das Zuführsystem konfigurieren möchten
  - [**QUICKSTART**](setupcomponenti)

* - Probleme beheben oder Support anfordern möchten
  - [**FEHLERSUCHE**](troubleshooting) und [**SUPPORT**](support)
```
## **Aufgabenbereiche und Verantwortlichkeiten**

Die korrekte Implementierung von FlexiVision One erfordert die Zusammenarbeit verschiedener Fachleute. Diese Tabelle verdeutlicht die Rollen und Verantwortlichkeiten:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Fachkraft
  - Hauptaufgaben
  - Abschnitte des Referenzhandbuchs

* - **Systemintegrator**
  - Layoutplanung, Dimensionierung der Komponenten, Überprüfung der technischen Anforderungen
  - Technische Hinweise und Spezifikationen, Optionen

* - **Installationstechniker**
  - Mechanische Montage, elektrische Verkabelung, Netzwerkkonfiguration
  - Systeminstallation, Verkabelung und Anschlüsse

* - **Roboterprogrammierer**
  - Kamera-Roboter-Kalibrierung, Plugin-Integration, Programmierung der Aufnahmelogik
  - Quickstart, Protokoll-Setup, Kalibrierung

* - **Anlagenbediener**
  - Erstellung neuer Werkstückmodelle, Konfiguration der FlexiBowl®-Parameter, Überwachen der Leistung
  - Überprüfung der Laufzeitergebnisse

* - **Wartungstechniker**
  - Fehlerdiagnose, Austausch von Komponenten, Software-Updates
  - Neues Modell, FlexiBowl®-Konfiguration, Fehlerbehebung, Support
```

## **Verwendete Begriffe und Symbole**

Im gesamten Handbuch werden Informationsbanner verwendet, um wichtige Inhalte hervorzuheben:

```{list-table}
:header-rows: 1

* - Typ
  - Bedeutung

* - ```{warning}
    Warnung
    ```
  - Weist auf eine potenziell gefährliche Situation oder einen kritischen Vorgang hin, der bei unsachgemäßer Ausführung zu Schäden am Gerät oder schwerwiegenden Systemfehlern führen kann.

* - ```{important}
    Wichtig
    ```
  - Hebt grundlegende Informationen hervor, die nicht ignoriert werden dürfen, um den ordnungsgemäßen Betrieb des Systems oder die Sicherheit des Vorgangs zu gewährleisten.

* - ```{note}
    Hinweis
    ```
  - Enthält wichtige Informationen für die ordnungsgemäße Durchführung des Vorgangs, technische Erläuterungen oder Verweise auf verwandte Kapitel.

* - ```{tip}
    Tipp
    ```
  - Schlägt eine bewährte Vorgehensweise, eine Alternative oder einen Ratschlag vor, der die Installation vereinfachen oder die Systemleistung verbessern kann.

* - ```{error}
    Fehler
    ```
  - Weist auf einen kritischen Fehler oder einen Fehlerzustand hin, der sofortiges Eingreifen erfordert. Weist auf Situationen hin, die den Betrieb des Systems beeinträchtigen und Korrekturmaßnahmen erfordern.
```







```{toctree}
:hidden:
:caption: BEVOR SIE ANFANGEN 

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
:caption: TECHNISCHE HINWEISE UND SPEZIFIKATIONEN 

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
:caption: ÜBERSICHT ÜBER DIE BENUTZEROBERFLÄCHE

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12a_Home.md
```  
```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12c_Dashboard.md
```    
```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12b_Recipes.md
```    
```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12d_Setup.md
```    

```{toctree}
:hidden:

FlexiVisionEasy_manual/PANORAMICA_INTERFACCIA/12e_TastiInfo.md
```    

```{toctree}
:hidden:
:caption: QUICKSTART
FlexiVisionEasy_manual/QUICKSTART/SETUP/13_setup.md
``` 


```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/Nuovo_Modello/16_Nuovo_modello.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/QUICKSTART/24_Verifica_Risultati.md
FlexiVisionEasy_manual/QUICKSTART/25_CheckBelt.md
```

```{toctree}
:hidden:
:caption: EXPERT

FlexiVisionEasy_manual/EXPERT/32_Expert.md
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
:caption: MULTI-GERÄTE-KONFIGURATIONEN

FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/30_2FB2CAM.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/31_3FB3CAM.md
```  


```{toctree}  
:hidden:
:caption: GARANTIE 

FlexiVisionEasy_manual/25_Garantie.md
```

```{toctree}  
:hidden:
:caption: FEHLERSUCHE

FlexiVisionEasy_manual/TROUBLESHOOTING/26_trb_shooting_guide.md
```
```{toctree}  
:hidden:
:caption: APPENDICI

FlexiVisionEasy_manual/APPENDICI/Release_Notes.md
```






