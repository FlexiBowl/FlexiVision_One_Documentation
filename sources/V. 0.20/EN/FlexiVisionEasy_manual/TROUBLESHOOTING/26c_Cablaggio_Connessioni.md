# **Wiring and Connections**

(troubleshooting_alimentazione)=
## FlexiBowl power supply issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **READY LED does not turn on**
  - • Power supply not connected correctly

    • AC switch in position `"O"` instead of `"I"`

    • Damaged power cable

    • Fuses inside the front panel are blown
  - • Verify the power connection according to the FlexiBowl manual

    • Move the switch to position `"I"`, ON

    • Inspect the cable for damage and replace it if necessary

    • Contact technical support for fuse replacement
* - **FlexiBowl turns off randomly**
  - • Loose power connection

    • Electrical interference

  - • Tighten the power connections

    • Connect the system to a dedicated line with EMI filtering
```

(troubleshooting_ethernet)=
## Ethernet connection issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **FlexiBowl does not communicate with the VisionController**
  - • FlexiBowl powered off, READY LED off  
    • Ethernet cable not connected correctly to the FlexiBowl and or VisionController  
    • Damaged Ethernet cable  
    • Incorrect IP address  
    • FlexiBowl and VisionController on different subnets  
    • Firewall blocking communication  
    • Faulty Ethernet port on the VisionController  
  - • Verify that the READY LED is on  
    • Check the physical cable connection on both ends  
    • Test the cable with a cable tester or replace it  
    • Verify IP configuration in [FlexiBowl Setup](../QUICKSTART/SETUP/13a_FB_Setup.md)  
    • Configure FlexiBowl and VisionController on the same network, for example `192.168.1.x`  
    • Temporarily disable the firewall for testing  
    • Try another Ethernet port on the VisionController  
* - **Intermittent connection**
  - • Cable too long, more than 100 m

    • Damaged or poorly crimped RJ45 connector

    • Electromagnetic interference
  - • Reduce cable length below 100 m or use an intermediate switch

    • Replace the connectors or the full cable

    • Use shielded cable, STP, routed away from EMI sources
```

(troubleshooting_pneumatica)=
## Pneumatic issues, compressed air

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Flip does not work or the impulse is very weak**
  - • Compressed air not connected  
    • Damaged or obstructed pneumatic tube  
    • Pressure regulator closed or set to minimum  
    • Insufficient pressure, below 5 bar  
    • Leaks in the pneumatic circuit
  - • Connect compressed air to the FlexiBowl connection, see manual

    • Check the tube for bends or obstructions and replace it if necessary

    • Open the pressure regulator on the control panel

    • Increase pressure to 5-6 bar

    • Inspect fittings with soapy water and tighten or replace them
* - **Air-blow does not work**
  - • FlexiBowl not equipped with the Air-Blow option

    • Air diverters not supplied externally

    • Flow regulators closed

    • Insufficient air pressure

    • Faulty solenoid valve
  - • Verify that the ordered FlexiBowl has the Blow Test option set to True in the production sheet

    • Verify that external pneumatic supply is present, supplied tube connected

    • If multiple air diverters are present, verify that the flow regulator on the side of the FlexiBowl is set above zero

    • Check air pressure, 5-6 bar

    • Follow the dedicated [instructions]()
```

(troubleshooting_connessione_camera)=
## Camera connection issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Camera not detected by the VisionController**
  - • Camera Ethernet cable not connected

    • Camera connected to a non-PoE port on the VisionController

    • Camera IP address conflicts with other devices on the same subnet

    • Faulty PoE port on the VisionController
  - • Verify the physical camera cable connection

    • Connect the camera only to a PoE port on the VisionController

    • Reset the camera IP or configure a unique static IP

    • Try another PoE port on the VisionController
* - **Camera image black or missing**
  - • Illuminator off
    • Camera exposure too low
    • Lens protective cap not removed
    • Lens not installed
    • Camera not powered, PoE inactive
    • Faulty camera
  - • Verify that the illuminator is on
    • Increase exposure in [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)
    • Remove the lens protective cap
    • Install the correct focal length lens
    • Verify that the camera LED is on, PoE active
    • Replace the camera

* - **Camera disconnects randomly**
  - • Insufficient PoE power, below camera requirement

    • Damaged cable

    • Camera overheating

    • Faulty PoE port
  - • Verify available PoE power
    • Replace the Ethernet cable
    • Improve ventilation around the camera
    • Replace the PoE switch or VisionController port
```

(troubleshooting_connessione_toplight)=
## TopLight connection issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **TopLight does not turn on**
  - • 24 V DC power supply not connected

    • Damaged power cable

    • Wrong voltage, not 24 V

    • Faulty TopLight

    • Tripped fuse or protection
  - • Verify the 24 V DC power connection

    • Inspect the cable and replace it if damaged

    • Measure the voltage with a multimeter, it must be 24 V DC, +/-10%

    • Replace the TopLight

    • Verify protections inside the electrical cabinet
* - **TopLight brightness varies**
  - • Unstable power supply

    • Loose connections

    • Undersized power supply

    • TopLight near end of life
  - • Verify power supply stability

    • Tighten all electrical connections

    • Verify current draw against power supply capacity

    • Replace the TopLight
* - **TopLight overheats**
  - • Insufficient ventilation

    • Excessive current

    • Continuous 100% duty cycle
  - • Improve air circulation around the TopLight

    • Verify that current draw does not exceed specifications

    • Implement intermittent duty cycle when possible
```

(troubleshooting_multi)=
## Multi-device configuration issues

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **System with 2-3 FlexiBowl units: only one communicates**
  - • FlexiBowl units powered off  
    • Duplicate IP addresses  
    • Crossed cabling  
  - • Verify that every FlexiBowl is powered on  
    • Assign a unique IP to each FlexiBowl, for example `192.168.1.10`, `.11`, `.12`  
    • Verify correct star cabling, no daisy-chain  
* - **System with 2-3 cameras: only one acquires**
  - • Insufficient power supply
    • Camera IP addresses in conflict
  - • Verify that supply voltage is within 6-26 V
    • Configure a unique static IP for each camera
    • Enable all cameras in [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)
* - **System with 2-3 hoppers: incorrect control**
  - • Hoppers not enabled individually in the software
    • Incorrect power supply
    • Wrong robot contact
  - • Enable each hopper in [Hopper Setup](../QUICKSTART/SETUP/13b_Hopper_Setup.md)
    • Check power supply
    • Check the robot contact wiring
```
