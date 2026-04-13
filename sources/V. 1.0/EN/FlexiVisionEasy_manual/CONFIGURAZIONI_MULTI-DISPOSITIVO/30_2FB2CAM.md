# **2 FlexiBowl® and 2 Cameras**

This section describes the available configurations when operating with **two FlexiBowl® units** and **two cameras** managed by a single FlexiVision One VisionController.

---

## Configuration overview

In a **2 FlexiBowl® + 2 Cameras** configuration, the system includes two independent feeding and vision stations, both managed by the same VisionController. Each station consists of:

* 1 FlexiBowl®
* 1 camera with dedicated optics
* 1 hopper, optional if present

The two stations communicate with the VisionController through a **network switch**.

```{important}
The **switch** is a **mandatory** component in all multi-device configurations. Without it, it is not possible to connect multiple FlexiBowl® units and multiple cameras to the VisionController at the same time. For technical specifications and order codes, refer to [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

This configuration supports two operating variants depending on the number of robots available in the plant:

| | **Variant A** | **Variant B** |
|---|---|---|
| **Robots** | 1 | 2 |
| **FlexiBowl®** | 2 | 2 |
| **Cameras** | 2 | 2 |
| **Operating logic** | One robot reaches both stations | Each robot is dedicated to one station |
| **Switch required** | Yes | Yes |

---

## Variant A - 1 Robot, 2 FlexiBowl®

![2FB2CAM1Robot system overview](../../../../_shared/media/images/2FB2CAM1R.png)

In this variant, a **single robot** operates on both stations. The robot is positioned so it can reach the picking area of each FlexiBowl®, alternating picks between the two stations according to the received commands.

Each station manages its own independent recipe. On each station it is possible to configure either a **Standard** or a **Mix** application, with different part models inside the same recipe.

| Parameter | Value |
|---|---|
| FlexiBowl® | 2 |
| Cameras | 2 |
| Robots | 1 |
| Switch required | **Yes** |

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 2FB + 2CAM setup the process starts from a single **base recipe** containing the hardware setup and the camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Variant B - 2 Robots, 2 FlexiBowl®

![2FB2CAM2Robot system overview](../../../../_shared/media/images/2FB2CAM2R.png)

In this variant, each robot is dedicated to one single station: **Robot 1** performs picking on FlexiBowl® 1, and **Robot 2** performs picking on FlexiBowl® 2. The two cells are independent and do not overlap.

Each station also supports both **Standard** and **Mix** applications in this variant.

| Parameter | Value |
|---|---|
| FlexiBowl® | 2 |
| Cameras | 2 |
| Robots | 2 |
| Switch required | **Yes** |

```{tip}
This variant guarantees maximum productivity, with the two cells operating in parallel and completely independently.
```

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 2FB + 2CAM setup the process starts from a single **base recipe** containing the hardware setup and the camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Required components

### FlexiVision One base kit

The **FlexiVision One base kit**, supplied with the system, already includes everything required for the **first station**, meaning camera, optics, cables, and calibration grid. It is not necessary to purchase a second complete kit for the second station.

### Additional Camera Kit

For the second station, it is sufficient to purchase the **Additional Camera Kit**, available in a specific version for each FlexiBowl® size. The kit includes:

* 1 camera
* 1 optic dedicated to the FlexiBowl® size
* 1 calibration grid
* 1 camera power cable
* 2 Ethernet cables

Select the kit according to the size of the **second** FlexiBowl®:

| FlexiBowl® size | Additional Camera Kit code | Included optic |
|---|---|---|
| FB 200 | GM002002 | CE000881 - FlexiVision One 35 mm optic |
| FB 350 | GM002003 | CE000881 - FlexiVision One 35 mm optic |
| FB 500 | GM002004 | CE000880 - FlexiVision One 25 mm optic |
| FB 650 | GM002005 | CE000879 - FlexiVision One 16 mm optic |
| FB 800 | GM002006 | CE000879 - FlexiVision One 16 mm optic |
| FB 1200 | GM002007 | CE000878 - FlexiVision One 12 mm optic |

```{note}
If the two stations use FlexiBowl® units of **different sizes**, the Additional Camera Kit must be selected according to the size of the FlexiBowl® used on the second station. The first station is already covered by the base kit.
```

### Switch

The switch is always required in multi-device configurations. For code, electrical specifications, and physical specifications, refer to:

**-> [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Wiring

The wiring diagram is identical for both variants: all field devices, meaning FlexiBowl® units, cameras, and robots, are connected to the **switch**, and the switch is connected to the **VisionController** through a single Ethernet port. The only difference between Variant A and Variant B is the number of robots connected to the switch.

```{important}
The switch provides **8 Ethernet ports**. Verify that the total number of devices to be connected does not exceed the available capacity, taking into account all FlexiBowl® units, cameras, and robots present.
```

### Connection scheme

| Device | Connection |
|---|---|
| FlexiBowl® 1 | Ethernet port -> switch |
| FlexiBowl® 2 | Ethernet port -> switch |
| Camera 1 | Ethernet cable -> switch |
| Camera 2 | Ethernet cable -> switch |
| Robot 1 | Ethernet port -> switch |
| Robot 2 *(Variant B only)* | Ethernet port -> switch |
| **Switch** | **Ethernet port -> VisionController** |

```{tip}
Verify that each device is assigned a unique IP address within the same subnet. The TCP/IP ports used by the VisionController for the two stations are configurable. By default, **FB1 -> 4001** and **FB2 -> 4002**. Refer to [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) for details.
```

### Switch ports used by variant

| Switch port | Variant A, 1 Robot | Variant B, 2 Robots |
|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | Camera 1 | Camera 1 |
| 4 | Camera 2 | Camera 2 |
| 5 | Robot 1 | Robot 1 |
| 6 | VisionController | Robot 2 |
| 7 | — | VisionController |
| 8 | — | — |

```{note}
**Wiring of the individual components**

The physical connection procedures for each component, meaning FlexiBowl®, camera, hopper, and robot, are fully described in [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md). In a 2FB + 2CAM configuration, the same operations simply need to be performed **twice**, once for each station, with the only difference that each device connects to the **switch** instead of directly to the VisionController.
```

```{important}
**Device association in the software**

FlexiVision One is able to manage all stations simultaneously, but it is essential that the association between devices is configured correctly in the software. Make sure to associate:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present

An incorrect association would compromise part localization and the correct operation of the whole system.
```

**-> [Initial System Configuration](../QUICKSTART/SETUP/13_setup.md)**
