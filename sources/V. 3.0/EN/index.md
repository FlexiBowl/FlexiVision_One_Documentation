# **FlexiVision One Manual**

## **Welcome to the FlexiVision One manual!**
We are pleased to welcome you to your new FlexiVision One guide.
This manual has been created to serve as a clear and reliable reference point. We hope it helps you make the most of all the benefits offered by our system.
Your feedback is important to us, so please do not hesitate to share your comments by [contacting us](https://www.flexibowl.it/contatti)!

*- The Ars Automation Team*
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>

## **What is FlexiVision One?**
FlexiVision One is our VisionController-based vision solution designed to guide the robot and available as an add-on component for FlexiBowl(R) systems.
While retaining all the powerful features of the previous version, including unloading, separation, recognition, and picking of loose parts on the feeder surface, FlexiVision One takes the user experience to a new level.
Thanks to a complete step-by-step guide and intuitive tools, we have greatly simplified programming and daily operation, making the system accessible to users at any experience level.

## **System overview**
Example layout of a system with connections for up to three FlexiBowls, three cameras, and three hoppers.

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Example layout of the FlexiVision One system
```

## **How to read this manual**
This manual has been designed to support both the design and system integration phase and the installation and commissioning phase in the field.
For this reason, it is divided into macro-sections intended for different users and purposes.

## **Which section are you looking for?**
```{list-table}
:widths: 40 60
:header-rows: 1

* - If you need to...
  - You can find the information in...

* - Check dimensions, weights, electrical requirements, and communication protocols
  - [**TECHNICAL REFERENCE AND SPECIFICATIONS**](specifiche_tecniche)

* - Install components, wire the system, configure the network, or calibrate the camera/robot
  - [**SYSTEM INSTALLATION**](Installazione_Meccanica) and [**QUICKSTART**](quickstart)

* - Program a new part model or configure the feeding system
  - [**QUICKSTART**](quickstart)

* - Troubleshoot issues or request assistance
  - [**TROUBLESHOOTING**](troubleshooting) and [**SUPPORT**](support)
```

## **Intervention groups and responsibilities**

The correct implementation of FlexiVision One requires collaboration among several professional roles. This table clarifies responsibilities and reference sections:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Professional role
  - Main responsibilities
  - Reference manual sections

* - **System integrator**
  - Layout design, component sizing, technical requirement verification
  - Technical reference and specifications, Options

* - **Installation technician**
  - Mechanical assembly, electrical wiring, network configuration
  - System installation, Wiring and connections

* - **Robot programmer**
  - Camera-robot calibration, plugin integration, picking logic programming
  - Quickstart, Protocol Setup, Calibration

* - **Line operator**
  - Creation of new part models, FlexiBowl parameter configuration, performance monitoring
  - Runtime result verification

* - **Maintenance technician**
  - Fault diagnosis, component replacement, software updates
  - New model, FlexiBowl configuration, Troubleshooting, Support
```

## **Conventions and symbols used**

Informational banners are used throughout the manual to highlight important content:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Type
  - Meaning

* - ```{warning}
    Warning
    ```
  - Indicates a potentially dangerous situation or a critical procedure that, if not carried out correctly, could cause equipment damage or serious system malfunctions.

* - ```{important}
    Important
    ```
  - Highlights key information that must not be ignored in order to ensure proper system operation or safe execution of the task.

* - ```{note}
    Informational note
    ```
  - Provides essential information for correct procedure execution, technical clarification, or references to related chapters.

* - ```{tip}
    Tip
    ```
  - Suggests a best practice, an alternative, or a recommendation that can simplify installation or improve system performance.

* - ```{error}
    Error
    ```
  - Indicates a critical error or fault condition that requires immediate action. It highlights situations that compromise system operation and need corrective intervention.
```

```{toctree}
:hidden:
:caption: BEFORE YOU START

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
