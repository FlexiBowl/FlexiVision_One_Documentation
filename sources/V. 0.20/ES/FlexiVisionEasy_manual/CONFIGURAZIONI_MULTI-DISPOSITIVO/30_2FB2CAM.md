# **2 FlexiBowl® y 2 Cámaras**

Esta sección describe las configuraciones disponibles cuando se desea operar con **dos FlexiBowl®** y **dos cámaras** gestionados por un único VisionController FlexiVision One.

---

## Vista general de la configuración

En una configuración **2 FlexiBowl® + 2 Cámaras**, el sistema comprende dos estaciones de alimentación y visión independientes, ambas gestionadas por el mismo VisionController. Cada estación se compone de:

* 1 FlexiBowl®
* 1 Cámara con óptica dedicada
* 1 Hopper (opcional, si está presente)

Las dos estaciones se comunican con el VisionController a través de un **Switch de red**.

```{important}
El **Switch** es un componente **obligatorio** en todas las configuraciones multidispositivo. Sin él no es posible conectar simultáneamente varios FlexiBowl® y varias cámaras al VisionController. Para las especificaciones técnicas y los códigos de pedido, consultar la sección [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Esta configuración admite dos variantes operativas, según el número de robots disponibles en la instalación:
| | **Variante A** | **Variante B** |
|---|---|---|
| **Robot** | 1 | 2 |
| **FlexiBowl®** | 2 | 2 |
| **Cámaras** | 2 | 2 |
| **Lógica operativa** | El robot alcanza ambas estaciones | Cada robot está dedicado a una estación |
| **Switch requerido** | Sí | Sí |


---

## Variante A — 1 Robot, 2 FlexiBowl®

![Vista General Sistema 2FB2CAM1Robot](../../../../_shared/media/images/2FB2CAM1R.png)

En esta variante, un **único robot** opera en ambas estaciones. El robot está posicionado de forma que pueda alcanzar el área de picking de cada FlexiBowl®, alternando la recogida entre las dos estaciones según los comandos recibidos.

Cada estación gestiona su propia receta independiente. En cada estación es posible configurar una aplicación de tipo **Estándar** o **Mix**, con modelos de componentes diferentes dentro de la misma receta.

| Parámetro | Valor |
|---|---|
| FlexiBowl® | 2 |
| Cámaras | 2 |
| Robot | 1 |
| Switch requerido | **Sí** |

```{important}
**Receta base y gestión de recetas**

Como en la configuración individual, también en una configuración 2FB + 2CAM el proceso parte de la creación de una **única receta base**, que contiene los setup hardware y la calibración de la cámara para todo el sistema. Esta receta base se **duplica** después para cada estación: cada duplicado constituye la receta operativa de esa estación, dentro de la cual se crean los modelos de las piezas (hasta 8 por estación).

Por este motivo, es fundamental que la asociación entre los dispositivos se configure correctamente desde el principio:

* **Cámara 1** → FlexiBowl® 1 (+ Hopper 1, si está presente)
* **Cámara 2** → FlexiBowl® 2 (+ Hopper 2, si está presente)

Una asociación incorrecta en fase de setup repercutiría en todas las recetas derivadas, comprometiendo el reconocimiento de las piezas y el correcto funcionamiento de todo el sistema.
```
---

## Variante B — 2 Robots, 2 FlexiBowl®

![Vista General Sistema 2FB2CAM2Robot](../../../../_shared/media/images/2FB2CAM2R.png)

En esta variante, cada robot está dedicado a una única estación: el **Robot 1** realiza el picking en el FlexiBowl® 1, el **Robot 2** realiza el picking en el FlexiBowl® 2. Las dos celdas son independientes y no se superponen.

También en esta variante cada estación admite aplicaciones tanto de tipo **Estándar** como **Mix**.

| Parámetro | Valor |
|---|---|
| FlexiBowl® | 2 |
| Cámaras | 2 |
| Robot | 2 |
| Switch requerido | **Sí** |

```{tip}
Esta variante garantiza la máxima productividad, con las dos celdas operando en paralelo y de forma completamente autónoma.
```

```{important}
**Receta base y gestión de recetas**

Como en la configuración individual, también en una configuración 2FB + 2CAM el proceso parte de la creación de una **única receta base**, que contiene los setup hardware y la calibración de la cámara para todo el sistema. Esta receta base se **duplica** después para cada estación: cada duplicado constituye la receta operativa de esa estación, dentro de la cual se crean los modelos de las piezas (hasta 8 por estación).

Por este motivo, es fundamental que la asociación entre los dispositivos se configure correctamente desde el principio:

* **Cámara 1** → FlexiBowl® 1 (+ Hopper 1, si está presente)
* **Cámara 2** → FlexiBowl® 2 (+ Hopper 2, si está presente)

Una asociación incorrecta en fase de setup repercutiría en todas las recetas derivadas, comprometiendo el reconocimiento de las piezas y el correcto funcionamiento de todo el sistema.
```

---

## Componentes necesarios

### Kit base FlexiVision One

El **kit base FlexiVision One** (suministrado con el sistema) ya incluye todo lo necesario para la **primera estación** (cámara, óptica, cables, rejilla de calibración). No es necesario comprar un segundo kit completo para la segunda estación.

### Kit Cámara Adicional

Para la segunda estación basta con comprar el **Kit Cámara Adicional**, disponible en una versión específica para cada tamaño de FlexiBowl®. El kit incluye:

* 1 Cámara
* 1 Óptica dedicada al tamaño FlexiBowl®
* 1 Rejilla de calibración
* 1 Cable alimentación cámara
* 2 Cables Ethernet

Seleccionar el kit en función del tamaño del **segundo** FlexiBowl®:

| Tamaño FlexiBowl® | Código Kit Cámara Adicional | Óptica incluida |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optic |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optic |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optic |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optic |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optic |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optic |
```{note}
Si las dos estaciones utilizan FlexiBowl® de **tamaños diferentes**, el Kit Cámara Adicional debe seleccionarse en función del tamaño del FlexiBowl® de la segunda estación. La primera estación ya está cubierta por el kit base.
```

### Switch

El Switch siempre es necesario en las configuraciones multidispositivo. Para código, especificaciones eléctricas y físicas, consultar la sección dedicada:

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Cableado

El esquema de cableado es idéntico para ambas variantes: todos los dispositivos de campo (FlexiBowl®, cámaras, robots) se conectan al **Switch**, y el Switch se conecta al **VisionController** mediante un único puerto Ethernet. La diferencia entre Variante A y Variante B se refiere exclusivamente al número de robots conectados al Switch.
```{important}
El Switch dispone de **8 puertos Ethernet**. Verificar que el número total de dispositivos que se van a conectar no supere la capacidad disponible, teniendo en cuenta todos los FlexiBowl®, cámaras y robots presentes.
```

### Esquema de conexión

| Dispositivo | Conexión |
|---|---|
| FlexiBowl® 1 | Puerto Ethernet → Switch |
| FlexiBowl® 2 | Puerto Ethernet → Switch |
| Cámara 1 | Cable Ethernet → Switch |
| Cámara 2 | Cable Ethernet → Switch |
| Robot 1 | Puerto Ethernet → Switch |
| Robot 2 *(solo Variante B)* | Puerto Ethernet → Switch |
| **Switch** | **Puerto Ethernet → VisionController** |
```{tip}
Verificar que a cada dispositivo se le asigne una dirección IP única en la misma subnet. Los puertos TCP/IP utilizados por el VisionController para las dos estaciones son configurables: por defecto **FB1 → 4001**, **FB2 → 4002**. Consultar la sección [Protocolo de Comunicación Robot-Visión](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) para los detalles.
```

### Puertos Switch ocupados por variante

| Puerto Switch | Variante A (1 Robot) | Variante B (2 Robots) |
|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | Cámara 1 | Cámara 1 |
| 4 | Cámara 2 | Cámara 2 |
| 5 | Robot 1 | Robot 1 |
| 6 | VisionController | Robot 2 |
| 7 | — | VisionController |
| 8 | — | — |

```{note}
**Cableado de los componentes individuales**

Los procedimientos de conexión física de cada componente (FlexiBowl®, cámara, hopper, robot) se describen íntegramente en la sección [Cableado y Conexiones](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md). En una configuración 2FB + 2CAM, las mismas operaciones simplemente deben ejecutarse **dos veces** — una por cada estación — con la única diferencia de que cada dispositivo se conecta al **Switch** en lugar de directamente al VisionController.
```
```{important}
**Asociación dispositivos en el software**

FlexiVision One puede gestionar simultáneamente todas las estaciones, pero es fundamental que la asociación entre los dispositivos se configure correctamente en el software. Asegurarse de asociar:

* **Cámara 1** → FlexiBowl® 1 (+ Hopper 1, si está presente)
* **Cámara 2** → FlexiBowl® 2 (+ Hopper 2, si está presente)

Una asociación incorrecta comprometería la localización de las piezas y el correcto funcionamiento de todo el sistema.
```

**→ [Configuración Inicial del Sistema](../QUICKSTART/SETUP/13_setup.md)**

