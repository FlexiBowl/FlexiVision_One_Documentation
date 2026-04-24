# **FlexiVision One Manual**

## **Welcome to the FlexiVision One manual!**  
test We are pleased to welcome you to your new FlexiVision One guide!
This manual has been created specifically to serve as your clear and reliable reference. We hope that, by consulting it, you can fully benefit from everything our system offers.
Your opinion is essential to us: please do not hesitate to provide your feedback by [contacting us](https://www.flexibowl.it/contatti)! 

*- The Ars Automation Team*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **What is FlexiVision One?**  
FlexiVision One is our VisionController-based vision solution, designed to guide the robot and available as an add-on component for FlexiBowl® systems.
While retaining all the powerful functions of the previous version, therefore allowing the unloading, separation, recognition, and picking of loose parts on the feeder surface, FlexiVision One revolutionizes the user experience.
Thanks to complete step-by-step guidance and intuitive tools, we have greatly simplified the process, making programming and use accessible and usable by anyone, regardless of experience level.

## **System overview** 
Example system diagram with connections for up to three FlexiBowl units, three cameras, and three hoppers.

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Example diagram of the FlexiVision One system
```
## **How to read the manual**  
This manual has been designed to support both the design and system integration phase and the field installation and commissioning phase. 
For this reason, it is divided into macro-sections with different audiences and purposes.
  
## **Which section are you looking for?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - If you need to...
  - The information is located in...

* - Check dimensions, weights, electrical requirements, and communication protocols
  - [**TECHNICAL REFERENCE AND SPECIFICATIONS**](specifiche_tecniche)

* - Install components, wire the system, configure the network, or calibrate camera/robot
  - [**SYSTEM INSTALLATION**](Installazione_Meccanica) and [**QUICKSTART**](quickstart)

* - Program a new part model or configure the feeding system
  - [**QUICKSTART**](quickstart)

* - Troubleshoot problems or request assistance
  - [**TROUBLESHOOTING**](troubleshooting) and [**SUPPORT**](support)
```
## **Work groups and responsibilities**

Correct implementation of FlexiVision One requires collaboration among several professional roles. This table clarifies roles and responsibilities:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Professional role
  - Main responsibilities
  - Reference manual sections

* - **System integrator**
  - Layout design, component sizing, verification of technical requirements
  - Technical reference and specifications, Options

* - **Installation technician**
  - Mechanical assembly, electrical wiring, network configuration
  - System installation, Wiring and connections

* - **Robot programmer**
  - Camera-robot calibration, plugin integration, programming of picking logic
  - Quickstart, Protocol Setup, Calibration

* - **Line operator**
  - Creation of new part models, configuration of FlexiBowl parameters, performance monitoring
  - Run Time results verification

* - **Maintenance technician**
  - Problem diagnosis, component replacement, software updates
  - New model, FlexiBowl configuration, Troubleshooting, Support
```

## **Conventions and symbols used**

Throughout the manual, information banners are used to highlight important content:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Type
  - Meaning

* - ```{warning}
    Warning
    ```
  - Indicates a potentially hazardous situation or a critical procedure which, if not performed correctly, could cause equipment damage or serious system malfunctions.

* - ```{important}
    Important
    ```
  - Highlights essential information that must not be ignored in order to ensure correct system operation or operational safety.

* - ```{note}
    Information note
    ```
  - Provides essential information for correct execution of the procedure, technical clarifications, or references to related chapters.

* - ```{tip}
    Tip
    ```
  - Suggests a best practice, an alternative, or advice that can simplify installation or improve system performance.

* - ```{error}
    Error
    ```
  - Indicates a critical error or fault condition requiring immediate intervention. It highlights situations that compromise system operation and require corrective action.
```







```{toctree}
:hidden:
:caption: BEFORE STARTING 

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
:caption: TECHNICAL REFERENCE AND SPECIFICATIONS 

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
:caption: SYSTEM INSTALLATION

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
:caption: MIX APPLICATIONS

FlexiVisionEasy_manual/APPLICAZIONI_MIX/28_Panoramica_Mix.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/APPLICAZIONI_MIX/29_Comandi_Mix.md
```  

```{toctree}
:hidden:
:caption: MULTI-DEVICE CONFIGURATIONS

FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/30_2FB2CAM.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/31_3FB3CAM.md
```  


```{toctree}  
:hidden:
:caption: WARRANTY 

FlexiVisionEasy_manual/25_Garanzia.md
```

```{toctree}  
:hidden:
:caption: TROUBLESHOOTING

FlexiVisionEasy_manual/TROUBLESHOOTING/26_trb_shooting_guide.md
```






