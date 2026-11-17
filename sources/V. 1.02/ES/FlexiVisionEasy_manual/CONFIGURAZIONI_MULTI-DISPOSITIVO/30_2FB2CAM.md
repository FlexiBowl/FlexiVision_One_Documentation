# **2 FlexiBowl® y 2 Cámaras**

Esta sección describe las configuraciones disponibles cuando se desea operar con **dos FlexiBowl®** y **dos cámaras** gestionadas por un único VisionController FlexiVision One.

---

## Resumen de la configuración

En una configuración **2 FlexiBowl® + 2 Cámaras**, el sistema consta de dos estaciones independientes de alimentación y visión, ambas controladas por el mismo VisionController. Cada estación consta de:

* 1 FlexiBowl®
* 1 Cámara con óptica dedicada
* 1 Tolva (opcional, si existe)

Las dos estaciones se comunican con el VisionController a través de un **Switch de red**.

```{important}
El **Switch** es un componente **obligatorio** en todas las configuraciones multidispositivo. Sin él no es posible conectar simultáneamente varios FlexiBowl® y varias cámaras al VisionController. Para las especificaciones técnicas y los códigos de pedido, consulte la sección [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

Esta configuración admite dos variantes de funcionamiento, en función del número de robots disponibles en la planta:
| | **Variante A** | **Variante B** |
|---|---|---|
| **Robot** | 1 | 2 |
| **FlexiBowl®** | 2 | 2 |
| **Cámaras** | 2 | 2 |
| **Lógica de funcionamiento** | El robot llega a las dos estaciones | Cada robot está dedicado a una estación |
| **Switch requerido** | Sí | Sí |


---

## Variante A - 1 Robot, 2 FlexiBowls

![Visión general del sistema 2FB2CAM1Robot](../../../../_shared/media/images/2FB2CAM1R.png)

En esta variante, un **solo robot** opera en ambas estaciones. El robot se posiciona de forma que pueda alcanzar la zona de picking de cada FlexiBowl®, alternando el picking entre las dos estaciones en función de las órdenes recibidas.

Cada estación ejecuta su propia receta independiente. En cada estación puede configurarse una aplicación de tipo **Standard** o **Mix**, con diferentes modelos de componentes dentro de la misma receta.

| Parámetro | Valor |
|---|---|
| FlexiBowl® | 2 |
| Cámaras | 2 |
| Robot | 1 |
| Switch requerido | **Sí** |

```{important}
**Receta básica y gestión de recetas**

Al igual que en la configuración simple, en una configuración 2FB + 2CAM el proceso comienza con la creación de una **única receta básica**, que contiene la configuración del hardware y la calibración de la cámara para todo el sistema. A continuación, esta receta de base se duplica para cada estación: cada duplicado constituye la receta de funcionamiento de dicha estación, dentro de la cual se crean los modelos de piezas (hasta 8 por estación).

Por lo tanto, es crucial que la asociación entre los dispositivos se configure correctamente desde el principio:

* **Cámara 1** → FlexiBowl® 1 (+ Tolva 1, si existe)
* **Cámara 2** → FlexiBowl® 2 (+ Tolva 2, si existe)

Una asociación incorrecta durante la configuración afectaría a todas las recetas derivadas, comprometiendo el reconocimiento de las piezas y el correcto funcionamiento de todo el sistema.
```
---

## Variante B - 2 Robots, 2 FlexiBowl®

![Visión general del sistema 2FB2CAM2Robot](../../../../_shared/media/images/2FB2CAM2R.png)

En esta variante, cada robot se dedica a una única estación: el **Robot 1** recoge en el FlexiBowl® 1, el **Robot 2** recoge en el FlexiBowl® 2. Las dos células son independientes y no se solapan.

También en esta variante, cada estación admite aplicaciones tanto de tipo **Standard** como **Mix**.

| Parámetro | Valor |
|---|---|
| FlexiBowl® | 2 |
| Cámaras | 2 |
| Robot | 2 |
| Switch requerido | **Sí** |

```{tip}
Esta variante garantiza la máxima productividad, con las dos células operando en paralelo y de forma completamente autónoma.
```

```{important}
**Receta básica y gestión de recetas**

Al igual que en la configuración simple, en una configuración 2FB + 2CAM el proceso comienza con la creación de una **única receta básica**, que contiene la configuración del hardware y la calibración de la cámara para todo el sistema. A continuación, esta receta de base se duplica para cada estación: cada duplicado constituye la receta de funcionamiento de dicha estación, dentro de la cual se crean los modelos de piezas (hasta 8 por estación).

Por lo tanto, es crucial que la asociación entre los dispositivos se configure correctamente desde el principio:

* **Cámara 1** → FlexiBowl® 1 (+ Tolva 1, si existe)
* **Cámara 2** → FlexiBowl® 2 (+ Tolva 2, si existe)

Una asociación incorrecta durante la configuración afectaría a todas las recetas derivadas, comprometiendo el reconocimiento de las piezas y el correcto funcionamiento de todo el sistema.
```

---

## Componentes necesarios

### *Kit básico FlexiVision One*

El **kit básico FlexiVision One** (suministrado con el sistema) ya incluye todo lo necesario para la **primera estación** (cámara, óptica, cables, rejilla de calibración). No es necesario adquirir un segundo kit completo para la segunda estación.

### *Kit de cámara adicional*

Para la segunda estación, sólo tiene que adquirir el **Kit de cámara adicional**, que está disponible en una versión específica para cada tamaño de FlexiBowl®. El kit incluye:

* 1 Cámara
* 1 Óptica dedicada al tamaño FlexiBowl®
* 1 Rejilla de calibración
* 1 Cable de alimentación de la cámara
* 2 Cables Ethernet

Seleccione el kit en función del tamaño del **segundo** FlexiBowl®:

| Tamaño FlexiBowl® | Código Kit Cámara Adicional | Óptica incluida |
|---|---|---|
| FB 200 | GM002002 | CE000881 — FlexiVision One 35mm Optic |
| FB 350 | GM002003 | CE000881 — FlexiVision One 35mm Optic |
| FB 500 | GM002004 | CE000880 — FlexiVision One 25mm Optic |
| FB 650 | GM002005 | CE000879 — FlexiVision One 16mm Optic |
| FB 800 | GM002006 | CE000879 — FlexiVision One 16mm Optic |
| FB 1200 | GM002007 | CE000878 — FlexiVision One 12mm Optic |
```{note}
Si las dos estaciones utilizan FlexiBowl® de **tamaños diferentes**, el Kit de Cámara Adicional debe seleccionarse en función del tamaño del FlexiBowl® de la segunda estación. La primera estación ya está cubierta por el kit básico.
```

### *Switch*

El Switch siempre es necesario en las configuraciones multidispositivo. Para las especificaciones de código, eléctricas y físicas, consulte la sección dedicada:

**→ [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Cableado

El diagrama de cableado es idéntico para ambas variantes: todos los dispositivos de campo (FlexiBowl®, cámaras, robots) se conectan al **Switch**, y el Switch se conecta al **VisionController** a través de un único puerto Ethernet. La diferencia entre la Variante A y la Variante B sólo afecta al número de robots conectados al Switch.
```{important}
El Switch dispone de **8 puertos Ethernet**. Compruebe que el número total de dispositivos a conectar no supera la capacidad disponible, teniendo en cuenta todos los FlexiBowl®, cámaras y robots presentes.
```

### *Diagrama de conexión*

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
Asegúrese de que cada dispositivo tiene asignada una dirección IP única en la misma subred. Los puertos TCP/IP utilizados por el VisionController para las dos estaciones son configurables: por defecto **FB1 → 4001**, **FB2 → 4002**. Consulte la sección [Protocolo de comunicación Robot-Vision](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) para obtener más detalles.
```

### *Puertos Switch ocupados por variante*

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

Los procedimientos de conexión física de cada componente (FlexiBowl®, cámara, tolva, robot) se describen detalladamente en la sección [Cableado y conexiones](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md). En una configuración 2FB + 2CAM, simplemente hay que realizar las mismas operaciones **dos veces** — una para cada estación — con la única diferencia de que cada dispositivo se conecta al **Switch** en lugar de directamente al VisionController.
```
```{important}
**Asociación de dispositivos en el software**

FlexiVision One puede gestionar todas las estaciones simultáneamente, pero es esencial que la asociación entre los dispositivos esté configurada correctamente en el software. Asegúrese de asociar:

* **Cámara 1** → FlexiBowl® 1 (+ Tolva 1, si existe)
* **Cámara 2** → FlexiBowl® 2 (+ Tolva 2, si existe)

Una asociación incorrecta comprometería la localización de las piezas y el buen funcionamiento de todo el sistema.
```

**→ [Configuración inicial del sistema](../QUICKSTART/SETUP/13_setup.md)**

