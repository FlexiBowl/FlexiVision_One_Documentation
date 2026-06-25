# **FlexiVision One Manual**

## **¡Bienvenido al manual de FlexiVision One!**
Nos complace darle la bienvenida a su nueva guía FlexiVision One
Este manual ha sido especialmente creado para ser su referencia clara y fiable. Esperamos que, al consultarlo, disfrute de todas las ventajas de nuestro sistema.
Su opinión es crucial para nosotros: ¡no dude en hacernos llegar sus comentarios [poniéndose en contacto con nosotros](https://www.flexibowl.it/contatti)!

*- El equipo de automatización de ARS*  
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **¿Qué es FlexiVision One?**
FlexiVision One es nuestra solución de visión basada en VisionController, diseñada para el guiado de robots y disponible como complemento para los sistemas FlexiBowl®.
Manteniendo todas las potentes funcionalidades de la versión anterior, que permiten descargar, separar, reconocer y recoger piezas a granel en la superficie del alimentador, FlexiVision One revoluciona la experiencia del usuario.
Con una completa guía paso a paso y herramientas intuitivas, hemos simplificado enormemente el proceso, haciendo que la programación y el funcionamiento sean accesibles y utilizables por cualquiera, independientemente de su nivel de experiencia.

## **Visión general del sistema**

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Ejemplo de diagrama del sistema FlexiVision One
```
## **Cómo leer el manual**
Este manual está diseñado para apoyar tanto la fase de diseño e integración del sistema como la fase de instalación y puesta en marcha sobre el terreno.
Por ello, se divide en macrosecciones con destinatarios y propósitos distintos.
  
## **¿Qué sección está buscando?**
```{list-table}
:widths: 40 60
:header-rows: 1

* - Si tienes que...
  - La información puede encontrarse en...

* - Compruebe las dimensiones, pesos, requisitos eléctricos y protocolos de comunicación
  - [**REFERENCIA TÉCNICA Y ESPECIFICACIONES**](lock id=)

* - Instalar los componentes, cablear el sistema, configurar la red o calibrar la cámara/robot
  - [**INSTALACIÓN DEL SISTEMA**](lock id=) e [**INICIO RÁPIDO**](lock id=)

* - Programación de un nuevo modelo de pieza o configuración del sistema de alimentación
  - [**INICIO RÁPIDO**](setupcomponenti)

* - Solución de problemas o solicitud de asistencia
  - [**SOLUCIÓN DE PROBLEMAS**](lock id=) e [**APOYO**](lock id=)
```
## **Grupos de intervención y responsabilidades**

El éxito de la implantación de FlexiVision One requiere la colaboración de varios profesionales. Este cuadro aclara las funciones y responsabilidades:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Figura profesional
  - Principales responsabilidades
  - Secciones del Manual de referencia

* - **Integrador de sistemas**
  - Diseño de maquetas, dimensionamiento de componentes, verificación de requisitos técnicos
  - Referencias y especificaciones técnicas, Opciones

* - **Técnico de instalación**
  - Montaje mecánico, cableado eléctrico, configuración de redes
  - Instalación de sistemas, cableado y conexiones

* - **Programador de robots**
  - Calibración cámara-robot, integración de plugins, programación de la lógica de recogida
  - Quickstart, Protocol Setup, Calibración

* - **Operador de línea**
  - Creación de nuevos modelos de piezas, configuración de los parámetros FlexiBowl®, supervisión del rendimiento
  - Verificación de resultados Run Time

* - **Mantenedor**
  - Resolución de problemas, sustitución de componentes, actualizaciones de software
  - Nuevo modelo, Configuración FlexiBowl®, Troubleshooting, Soporte
```

## **Convenciones y símbolos utilizados**

A lo largo del manual se utilizan banners informativos para destacar contenidos importantes:

```{list-table}
:header-rows: 1
:widths: 30 70

* - Tipo
  - Significado
* - ```{warning} Advertencia
    ```
  - Indica una situación potencialmente peligrosa o un procedimiento crítico que, si no se realiza correctamente, puede provocar daños en el equipo o un mal funcionamiento grave del sistema.
* - ```{important} Importante
    ```
  - Destaca información vital que no debe ignorarse para garantizar el correcto funcionamiento del sistema o la seguridad de la operación.
* - ```{note} Nota informativa
    ```
  - Proporciona información esencial para la correcta realización del procedimiento, aclaraciones técnicas o referencias a capítulos relacionados.
* - ```{tip} Consejo
    ```
  - Sugiere una mejor práctica, alternativa o consejo que puede simplificar la instalación o mejorar el rendimiento del sistema.
* - ```{error} Error
    ```
  - Indica una condición crítica de error o fallo que requiere una acción inmediata. Señala situaciones que comprometen el funcionamiento del sistema y requieren medidas correctoras.
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
:caption: PANORÁMICA DE LA INTERFAZ

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
:caption: INICIO RÁPIDO
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
:caption: EXPERTO

FlexiVisionEasy_manual/EXPERT/32_Expert.md
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






