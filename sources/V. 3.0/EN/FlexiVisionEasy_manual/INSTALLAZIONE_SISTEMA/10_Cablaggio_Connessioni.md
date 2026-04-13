(cablaggio)=
# **Wiring and Connections**
Overview image of the electrical connections:

![Connection overview](../../../../_shared/media/images/panoramicacollegamenti.png)

```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **From**
  - **To**
  - **Connection**

* - Power mains
  - FlexiBowl
  - 110/220 Vdc power supply

* - Power mains
  - Robot
  - Power supply according to the specifications of your robot

* - Power mains
  - Camera
  - 24 Vdc power supply

* - Power mains
  - Illuminator (light)
  - 24 Vdc power supply

* - Power mains
  - Hopper Controller
  - 110/220 Vdc power supply

* - Hopper Controller
  - Hopper
  - Power and signal

* - Robot
  - Hopper Controller
  - Digital I/O

* - VisionController
  - Camera
  - TCP Ethernet

* - VisionController
  - FlexiBowl
  - TCP Ethernet

* - VisionController
  - Robot
  - TCP Ethernet
```

## Guided wiring procedure

```{list-table}
:header-rows: 1

* - **Step**
  - **Action**
* - 1
  - Connect the FlexiBowl® power supply.  
    [🔗 Refer to the dedicated manual for the power specifications](http://link-al-manuale.com)
* - 2
  - Connect the [24 V Hirose power cable](cavo) to the camera.
* - 3
  - Connect the FlexiBowl® to the VisionController using an Ethernet cable.
* - 4
  - Connect the camera to the VisionController (PC) using an Ethernet cable.
* - 5
  - Connect the robot to the VisionController using an Ethernet cable.
* - 6
  - Connect the compressed air supply to the FlexiBowl®.  
    [🔗 Refer to the dedicated manual for the pneumatic specifications](http://link-al-manuale.com)
* - 7
  - If present, connect the hopper to its controller.
* - 8
  - If present, connect the robot to the hopper controller through digital I/O.
* - 9
  - If present, power the hopper controller (110/220 V depending on the option selected when purchasing the hopper vibrating base).
* - 10
  - Turn on the FlexiBowl® AC switch, position `"I"`. The READY LED must be **ON**.
* - 11
  - Turn on all the other devices.
```

(cablaggio_illuminatore)=
## Illuminator wiring

![TopLight pinout](../../../../_shared/media/images/pin_toplight.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Requirement / Action
* - **Voltage**
  - 24 V DC (+/-10%). Minimum operating voltage: 20 V DC at the light input.
* - **Connector**
  - M12 male.
    :::{note}
      To connect the TopLight, you can also purchase its dedicated [power cable](cavoalimtoplight).
    :::
* - **Connector pinout**
  - Pin 1: +24V (brown) - Pin 3: GND (blue) - Pin 4: STROBE PNP (black)
* - **STROBE mode (PNP)**
  - From 5 V to 24 V for 100% ON. From 0 V to 1 V for 100% OFF.
* - **CONTINUOUS mode**
  - Pin 1 (+24V) and Pin 3 (GND) connected; Pin 4 (PNP) connected to Pin 1.
* - **Voltage drop (10 m M12 cable)**
  - 1.15 V @ 5 A - 2.3 V @ 10 A - 3.5 V @ 15 A - 4.6 V @ 20 A (max 20 A)
* - **Shielding**
  - Use shielded cables to reduce electromagnetic interference (EMI).
```

```{warning}
**Electrical safety**

- Follow the specified supply voltages and connection terminals.
- Do not modify or disassemble the product.
- Do not connect or clean the device while it is powered.
- Do not look directly at the light source.
```
