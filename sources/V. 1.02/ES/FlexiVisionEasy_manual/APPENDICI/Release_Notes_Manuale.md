# Manual FlexiVision One

Esta página recoge el historial de revisiones de este manual e indica con qué versiones del software FlexiVision One es compatible cada revisión.

```{important}
Consulte siempre la versión del manual compatible con la versión del software instalada para acceder a la información más actualizada sobre funcionalidades, seguridad y procedimientos.
```

## Compatibilidad

| Versión del manual | Versiones compatibles del software FlexiVision One |
|---|---|
| **1.02** (actual) | v0.23, v0.24 |
| **1.01** | v0.21, v0.22 |
| **1.00** | v0.20, v0.21, v0.22 |

## Historial de revisiones

### Versión 1.02

Fecha de publicación: 17/11/2026

**Páginas añadidas**

- Nueva sección **Cámaras de control**, con las páginas:
  - [Cámaras de control](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md): descripción general, secuencia de funcionamiento, uso desde la HMI (Setup Camera Ctrl, Setup Tool Ctrl, View Runtime, Test Tool) y prueba rápida de aceptación.
  - [Comando `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md): formato del comando, parámetros, respuestas al robot y ejemplos de intercambio.
  - [Script de VisionPro](../TELECAMERE_CONTROLLO/35_Script_VisionPro.md): interfaz del ToolBlock, personalización del script y Apéndice A con el script C# completo.
- Añadida la página [Solución de problemas – Cámaras de control](../TROUBLESHOOTING/26j_Telecamere_Controllo.md) con los mensajes `#Error_Control_…` y `#Error_Camera…` y las acciones recomendadas.
- Todas las páginas de la sección Cámaras de control muestran en la parte superior un banner que indica que la **Control Camera** es una función **Expert**.

**Páginas actualizadas**

- [Protocolo de comunicación Robot-Visión](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): añadida la subsección «Comandos de las cámaras de control» con el comando `start_control_<parámetro>`.
- [Solución de problemas](../TROUBLESHOOTING/26_trb_shooting_guide.md): añadida la ficha «Cámaras de control».
- [Glosario](../27b_Glossario.md): añadidos los términos CogRecord, PMRedLine, Cámara de control, ToolBlock y VisionPro.
- Notas de la versión – Software: añadidas las versiones [V. 0.23](V.0.23.md) y [V. 0.24](V.0.24.md) y actualizada la página [Software FlexiVision One](Release_Notes_Software.md).
- Actualizada la tabla de compatibilidad con las versiones de software v0.23 y v0.24.

### Versión 1.01

Fecha de publicación: 04/09/2026

- Añadida la página **Check Belt** (Monitorización de la Cinta) en el Quickstart y la entrada correspondiente en la página Setup de la Visión general de la interfaz.
- Actualizada la sección Hopper Setup con los procedimientos guiados **Wizard Steps** y **Wizard Time**.
- Actualizada la sección Histogramas con la elección del tipo de región para las Clearances (Rectangle, Annulus Section, Circle).
- Actualizada la sección Aplicaciones Mix con los comandos multimodelo `mix_Locator_<modelos>` y la protección para los comandos ya en ejecución.
- Añadida al Protocolo de Comunicación Robot-Visión la subsección "Cómo utilizar correctamente los comandos Start y Mix".
- Actualizada la sección FlexiBowl® Setup: introducción manual de los parámetros desde el teclado y aviso en caso de parámetros no sincronizados.
- Actualizada la sección Robot Pick: formato de los offsets con el punto como separador decimal y control del Picking Offset antes de continuar con **Next**.
- Añadida a la sección Setup la indicación sobre el control del nivel de acceso del usuario.
- Reorganizada la sección Notas de la versión, separando las notas del software FlexiVision One de las del manual.

### Versión 1.00

Fecha de publicación: 01/08/2026

- Primera edición del manual.

