(telecamere_controllo)=
# **Cámaras de control**

```{important}
**Función Expert**

La gestión de las cámaras de control (**Control Camera**) es una función **Expert**: requiere conocimientos de Cognex VisionPro y de scripts en C#, y está destinada a usuarios expertos. Para obtener información sobre el modo Expert, consulte [Qué es y cuándo se necesita](../EXPERT/32_Expert.md).
```

```{note}
**Disponible a partir de la versión de software v0.24**

Las funciones descritas en esta sección se introdujeron con FlexiVision One v0.24. Consulte las [Notas de la versión – V. 0.24](../APPENDICI/V.0.24.md).
```

Además de la cámara de visión utilizada para la recogida, FlexiVision One gestiona **3 cámaras de control independientes**, asociadas respectivamente a **FLB1**, **FLB2** y **FLB3**. Las cámaras de control permiten realizar una **inspección visual** a petición del robot, por ejemplo la verificación de una pieza recogida, y devolver al robot el resultado del control.

## Para qué sirve

El comando `start_control_` permite al robot solicitar a FlexiVision una inspección con una cámara de control. El robot puede añadir un **parámetro de texto** después del guion bajo (`_`): FlexiVision reenvía el parámetro al **script de VisionPro**, que decide qué herramientas ejecutar y qué resultados devolver.

```{important}
**Principio de funcionamiento**

La configuración de la HMI no cambia: el cliente puede adaptar las reglas de inspección y el formato de los resultados modificando su propio **script de VisionPro**, sin intervenir en la interfaz de FlexiVision One.
```

## Secuencia de funcionamiento

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - #
  - Actor
  - Acción
* - 1
  - **Robot**
  - Envía `start_control_` o `start_control_<parámetro>`.
* - 2
  - **FlexiVision**
  - Adquiere la imagen con la cámara de control asociada e inicia el script de VisionPro.
* - 3
  - **VisionPro**
  - Ejecuta las herramientas seleccionadas y prepara una respuesta de texto y un registro gráfico.
* - 4
  - **FlexiVision**
  - Muestra la imagen y la cadena en la HMI; envía la cadena al robot **solo si está conectado**.
```

Para cada control, FlexiVision gestiona un **Main Task** dedicado a la cámara de control, con gestión de errores, registro (logging) y envío de los resultados al robot.

## Uso desde la HMI

Las páginas HMI de las cámaras de control son **compartidas** entre los dispositivos: desde la sección **Control FlexiBowl®** se selecciona el dispositivo correspondiente.

```{list-table}
:header-rows: 1
:widths: 25 75

* - Página
  - Función
* - **Setup Camera Ctrl**
  - Configuración de la cámara de control.
* - **Setup Tool Ctrl**
  - Configuración de VisionPro: permite intervenir en las herramientas y en el script de VisionPro (véase [Script de VisionPro](35_Script_VisionPro.md)).
* - **View Runtime**
  - Visualización de la imagen y del resultado del control.
* - **Test Tool**
  - Inicia un control local, incluso sin robot conectado.
```

```{note}
Con el comando **Test Tool**, el control se ejecuta incluso **sin robot conectado**: en este caso el resultado se muestra en la HMI pero **no se transmite por TCP**.
```

## Prueba rápida de aceptación

Tras instalar o modificar el script de VisionPro, realice las siguientes comprobaciones:

- ☐ Enviar `start_control_1` y verificar el resultado de texto y la imagen de la PMRedLine 1.
- ☐ Enviar `start_control_2` y verificar el resultado de texto y la imagen de la PMRedLine 2.
- ☐ Enviar `start_control_` y verificar que la cadena contenga ambos resultados.
- ☐ Enviar `start_control_ABC` y verificar el error `INVALID_CONTROL` del script de ejemplo.
- ☐ Ejecutar **Test Tool** con el robot desconectado y verificar que la HMI y VisionPro siguen operativos.

## Más información

- [Comando `start_control_`](34_Comando_start_control.md): formato del comando, parámetros, respuestas y ejemplos de intercambio.
- [Script de VisionPro](35_Script_VisionPro.md): interfaz del script, personalización y código de ejemplo completo.
- [Solución de problemas – Cámaras de control](../TROUBLESHOOTING/26j_Telecamere_Controllo.md): mensajes de error y acciones recomendadas.
- [Protocolo de comunicación Robot-Visión](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md): lista completa de los comandos del robot.
