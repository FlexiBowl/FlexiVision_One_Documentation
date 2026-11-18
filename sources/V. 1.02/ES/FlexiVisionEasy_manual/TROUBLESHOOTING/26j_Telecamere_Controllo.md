(troubleshooting_telecamere_controllo)=
# **Cámaras de control**

```{important}
**Función Expert**

La gestión de las cámaras de control (**Control Camera**) es una función **Expert**: requiere conocimientos de Cognex VisionPro y de scripts en C#, y está destinada a usuarios expertos. Para obtener información sobre el modo Expert, consulte [Qué es y cuándo se necesita](../EXPERT/32_Expert.md).
```

```{note}
Esta página se refiere al comando `start_control_` y a los scripts de VisionPro (disponibles a partir de la versión de software v0.24). Para el procedimiento completo, consulte [Cámaras de control](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md) y [Comando `start_control_`](../TELECAMERE_CONTROLLO/34_Comando_start_control.md).
```

## Respuestas y mensajes de error

Los errores relativos al script de control comienzan con `#Error_Control_`. El caso `Not_Found` **no es un error de software**: significa que el locator no ha detectado ningún objeto. Los errores de la cámara pueden comunicarse por separado con el prefijo `#Error_Camera`.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Respuesta
  - Significado / acción recomendada
* - `Not_Found`
  - Inspección completada sin reconocimientos: verificar la pieza, la imagen y el modelo.
* - `#Error_Control_INVALID_CONTROL`
  - El parámetro no está gestionado por el script: verificar el texto tras `start_control_`.
* - `#Error_Control_TOOL_NOT_FOUND`
  - Una de las herramientas esperadas no está presente o tiene un nombre distinto.
* - `#Error_Control_LAST_RECORD_NULL`
  - No está disponible el registro de la última ejecución de la herramienta.
* - `#Error_Control_INPUT_IMAGE_RECORD_NULL`
  - El subregistro `InputImage` no está disponible.
* - `#Error_Control_RECORD_WITHOUT_IMAGE`
  - El registro seleccionado no contiene una imagen válida.
* - `#Error_Control_VISIONPRO_JOB`
  - La ejecución de la tarea de VisionPro ha generado un error.
* - `#Error_Control_EMPTY_OUTPUT`
  - El script no ha devuelto una cadena válida.
* - `#Error_Camera …`
  - Problema de adquisición: comprobar la conexión y el estado de la cámara.
```

```{note}
El script de ejemplo también puede devolver `#Error_Control_TOOL_RUN` cuando los resultados de una herramienta no están disponibles (por ejemplo `#Error_Control_TOOL_RUN;Tool=2` si el error afecta a la herramienta 2). Si al menos una herramienta produce un error de ejecución, el error se escribe al principio de la respuesta.
```

## Comprobaciones rápidas

- Verificar que el comando tenga el **guion bajo final** (`start_control_`) y que el parámetro no contenga espacios.
- Verificar que los nombres de entrada y salida del ToolBlock sigan siendo `Image`, `Input_Control`, `Output_String` y `Output_Image`.
- Verificar que la salida `Output_Image` esté configurada como un `CogRecord` compatible.
- Ejecutar **Test Tool** desde la HMI incluso sin robot conectado para aislar el problema de la comunicación TCP: en este caso el resultado se muestra en la HMI pero no se transmite al robot.
- Tras cada modificación del script, repetir la [prueba rápida de aceptación](../TELECAMERE_CONTROLLO/33_Telecamere_Controllo.md).
