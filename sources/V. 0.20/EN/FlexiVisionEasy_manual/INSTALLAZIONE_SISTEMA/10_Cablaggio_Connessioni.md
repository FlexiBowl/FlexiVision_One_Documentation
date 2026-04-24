(cablaggio)=
# **Wiring and Connections**
overview image of electrical connections 
type:  
![Pan Coll](../../../../_shared/media/images/panoramicacollegamenti.png)
```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **From**
  - **To**
  - **Connection**

* - Electrical network
  - FlexiBowl
  - 110/220 Vdc power supply

* - Electrical network
  - Robot
  - Power supply according to the specifications of your robot

* - Electrical network
  - Camera
  - 24 Vdc power supply

* - Electrical network
  - Illuminator (light)
  - 24 Vdc power supply

* - Electrical network
  - Hopper Controller
  - 110/220 Vdc power supply

* - Hopper Controller
  - Hopper
  - Power supply and signal

* - Robot
  - Hopper Controller
  - Digital I/O

* - VisionController
  - Camera
  - Ethernet TCP

* - VisionController
  - FlexiBowl
  - Ethernet TCP

* - VisionController
  - Robot
  - Ethernet TCP
```

## Guided wiring procedure

```{list-table} 
:header-rows: 1

* - **Step**
  - **Action**
* - 1
  - Connect the FlexiBowl® power supply.  
    [🔗 Refer to the manual for power supply specifications](http://link-al-manuale.com)
* - 2
  - Connect the [Hirose 24V power cable](cavo) to the Camera.
* - 3
  - Connect the FlexiBowl® to the VisionController with an Ethernet cable.
* - 4
  - Connect the Camera to the VisionController (PC) with an Ethernet cable.
* - 5
  - Connect the Robot to the VisionController with an Ethernet cable.
* - 6
  - Connect compressed air to the FlexiBowl®.  
    [🔗 Refer to the manual for pneumatic specifications](http://link-al-manuale.com)
* - 7
  - If present, connect the hopper to its controller
* - 8
  - If present, connect the robot to the hopper controller (Digital I/O)
* - 9 
  - If present, power the hopper controller (110/220 V according to the option selected when purchasing the hopper vibrating base)
* - 10
  - Turn on the FlexiBowl® AC switch (position "I"). The READY LED is **ON**.
* - 11
  - Turn on all other devices
```
(cablaggio_illuminatore)=
## Illuminator wiring

![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parameter
  - Requirement / Action
* - **Voltage**
  - 24V DC (±10%). Minimum operating voltage: 20V DC at the light input.
* - **Connector**
  - M12 Male. 
    :::{note}
      To connect the toplight, its [power cable](cavoalimtoplight) can also be purchased. 
    :::
* - **Connector pinout**
  - Pin 1: +24V (brown) — Pin 3: GND (blue) — Pin 4: STROBE PNP (black)
* - **STROBE mode (PNP)**
  - From 5V to 24V for 100% ON. From 0V to 1V for 100% OFF.
* - **CONTINUOUS mode**
  - Pin 1 (+24V) and Pin 3 (GND) connected; Pin 4 (PNP) connected to Pin 1.
* - **Voltage drop (M12 cable, 10m)**
  - 1.15V @ 5A — 2.3V @ 10A — 3.5V @ 15A — 4.6V @ 20A (max 20A)
* - **Shielding**
  - Use shielded cables to reduce electromagnetic interference (EMI).
```
```{warning}
**Electrical safety**

- Respect the indicated supply voltages and connection terminals.
- Do not modify or disassemble the product.
- Do not connect or clean the device when it is energized.
- Do not look directly at the light source.
```



