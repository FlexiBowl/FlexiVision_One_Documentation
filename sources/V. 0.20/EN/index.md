# **FlexiVision One Manual**

## **Welcome to the FlexiVision One manual!**  
We are excited to welcome you to your new FlexiVision One guide!
This manual has been specifically drafted to be your clear and reliable reference. We hope that, by consulting it, you will fully enjoy all the benefits of our system.
Your opinion is crucial to us: please do not hesitate to give us your feedback [by contacting us](https://www.flexibowl.it/contatti)!

*- The ARS Automation Team*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **What is FlexiVision One?**  
FlexiVision One is our vision solution based on VisionController, designed to guide the robot and available as an add-on for FlexiBowl® systems.
Retaining all the full-capacity functions of the previous version, thus allowing unloading, separation, identification and picking of bulk parts on the feeder surface, FlexiVision One revolutionises the user’s experience.
With comprehensive step-by-step guidance and intuitive tools, we have greatly simplified the process, making programming and operation accessible and usable by anyone, regardless of their level of expertise.

## **System overview** 

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Example diagram of the FlexiVision One system
```
## **How to read the manual**  
This manual is intended to support both the system design and integration phase, as well as the on-field installation and commissioning phase.
For this reason, it is divided into macro-sections with distinct addressees and purposes.
  
## **Which section are you looking for?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - If you must...
  - The information can be found in...

* - Check dimensions, weights, electrical requirements and communication protocols
  - [**TECHNICAL REFERENCE AND SPECIFICATIONS**](specifiche_tecniche)

* - Install the components, wire the system, configure the network or calibrate the camera/robot
  - [**SYSTEM INSTALLATION**](Installazione_Meccanica) and [**QUICKSTART**](setupcomponenti)

* - Program a new part model or configure the feed system
  - [**QUICKSTART**](setupcomponenti)

* - Solve problems or request assistance
  - [**TROUBLESHOOTING**](troubleshooting) and [**SUPPORT**](support)
```
## **Intervention groups and responsibilities**

The successful implementation of FlexiVision One requires the collaboration of several professionals. This table establishes roles and responsibilities:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Professional figure
  - Main responsibilities
  - Sections of the reference manual

* - **System Integrator**
  - Layout design, component dimensioning, assessment of technical requirements
  - Technical reference and specifications, Options

* - **Installation technician**
  - Mechanical assembly, electrical wiring, network configuration
  - System installation, wiring and connections

* - **Robot programmer**
  - Camera-robot calibration, plugin integration, pick logic programming
  - Quickstart, Protocol Setup, Calibration

* - **Line operator**
  - Creating new part models, configuring FlexiBowl® parameters, monitoring performance
  - Checking Run Time results

* - **Maintenance technician**
  - Troubleshooting, component replacement, software upgrades
  - New model, FlexiBowl® configuration, Troubleshooting, Support
```

## **Conventions and symbols used**

Throughout the manual, information banners are used to highlight important content:

```{list-table}
:header-rows: 1

* - Type
  - Meaning

* - ```{warning}
    Warning
    ```
  - Indicates a potentially hazardous situation or critical procedure which, if not carried out correctly, could result in damage to the equipment or serious system malfunctioning.

* - ```{important}
    Important
    ```
  - Highlights vital information that must not be ignored to ensure the correct functioning of the system or the safety of the operation.

* - ```{note}
    Information note
    ```
  - Provides essential information to correctly carry out the procedure, technical clarifications or references to related chapters.

* - ```{tip}
    Tip
    ```
  - Suggests a best practice, alternative or advice that can simplify installation or improve system performance.

* - ```{error}
    Error
    ```
  - Indicates a critical error or faulty condition requiring immediate action. It signals situations that jeopardise system operation and require corrective action.
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
:caption: INTERFACE OVERVIEW

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
```

```{toctree}
:hidden:
:caption: EXPERT

FlexiVisionEasy_manual/EXPERT/32_Expert.md
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






