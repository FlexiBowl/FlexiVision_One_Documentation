# **Monitorización de la Cinta: Check Belt**

Esta sección describe el procedimiento para verificar el estado de desgaste y limpieza de la cinta del FlexiBowl® mediante la función **Belt Check**.

**¿Qué es el Belt Check?**
El **Belt Check** es una herramienta que compara la imagen actual de la cinta con una imagen de referencia de la cinta limpia (**Clean Reference**), calculando un índice de similitud. Esto permite monitorizar a lo largo del tiempo el nivel de suciedad o desgaste de la cinta, detectando a tiempo la necesidad de mantenimiento.

:::{note}
**Requisitos previos**

Antes de continuar, asegúrese de que:

- El FlexiBowl® esté conectado y configurado ([FlexiBowl® Setup](../QUICKSTART/SETUP/13a_FB_Setup.md))
- La cinta sea visible y esté correctamente iluminada
:::

---

## Acceso a la página Check Belt

| **1** | Desde la página principal del software, hacer clic en **Setup** |
| ----- | ------------------------------------------------------------ |
| **2** | En la página SETUP, localizar y hacer clic en el icono **Check Belt** |
| **3** | Se abre la página de control de la cinta, con un bloque para cada FlexiBowl® gestionado por el sistema |

---

## Descripción general de la interfaz Check Belt

:::{image} ../../../_shared/media/images/beltcheck.png
:width: 100%
:align: center
:::

La página se divide en un bloque para cada FlexiBowl® conectado, cada uno compuesto por dos secciones:

| Elemento | Descripción |
| --- | --- |
| **Flb X Connected** | Indicador de estado de conexión del FlexiBowl® correspondiente (🟢 Verde = conectado, 🔴 Rojo = no conectado) |
| **Save Clean Reference** | Captura y guarda la imagen actual de la cinta como referencia "limpia", para usarla como término de comparación en los controles posteriores |
| **Delete Clean Reference** | Elimina la imagen de referencia guardada anteriormente, para poder capturar una nueva |
| **Vista previa de cámara (antes/después)** | Las dos miniaturas muestran, respectivamente, la imagen de referencia guardada y la imagen actual de la cinta en el momento de la prueba |
| **Run Belt Check** | Inicia la comparación entre la imagen de referencia y la actual, calculando el estado de la cinta |
| **Belt Health Result** | Panel con el resultado de la comparación: barra graduada Clean → Dirty, indicador de color, estado textual y fecha del último control |

---

## Procedimiento

### Paso 1: Captura de la referencia limpia

:::{important}
Realizar este paso **solo con la cinta realmente limpia**. La precisión de todos los controles futuros depende de la calidad de esta imagen de referencia.
:::

| **1** | Asegurarse de que la cinta esté limpia y libre de componentes o residuos en el área encuadrada |
| **2** | Hacer clic en **Save Clean Reference** |
| **3** | La imagen se captura y se guarda como referencia; aparecerá en la miniatura de la izquierda |

:::{tip}
Si la cinta se sustituye o se limpia a fondo, repetir este paso para actualizar la referencia.
:::

### Paso 2: Ejecución del Belt Check

| **4** | Hacer clic en **Run Belt Check** |
| **5** | El sistema captura la imagen actual de la cinta (visible en la miniatura de la derecha) y la compara con la referencia guardada |
| **6** | El resultado se muestra en el panel **Belt Health Result** |

---

## Interpretación de los resultados

El panel **Belt Health Result** muestra:

| Elemento | Significado |
| --- | --- |
| **Barra graduada** | Representación visual de la posición del valor medido entre los dos extremos Clean (limpio) y Dirty (sucio) |
| **Indicador de color y texto** | Estado sintético de la cinta: |

| Color | Texto | Significado |
| --- | --- | --- |
| 🟢 Verde | **Good** | Cinta en buenas condiciones |
| 🟡 Amarillo | **Warning** | Cinta a monitorizar, posible necesidad de limpieza próximamente |
| 🔴 Rojo | **Poor** | Cinta sucia o desgastada, se recomienda intervención de limpieza/mantenimiento |



:::{note}
*Por confirmar*: los umbrales porcentuales exactos que determinan el paso de Good a Warning a Poor.
:::

---