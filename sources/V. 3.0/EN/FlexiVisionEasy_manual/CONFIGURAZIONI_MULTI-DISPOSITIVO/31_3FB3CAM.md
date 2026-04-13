# **3 FlexiBowl® and 3 Cameras**

This section describes the available configurations when operating with **three FlexiBowl® units** and **three cameras** inside the same picking cell, managed by a single FlexiVision One VisionController.

---

## Configuration overview

In a **3 FlexiBowl® + 3 Cameras** configuration, the system includes three independent feeding and vision stations, all managed by the same VisionController. Each station consists of:

* 1 FlexiBowl®
* 1 camera with dedicated optics
* 1 hopper, optional if present

The three stations communicate with the VisionController through a **network switch**.

```{important}
The **switch** is a **mandatory** component in all multi-device configurations. Without it, it is not possible to connect multiple FlexiBowl® units and multiple cameras to the VisionController at the same time. For technical specifications and order codes, refer to [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

This configuration supports three operating variants depending on the number of robots available in the plant:

| | **Variant A** | **Variant B** | **Variant C** |
|---|---|---|---|
| **Robots** | 1 | 2 | 3 |
| **FlexiBowl®** | 3 | 3 | 3 |
| **Cameras** | 3 | 3 | 3 |
| **Operating logic** | The robot reaches all three stations | First robot works on one FlexiBowl, second robot works on two FlexiBowl units | Each robot is dedicated to one station |
| **Switch required** | Yes | Yes | Yes |

---

## Variant A - 1 Robot, 3 FlexiBowl®

![3FB3CAM1Robot system overview](../../../../_shared/media/images/3FB3CAM1R.png)

A **single robot** operates on all three stations. The robot must be positioned so that it can reach the picking area of each FlexiBowl®. The VisionController manages the three stations independently, each with its own recipe and TCP/IP communication channel.

Each station supports both **Standard** and **Mix** applications.

| Parameter | Value |
|---|---|
| FlexiBowl® | 3 |
| Cameras | 3 |
| Robots | 1 |
| Switch required | **Yes** |

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 3FB + 3CAM setup the process starts from a single **base recipe** containing the hardware setup and camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Variant B - 2 Robots, 3 FlexiBowl®

![3FB3CAM2Robot system overview](../../../../_shared/media/images/3FB3CAM2R.png)

In this variant, **two robots** share the three stations. The first robot performs picking on one FlexiBowl, while the second robot works on the other two FlexiBowl units. The workload distribution between the robots is defined by the robot program logic and the physical plant layout.

Each station supports both **Standard** and **Mix** applications.

| Parameter | Value |
|---|---|
| FlexiBowl® | 3 |
| Cameras | 3 |
| Robots | 2 |
| Switch required | **Yes** |

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 3FB + 3CAM setup the process starts from a single **base recipe** containing the hardware setup and camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Variant C - 3 Robots, 3 FlexiBowl®

![3FB3CAM3Robot system overview](../../../../_shared/media/images/3FB3CAM3R.png)

Each robot is dedicated to one single station, providing maximum productivity, with the three cells operating in parallel and completely independently.

Each station supports both **Standard** and **Mix** applications.

| Parameter | Value |
|---|---|
| FlexiBowl® | 3 |
| Cameras | 3 |
| Robots | 3 |
| Switch required | **Yes** |

```{tip}
Variant C guarantees the best overall performance. Each cell is completely autonomous and does not depend on the availability of the others.
```

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 3FB + 3CAM setup the process starts from a single **base recipe** containing the hardware setup and camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Required components

### FlexiVision One base kit

The **FlexiVision One base kit**, supplied with the system, already includes everything required for the **first station**, including the VisionController, camera, optics, cables, and calibration grid. It is not necessary to purchase a second complete kit for the additional stations.

### Additional Camera Kit, quantity 2

For stations 2 and 3 it is necessary to purchase **two Additional Camera Kits**, one for each station, selecting the code corresponding to the FlexiBowl® size of each station. The kit includes:

* 1 camera
* 1 optic dedicated to the FlexiBowl® size
* 1 calibration grid
* 1 camera power cable
* 2 Ethernet cables

Select the kit according to the FlexiBowl® size of each additional station:

| FlexiBowl® size | Additional Camera Kit code | Included optic |
|---|---|---|
| FB 200 | GM002002 | CE000881 - FlexiVision One 35 mm optic |
| FB 350 | GM002003 | CE000881 - FlexiVision One 35 mm optic |
| FB 500 | GM002004 | CE000880 - FlexiVision One 25 mm optic |
| FB 650 | GM002005 | CE000879 - FlexiVision One 16 mm optic |
| FB 800 | GM002006 | CE000879 - FlexiVision One 16 mm optic |
| FB 1200 | GM002007 | CE000878 - FlexiVision One 12 mm optic |

```{note}
If the additional stations use FlexiBowl® units of different sizes, purchase one kit for each required size.  
For example, with a configuration FB500 + FB650 + FB800, the base kit covers the first station, while the second and third stations require GM002005 and GM002006 respectively, according to the size installed on those stations.
```

### Switch

The switch is always required in multi-device configurations. For code, electrical specifications, and physical specifications, refer to:

**-> [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Wiring

In **Variant A**, meaning 1 robot, all field devices, meaning FlexiBowl® units, cameras, and robot, connect to the **switch**, and the switch connects to the **VisionController** through a single Ethernet port. The total number of connections fits within the 8 available switch ports.

From **Variant B** onward, the total number of devices exceeds the ports available on the switch.  
In these cases, one VisionController port is used to connect it to the switch, while the remaining free VisionController ports are used for the devices that cannot fit on the switch:

- In **Variant B**, 2 robots, **FlexiBowl® 3** connects directly to a free VisionController port
- In **Variant C**, 3 robots, **FlexiBowl® 3** and **Camera 3** connect directly to the free VisionController ports

```{important}
The switch provides **8 Ethernet ports**. Starting from Variant B, it is no longer possible to connect all devices only through the switch. The extra devices must be connected directly to the free Ethernet ports on the VisionController, as indicated in the tables below.
```

:::{note}
You may choose arbitrarily which devices connect directly to the VisionController. The important point is to always keep one free port available for the connection between VisionController and switch.
:::

### Connection scheme

| Device | Variant A, 1 Robot | Variant B, 2 Robots | Variant C, 3 Robots |
|---|---|---|---|
| FlexiBowl® 1 | -> Switch | -> Switch | -> Switch |
| FlexiBowl® 2 | -> Switch | -> Switch | -> Switch |
| FlexiBowl® 3 | -> Switch | **-> VisionController, free port** | **-> VisionController, free port** |
| Camera 1 | -> Switch | -> Switch | -> Switch |
| Camera 2 | -> Switch | -> Switch | -> Switch |
| Camera 3 | -> Switch | -> Switch | **-> VisionController, free port** |
| Robot 1 | -> Switch | -> Switch | -> Switch |
| Robot 2 | — | -> Switch | -> Switch |
| Robot 3 | — | — | -> Switch |
| **Switch** | **-> VisionController** | **-> VisionController** | **-> VisionController** |

:::{note}
You may choose arbitrarily which devices connect directly to the VisionController. The important point is to always keep one free port available for the connection between VisionController and switch.
:::

```{tip}
Verify that each device is assigned a unique IP address in the same subnet.  
The TCP/IP ports used by the VisionController for the three stations are configurable. By default they are **FB1 -> 4001**, **FB2 -> 4002**, and **FB3 -> 4003**. Refer to [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) for details.
```

### Switch ports used by variant

| Switch port | Variant A, 1 Robot | Variant B, 2 Robots | Variant C, 3 Robots |
|---|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | FlexiBowl® 3 | Camera 1 | Camera 1 |
| 4 | Camera 1 | Camera 2 | Camera 2 |
| 5 | Camera 2 | Camera 3 | Robot 1 |
| 6 | Camera 3 | Robot 1 | Robot 2 |
| 7 | Robot 1 | Robot 2 | Robot 3 |
| 8 | VisionController | VisionController | VisionController |

### VisionController ports used by variant

| VisionController port | Variant A, 1 Robot | Variant B, 2 Robots | Variant C, 3 Robots |
|---|---|---|---|
| 1 | Switch | Switch | Switch |
| 2 | — | FlexiBowl® 3 | FlexiBowl® 3 |
| 3 | — | — | Camera 3 |

:::{note}
You may choose arbitrarily which devices connect directly to the VisionController. The important point is to always keep one free port available for the connection between VisionController and switch.
:::

```{note}
In **Variant B**, the switch ports are all occupied, meaning 7 field devices plus the VisionController, so **FlexiBowl® 3** connects directly to the VisionController. In **Variant C**, **Camera 3** also connects directly to the VisionController, occupying the third available port.
```

```{note}
**Wiring of the individual components**

The physical connection procedures for each component, meaning FlexiBowl®, camera, hopper, and robot, are fully described in [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md).  
In a 3FB + 3CAM configuration, the same operations simply need to be performed **three times**, once for each station, with the only difference that each device connects to the **switch** instead of directly to the VisionController, except for **FlexiBowl® 3** in Variant B and Variant C, and **Camera 3** in Variant C, which connect directly to the free Ethernet ports on the VisionController.
```

```{important}
**Device association in the software**

FlexiVision One is able to manage all stations simultaneously, but it is essential that the association between devices is configured correctly in the software. Make sure to associate:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association would compromise part localization and the correct operation of the whole system.
```

**-> [Initial System Configuration](../QUICKSTART/SETUP/13_setup.md)**
