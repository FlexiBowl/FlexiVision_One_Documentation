(start_control)=
# **Comando `start_control_`**

```{important}
**Función Expert**

La gestión de las cámaras de control (**Control Camera**) es una función **Expert**: requiere conocimientos de Cognex VisionPro y de scripts en C#, y está destinada a usuarios expertos. Para obtener información sobre el modo Expert, consulte [Qué es y cuándo se necesita](../EXPERT/32_Expert.md).
```

```{note}
**Requisitos previos**

El comando `start_control_` requiere una cámara de control configurada y un script de VisionPro cargado. Consulte [Cámaras de control](33_Telecamere_Controllo.md). Disponible a partir de la versión de software v0.24.
```

El comando `start_control_` permite al robot solicitar una inspección visual con una cámara de control. El robot puede añadir un parámetro de texto, que FlexiVision reenvía al [script de VisionPro](35_Script_VisionPro.md).

## Formato del comando

```
start_control_<parámetro>
```

El **guion bajo final** del prefijo es **obligatorio**. El parámetro puede estar vacío o contener números, letras y más guiones bajos.

```{list-table}
:header-rows: 1
:widths: 30 25 45

* - Comando enviado por el robot
  - Texto recibido por VisionPro
  - Comportamiento del script de ejemplo
* - `start_control_`
  - `""` (vacío)
  - Ejecuta ambas PMRedLine
* - `start_control_1`
  - `"1"`
  - Ejecuta solo la PMRedLine 1
* - `start_control_2`
  - `"2"`
  - Ejecuta solo la PMRedLine 2
* - `start_control_ABC_123`
  - `"ABC_123"`
  - Parámetro personalizado: requiere lógica específica en el script
```

```{important}
El parámetro se trata como **texto**. FlexiVision no atribuye ningún significado a valores como `ABC_123`: es el script de VisionPro del cliente el que debe interpretarlos.
```

```{note}
`start_control_ 1` también se lee como parámetro `"1"`: los espacios al principio y al final se eliminan. Para evitar ambigüedades, se recomienda enviar `start_control_1`, sin espacios.

El prefijo `start_control_` no se pasa al script: solo llega la parte siguiente (por ejemplo `"2"` para `start_control_2`).
```

El comando también puede ejecutarse **sin robot conectado** desde la HMI mediante **Test Tool**; en ese caso el resultado se muestra en la HMI pero no se transmite por TCP.

## Respuesta al robot

La respuesta es la cadena `Output_String` generada por el script de VisionPro. El formato que se muestra a continuación es el del **script de ejemplo** y puede adaptarse al protocolo requerido por el robot.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Situación
  - Ejemplo de Output_String
* - Objeto encontrado
  - `X=125.450;Y=78.320;Rz=45.000`
* - Ningún objeto encontrado
  - `Not_Found`
* - Ambas herramientas ejecutadas
  - `1:X=125.450;Y=78.320;Rz=45.000|2:Not_Found`
* - Parámetro no previsto
  - `#Error_Control_INVALID_CONTROL`
* - Error en la herramienta 2
  - `#Error_Control_TOOL_RUN;Tool=2`
```

Para cada herramienta ejecutada se utiliza únicamente el **primer objeto** reconocido. Si se ejecutan ambas herramientas, las respuestas van precedidas de los prefijos `1:` y `2:` y separadas por `|`.

```{note}
- `X` e `Y` se expresan en el sistema de coordenadas configurado en la herramienta de VisionPro (píxeles o unidades calibradas): no están automáticamente en milímetros.
- `Rz` se expresa en grados.
- Tres decimales; el punto se utiliza siempre como separador decimal, independientemente del idioma de Windows.
```

### Not_Found y errores

`Not_Found` **no es un error**: indica que la herramienta se ejecutó pero no encontró ningún objeto. Los **errores de los scripts de control** comienzan siempre con el prefijo `#Error_Control_`; los errores de la cámara pueden comunicarse por separado con el prefijo `#Error_Camera`. Si al menos una herramienta produce un error de ejecución, el script escribe el error al principio de la respuesta (en el ejemplo tiene prioridad la herramienta 1).

La lista completa de mensajes y acciones recomendadas está disponible en [Solución de problemas – Cámaras de control](../TROUBLESHOOTING/26j_Telecamere_Controllo.md).

## Ejemplos de intercambio

**Caso A – solo Locator 2**

Comando enviado por el robot: `start_control_2`. VisionPro recibe `Input_Control = "2"`, ejecuta `CogPMRedLineTool2`, lee X, Y y Rz del primer resultado y produce la respuesta de texto. La pantalla muestra el registro de la herramienta 2.

**Caso B – dos Locators**

Comando enviado: `start_control_`. VisionPro recibe una cadena vacía y ejecuta ambas herramientas. La respuesta contiene dos secciones, una por cada locator. El registro de la imagen procede de la herramienta 1, salvo que se elija otra cosa en el script.

**Caso C – parámetro de aplicación**

Comando enviado: `start_control_ABC_123`. El parámetro llega a VisionPro sin ser interpretado por FlexiVision. El script de ejemplo responde `#Error_Control_INVALID_CONTROL`; para usarlo como comando real hay que añadir la lógica correspondiente en el script C#.

```{tip}
Para la lista completa de los comandos del robot, consulte [Protocolo de comunicación Robot-Visión](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md).
```
