# **Manual FlexiVision One**

## **¡Bienvenido al manual de FlexiVision One!**  
test Nos complace darte la bienvenida a tu nueva guía de FlexiVision One.
Este manual ha sido creado específicamente para ser tu punto de referencia claro y fiable. Esperamos que, al consultarlo, puedas aprovechar plenamente todos los beneficios de nuestro sistema.
Tu opinión es fundamental para nosotros: no dudes en enviarnos tus comentarios [contactándonos](https://www.flexibowl.it/contatti)! 

*- El Equipo de Ars Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **¿Qué es FlexiVision One?**  
FlexiVision One es nuestra solución de visión basada en VisionController, diseñada para guiar al robot y disponible como componente adicional para los sistemas FlexiBowl®.
Manteniendo todas las potentes funcionalidades de la versión anterior, permitiendo por tanto la descarga, separación, reconocimiento y recogida de piezas a granel sobre la superficie del alimentador, FlexiVision One revoluciona la experiencia de usuario.
Gracias a una guía completa paso a paso y a herramientas intuitivas, hemos simplificado enormemente el proceso, haciendo que la programación y el uso sean accesibles y utilizables por cualquier persona, independientemente de su nivel de experiencia.

## **Vista general del sistema** 
Esquema ejemplificativo del sistema con conexiones de hasta tres FlexiBowl, tres cámaras y tres hoppers.

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Esquema ejemplificativo del sistema FlexiVision One
```
## **Cómo leer el manual**  
Este manual ha sido concebido para apoyar tanto la fase de diseño e integración del sistema como la fase de instalación y puesta en servicio en campo. 
Por este motivo, está dividido en macrosecciones con destinatarios y finalidades distintas.
  
## **¿Cuál es la sección que estás buscando?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Si necesitas...
  - La información se encuentra en...

* - Verificar dimensiones, pesos, requisitos eléctricos y protocolos de comunicación
  - [**REFERENCIA TÉCNICA Y ESPECIFICACIONES**](specifiche_tecniche)

* - Instalar los componentes, cablear el sistema, configurar la red o calibrar cámara/robot
  - [**INSTALACIÓN DEL SISTEMA**](Installazione_Meccanica) y [**QUICKSTART**](quickstart)

* - Programar un nuevo modelo de pieza o configurar el sistema de alimentación
  - [**QUICKSTART**](quickstart)

* - Resolver problemas o solicitar asistencia
  - [**SOLUCIÓN DE PROBLEMAS**](troubleshooting) y [**SOPORTE**](support)
```
## **Grupos de intervención y responsabilidades**

La correcta implementación de FlexiVision One requiere la colaboración de diferentes figuras profesionales. Esta tabla aclara funciones y responsabilidades:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Figura profesional
  - Responsabilidades principales
  - Secciones de referencia del manual

* - **Integrador de sistema**
  - Diseño del layout, dimensionamiento de componentes, verificación de requisitos técnicos
  - Referencia técnica y especificaciones, Opciones

* - **Técnico instalador**
  - Montaje mecánico, cableado eléctrico, configuración de red
  - Instalación del sistema, Cableado y conexiones

* - **Programador robot**
  - Calibración cámara-robot, integración de plugin, programación de lógicas de recogida
  - Quickstart, Protocol Setup, Calibración

* - **Operador de línea**
  - Creación de nuevos modelos de pieza, configuración de parámetros FlexiBowl, monitorización de prestaciones
  - Verificación de resultados Run Time

* - **Técnico de mantenimiento**
  - Diagnóstico de problemas, sustitución de componentes, actualizaciones de software
  - Nuevo modelo, Configuración FlexiBowl, Solución de problemas, Soporte
```

## **Convenciones y símbolos utilizados**

En todo el manual se utilizan banners informativos para resaltar contenidos importantes:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Tipo
  - Significado

* - ```{warning}
    Advertencia
    ```
  - Indica una situación potencialmente peligrosa o un procedimiento crítico que, si no se realiza correctamente, podría provocar daños al equipo o fallos graves del sistema.

* - ```{important}
    Importante
    ```
  - Resalta información fundamental que no debe ignorarse para garantizar el correcto funcionamiento del sistema o la seguridad de la operación.

* - ```{note}
    Nota informativa
    ```
  - Proporciona información esencial para el correcto desarrollo del procedimiento, aclaraciones técnicas o referencias a capítulos relacionados.

* - ```{tip}
    Sugerencia
    ```
  - Sugiere una práctica óptima, una alternativa o un consejo que puede simplificar la instalación o mejorar las prestaciones del sistema.

* - ```{error}
    Error
    ```
  - Indica un error crítico o una condición de fallo que requiere intervención inmediata. Señala situaciones que comprometen el funcionamiento del sistema y requieren una acción correctiva.
```







```{toctree}
:hidden:
:caption: ANTES DE EMPEZAR 

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
:caption: REFERENCIA TÉCNICA Y ESPECIFICACIONES 

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
:caption: INSTALACIÓN DEL SISTEMA

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
:caption: APLICACIONES MIX

FlexiVisionEasy_manual/APPLICAZIONI_MIX/28_Panoramica_Mix.md
```  

```{toctree}
:hidden:
FlexiVisionEasy_manual/APPLICAZIONI_MIX/29_Comandi_Mix.md
```  

```{toctree}
:hidden:
:caption: CONFIGURACIONES MULTIDISPOSITIVO

FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/30_2FB2CAM.md
```

```{toctree}
:hidden:
FlexiVisionEasy_manual/CONFIGURAZIONI_MULTI-DISPOSITIVO/31_3FB3CAM.md
```  


```{toctree}  
:hidden:
:caption: GARANTÍA 

FlexiVisionEasy_manual/25_Garanzia.md
```

```{toctree}  
:hidden:
:caption: SOLUCIÓN DE PROBLEMAS

FlexiVisionEasy_manual/TROUBLESHOOTING/26_trb_shooting_guide.md
```






