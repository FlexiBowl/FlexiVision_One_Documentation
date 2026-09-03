# **Wiring and Connections**
(troubleshooting_alimentazione)=
## FlexiBowl® power supply problems

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **READY LED does not light up**
  - • Power supply not connected properly
    
    • AC switch in 'O' position instead of 'I' position
    
    • Damaged power cable
    
    • Blown fuses inside front panel
  - • Check power connection according to FlexiBowl® manual
    
    • Set switch to position 'I' (ON)
    
    • Inspect cable for damage and replace if necessary
    
    • Contact technical support to replace fuse
* - **FlexiBowl® switches off** **accidentally**
  - • Loose power connection
    
    • Electrical interference
    
  - • Tighten power connections
    
    • Connect to dedicated line with EMI filter

```
(troubleshooting_ethernet)=
## Ethernet Connection Problems

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible causes
  - Solutions
* - **FlexiBowl® not communicating with VisionController**
  - • FlexiBowl® not switched on (READY LED off)  
    • Ethernet cable not properly connected to the FlexiBowl® and/or VisionController  
    • Ethernet cable damaged    
    • Wrong IP address  
    • FlexiBowl® and VisionController on different subnets  
    • Firewall blocks communication  
    • VisionController Ethernet port faulty  
  - • Check that READY LED is lit on the FlexiBowl®  
    • Check physical Ethernet cable connection on both sides  
    • Test cable with cable tester or replace  
    • Check IP configuration in [FlexiBowl® Setup](../QUICKSTART/SETUP/13a_FB_Setup.md)  
    • Configure FlexiBowl® and VisionController in the same network (e.g: 192.168.1.x)  
    • Temporarily disable firewall for testing  
    • Try other Ethernet port of VisionController  
* - **Intermittent connection**  
  - • Cable too long (> 100m)  
    • RJ45 connector damaged or poorly crimped  
    • Electromagnetic interference  
  - • Reduce cable length below 100m or use intermediate switch  
    • Replace connectors or complete cable  
    • Use shielded cable (STP) away from EMI sources  
```
(troubleshooting_pneumatica)=
## Pneumatic Problems (Compressed Air)

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Flip does not work or very weak impulse**
  - • Compressed air not connected  
    • Damaged or obstructed pneumatic hose  
    • Pressure regulator closed or at minimum  
    
    • Insufficient pressure (< 5 bar)
    
    
    
    • Leaks in the pneumatic circuit
    
    
  - • Connect compressed air to the FlexiBowl® connection (see manual)  

    • Check hose for kinks/obstructions, replace if necessary  
    • Open pressure regulator on control panel  
    
    • Increase pressure to 5-6 bar
    
    
    
    • Inspect fittings with soapy water, tighten or replace
    
    
* - **Air-blow does not** **work**
  - • FlexiBowl® not set up with Air-Blow option  

    • Air diverters not externally fed   

    • Flow Regulators closed   

    • Insufficient air pressure  
  
    
    • Faulty solenoid valve
  - • Check that the FlexiBowl® ordered has the Option Blow Test entry at True in the production sheet   

    • Check that external Pneumatic supply is present (hose supplied)     

    • If there are several air diverters, check that the flow regulator on the side of the FlexiBowl® is set above zero     

    • Check air pressure (5-6 bar)    

    
    • follow [Instructions]()
```
(troubleshooting_connessione_camera)=
## Camera Connection Problems

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Camera not detected by VisionController**
  - • Camera Ethernet cable not connected
    
    • Camera connected to non-POE port of VisionController
    

    
    • Camera IP address conflicts with those of other devices in the same sub-network  
    • VisionController POE port faulty
  - • Check physical camera cable connection  
    • Connect camera ONLY to VisionController POE port  
    • Reset camera IP or configure unique static IP    
    • Try other VisionController POE port  
* - **Camera image black or absent**
  - • Light off   
    • Camera exposure too low  
    • Lens protective cap not removed    
    • Lens not installed    
    • Camera not powered (POE not active)  
    
     
    • Faulty camera  
  - • Check that the light is switched on   
    • Increase exposure in [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
    • Remove lens protection cap   
    • Install lens with correct focal length  
    • Check camera LED is switched on (POE indicator active)  
    • Replace camera  

* - **Camera disconnects accidentally**
  - • Insufficient POE power supply (power < camera demand)
    
    • Damaged cable
    
    • Camera overheating
    
    • POE port damaged
  - • Check available POE power   
    • Replace Ethernet cable  
    
    • Improve camera area ventilation  
    
    • Replace POE switch or VisionController port  
```
(troubleshooting_connessione_toplight)=
## Toplight Connection Problems
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **Toplight does not switch on**
  - • 24V DC power supply not connected
    
    • Damaged power cable
    
    • Incorrect voltage (≠ 24V)
    
    • Toplight failure
    
    • Fuse blown/protection tripped
  - • Check 24V DC power connection
    
    • Inspect cable, replace if damaged
    
    • Measure voltage with multimeter, it must be 24V DC (±10%)
    
    • Replace toplight
    
    • Check protections in the electric panel
* - **Variable toplight brightness**
  - • Unstable power supply
    
    • Loose connections
    
    • Undersized power supply
    
    • Toplight at end of life
  - • Check supply voltage stability
    
    • Tighten all electrical connections
    
    • Check current consumption against power supply capacity
    
    • Replace toplight
* - **Toplight overheats**
  - • Insufficient ventilation
    
    • Overcurrent
    
    • 100% continuous duty cycle
  - • Improve air circulation around toplight
    
    • Check current consumption does not exceed specifications
    
    • Implement intermittent duty cycle if possible
```
(troubleshooting_multi)=
## Multi-Device Configuration Problems
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problem
  - Possible Causes
  - Solutions
* - **System with 2-3 FlexiBowl®: only one communicates**
  - • FlexiBowl® switched off  
    • Duplicate IP addresses  
    • Crossed cables  
  - • Check that the FlexiBowl® is switched on  
    • Assign unique IPs to each FlexiBowl® (e.g: 192.168.1.10, .11, .12)  
    • Check correct star wiring (no daisy-chain)  
* - **System with 2-3 cameras: only one** **capture**s  
  - • Insufficient power supply   
    • Conflicting camera IP addresses  
  - • Check that power supply is between 6 - 26 V  
    • Configure unique static IP for each camera  
    • Enable all cameras in [Camera Setup](../QUICKSTART/SETUP/13d_Camera_Setup.md)  
* - **System with 2-3 hoppers: incorrect control**  
  - • Hoppers not individually enabled in software  
    • Wrong power supply   
    • Wrong robot contact   
  - • Enable each hopper in [Hopper Setup](../QUICKSTART/SETUP/13b_Hopper_Setup.md)  
    • Check power supply  
    • Check contact to robot   
```



